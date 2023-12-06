from odoo import models, fields


class SchoolInfo(models.Model):
    _name = 'school.info'
    _description = "All the Information about school"

    school_name = fields.Text()
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one(
        'res.country.state', domain="[('country_id', '=?', country_id)]", string="City/State")
    image = fields.Binary()
