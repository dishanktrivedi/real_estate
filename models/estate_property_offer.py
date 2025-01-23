from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer Model"
    _order = "price desc"

    # Price of the offer
    price = fields.Float(string='Price')

    # Partner making the offer
    partner_id = fields.Many2one('res.partner', string='Partners')

    # The related property for the offer
    property_id = fields.Many2one('estate.property', string='Property')

    # Validity of the offer in days, default is 7
    validity = fields.Integer(string="Validity (Days)", default=7)

    # Property type, related to the property record
    property_type_id = fields.Many2one(
        'estate.property.type',
        string="Property Type",
        related='property_id.property_type_id',
        store=True
    )

    # Status of the offer, either accepted or refused
    status = fields.Selection(
        string='Status',
        copy=False,
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ])

    # Deadline for the offer based on its validity
    date_deadline = fields.Date(string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
        store=True)

    # SQL constraints to ensure offer price is strictly positive
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price > 0)',
         'The offer price must be strictly positive.'),
    ]

    @api.constrains('price')
    def _check_offer_price(self):
        """Validate that the offer price is greater than zero."""
        for record in self:
            if record.price <= 0:
                raise ValidationError("Offer price must be strictly positive.")

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        """Compute the deadline date by adding validity (in days) to the creation date."""
        for record in self:
            create_date = record.create_date or fields.Date.today()
            record.date_deadline = create_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        """Inverse function to update validity based on date_deadline change."""
        for record in self:
            # If create_date is None, use today's date
            create_date = record.create_date.date() if record.create_date else fields.Date.today()
            if record.date_deadline:
                # Calculate the difference in days between deadline and creation date
                delta = (record.date_deadline - create_date).days
                record.validity = delta if delta >= 0 else 0

    def action_accept_offer(self):
        """Accept the current offer, set selling price and partner (buyer), and change property state."""
        for offer in self:
            # Ensure the property is not already sold before accepting the offer
            if offer.property_id.state == 'sold':
                raise UserError(_("You cannot accept an offer for a sold property."))

            # Ensure only one offer can be accepted at a time for a property
            if offer.property_id.offer_ids.filtered(lambda o: o.status == 'accepted'):
                raise UserError(_("An offer has already been accepted for this property."))

            # Accept the offer and update property details
            offer.status = 'accepted'
            offer.property_id.selling_price = offer.price
            offer.property_id.partner_id = offer.partner_id
            offer.property_id.state = 'offer_accepted'

    def action_refuse_offer(self):
        """Refuse the current offer."""
        for offer in self:
            # Prevent refusing an already accepted offer
            if offer.status == 'accepted':
                raise UserError(_("You cannot refuse an already accepted offer."))
            # Refuse the offer
            offer.status = 'refused'

    @api.model
    def create(self, vals):

        """Create a new offer and ensure its price is higher than any existing offer for the same property."""
        # Instantiate the property object using the property_id from vals
        #TODO
        property_id = self.env['estate.property'].browse(vals.get('property_id'))

        # Check if the new offer price is higher than any existing offer for the same property
        if property_id.best_price < vals.get('price'):
            # Create the offer as usual
            offer = super(EstatePropertyOffer, self).create(vals)

            # Set the property state to "Offer Received" if not already sold or canceled
            if property_id.state != 'sold' and property_id.state != 'canceled':
                property_id.state = 'offer_received'

            return offer
        else:
            # Raise validation error if the new offer price is lower than the best price
            raise ValidationError(_("The offer price cannot be lower than an existing offer."))
