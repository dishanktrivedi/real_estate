from odoo import models, fields

class InheritedModel(models.Model):
    # Inherit the 'res.users' model to add custom fields specific to users
    _inherit = 'res.users'

    # One2many relationship with the 'estate.property' model to link properties managed by the user (salesman)
    # The domain restricts the properties to those with states 'new' or 'offer_received'
    property_ids = fields.One2many('estate.property',
                                   'user_id',  # The field 'user_id' in 'estate.property' model links the properties to users
                                   string="Properties of Salesman",  # The label displayed in the UI
                                   domain=[('state', 'in', ['new', 'offer_received'])])  # Restricts properties to certain states
