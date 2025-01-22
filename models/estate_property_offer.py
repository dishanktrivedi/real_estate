from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer Model"
    _order = "price desc"

    price = fields.Float(string='Price')
    partner_id = fields.Many2one('res.partner', string='Partners')
    property_id = fields.Many2one('estate.property', string='Property')
    validity = fields.Integer(string="Validity (Days)", default=7)

    property_type_id = fields.Many2one(
        'estate.property.type',
        string="Property Type",
        related='property_id.property_type_id',
        store=True
    )

    status = fields.Selection(
        string='Status',
        copy=False,
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ])

    date_deadline = fields.Date(string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
        store=True)

    _sql_constraints = [
        ('check_offer_price', 'CHECK(price > 0)',
         'The offer price must be strictly positive.'),
    ]

    @api.constrains('price')
    def _check_offer_price(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("Offer price must be strictly positive.")

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        """Compute the deadline date by adding validity to create_date."""
        for record in self:
            create_date = record.create_date or fields.Date.today()
            record.date_deadline = create_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        """Inverse function to update validity based on date_deadline change."""
        for record in self:
            create_date = record.create_date.date() if record.create_date else fields.Date.today()
            if record.date_deadline:
                delta = (record.date_deadline - create_date).days
                record.validity = delta if delta >= 0 else 0

    def action_accept_offer(self):
        """Accept the current offer and set the selling price and buyer."""
        for offer in self:
            if offer.property_id.state == 'sold':
                raise UserError(_("You cannot accept an offer for a sold property."))

            # Ensure only one offer can be accepted
            if offer.property_id.offer_ids.filtered(lambda o: o.status == 'accepted'):
                raise UserError(_("An offer has already been accepted for this property."))

            offer.status = 'accepted'
            offer.property_id.selling_price = offer.price
            offer.property_id.partner_id = offer.partner_id
            offer.property_id.state = 'offer_accepted'

    def action_refuse_offer(self):
        """Refuse the current offer."""
        for offer in self:
            if offer.status == 'accepted':
                raise UserError(_("You cannot refuse an already accepted offer."))
            offer.status = 'refused'

    @api.model
    def create(self, vals):
        # Instantiate the property object using the property_id from vals
        property_id = self.env['estate.property'].browse(vals.get('property_id'))

        # Check if the new offer price is higher than any existing offer for the same property
        if property_id.best_price < vals.get('price'):
            # Create the offer as usual
            offer = super(EstatePropertyOffer, self).create(vals)

            # Set the property state to "Offer Received"
            if property_id.state != 'sold' and property_id.state != 'canceled':
                property_id.state = 'offer_received'

            return offer

        else:
            raise ValidationError(_("The offer price cannot be lower than an existing offer."))