from odoo import models, fields, api, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property Model"
    _order = "id desc"

    name = fields.Char(required=True, string='Name')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postal Code')
    date_availability = fields.Date(string='Availability From' ,default=lambda self: (datetime.today() + timedelta(days=90)).date(), copy=False)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Number of Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facedes')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ],
        help="One can choose the garden orientation of the house.")
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ],
        string='State',
        required=True,
        default='new',
        copy=False
    )

    user_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    total_area = fields.Float(string="Total Area (sqm)", compute='_compute_total_area', store=True,
        help="Total area calculated as the sum of living area and garden area.")
    best_price = fields.Float(
        string='Best Offer Price',
        compute='_compute_best_price',
        store=True,
        help="The highest offer price from all related offers."
    )

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The expected price must be strictly positive.'),
        ('check_selling_price', 'CHECK(selling_price >= 0)',
         'The selling price must be positive.'),
    ]

    @api.constrains('expected_price', 'selling_price')
    def check_price(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError("Expected price must be strictly positive.")
            if record.selling_price < 0:
                raise ValidationError("Selling price must be positive.")

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            # Allow selling_price to be zero until an offer is validated
            if float_is_zero(record.selling_price, precision_digits=2):
                continue  # Skip the validation if selling price is zero

            # Calculate 90% of the expected price
            min_acceptable_price = record.expected_price * 0.90

            # Compare selling price with the minimum acceptable price
            if float_compare(record.selling_price, min_acceptable_price, precision_digits=2) == -1:
                raise ValidationError(
                    "Selling price cannot be lower than 90% of the expected price."
                )

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = (record.living_area or 0) + (record.garden_area or 0)

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'), default=0.0)

    @api.onchange('garden')
    def _onchange_garden(self):
        """Set default values for garden area and orientation when garden is True, otherwise clear them."""
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def action_set_sold(self):
        """Set the property state to 'sold' if not canceled."""
        for record in self:
            if record.state == 'canceled':
                raise UserError(_("A canceled property cannot be sold."))
            record.state = 'sold'

    def action_set_canceled(self):
        """Set the property state to 'canceled' if not already sold."""
        for record in self:
            if record.state == 'sold':
                raise UserError(_("A sold property cannot be canceled."))
            record.state = 'canceled'


    def _update_state_on_offer(self):
        """Method to update the state to 'offer_received' when an offer is made"""
        for record in self:
            if record.offer_ids:
                record.state = 'offer_received'


    @api.ondelete(at_uninstall=False)
    def _check_state_before_delete(self):
        """Prevent deletion of properties if state is not 'New' or 'Canceled'."""
        if any(property.state not in ['new', 'canceled'] for property in self):
            raise UserError(_("You can only delete properties in 'New' or 'Canceled' state."))