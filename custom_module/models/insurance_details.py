from odoo import models, fields


class InsuranceDetails(models.Model):
    _name = 'insurance.details'

    customer_name = fields.Char(string="Customer Name")
    # insurance_type - This field is m2o field
    insurance_amount = fields.Float(string="Insurance Amount")
    # insurance_valid_type = fields.Selection()
    # insurance_validity_days = fields.d 
    # insurance_expired_date = 
