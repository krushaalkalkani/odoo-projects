from odoo import models, fields


class StockPickingInherited(models.Model):
    _inherit = 'stock.picking'

    vehicle_part_number = fields.Char(string="Vehicle Part Number")
    vehicle_chassis_number = fields.Char(string="License Number")
