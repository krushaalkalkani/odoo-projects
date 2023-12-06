from odoo import fields, models

class Aura(models.Model):
    
    _name = "aura.profile"
    _description = "Test Model"
    # print this 
    
    name = fields.Char(string="Your Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone", required=True)
    description = fields.Char(string="Write Description")
    date = fields.Date(string="Select the Date", required=True)
    price = fields.Float(string="What the Price(You can enter fractional part of your price)", required=False)