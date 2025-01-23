from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag Model"
    _order = "name asc"  # Orders the tags alphabetically by name

    # Name of the property tag, required field
    name = fields.Char(string="Name", required=True)

    # Color associated with the tag, represented as an integer
    color = fields.Integer(string="Color")

    # SQL constraint to ensure that property tag names are unique
    _sql_constraints = [
        ('unique_property_tag_name', 'UNIQUE(name)',
         'The property tag name must be unique.'),
    ]
