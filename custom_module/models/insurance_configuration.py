from odoo import models, fields


class InsuranceConfigurance(models.Model):
    _name = 'insurance.configuration'

    customer_name = fields.Char(string="Customer Name")
    