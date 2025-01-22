from odoo import models, fields

class InheritedModel(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property',
                                   'user_id',
                                   string="Properties of Salesman",
                                   domain=[('state', 'in', ['new', 'offer_received'])])

