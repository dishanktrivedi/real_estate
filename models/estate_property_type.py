from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type Model"
    _order = "name asc"  # Orders the property types alphabetically by name

    # Sequence field to define the order of property types
    sequence = fields.Integer('Sequence')

    # Name of the property type, required field
    name = fields.Char(string="Name", required=True)

    # One2many relationship to estate.property model to link properties to this type
    property_ids = fields.One2many('estate.property',
                                   'property_type_id',
                                   string="Properties")

    # One2many relationship to estate.property.offer model to link offers to this type
    offer_ids = fields.One2many('estate.property.offer',
                                'property_type_id',
                                string="Offers")

    # Computed field to count the number of offers for this property type
    offer_count = fields.Integer(string="Offer Count", compute="_compute_offer_count", store=True)

    # SQL constraint to ensure that property type names are unique
    _sql_constraints = [
        ('unique_property_type_name', 'UNIQUE(name)',
         'The property type name must be unique.'),
    ]

    @api.depends('offer_ids')  # Trigger computation when offer_ids change
    def _compute_offer_count(self):
        """Compute the number of offers associated with this property type."""
        for record in self:
            record.offer_count = len(record.offer_ids)
