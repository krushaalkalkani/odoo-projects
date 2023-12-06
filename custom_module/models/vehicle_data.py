from odoo import models, fields, api


class AddVehicle(models.TransientModel):
    _name = 'vehicles.data'

    vehicle_part_number = fields.Char(string="Vehicle Part Number")
    vehicle_chassis_number = fields.Char(string="License Number")

    def add_vehicle_data(self):
        context = dict(self._context)
        order_id = context.get('params').get('id') or False
        sale_order_id = self.env['sale.order'].browse(order_id)
        sale_order_id.vehicle_part_number = self.vehicle_part_number or " "
        sale_order_id.vehicle_chassis_number = self.vehicle_chassis_number or ""
        sale_order_id.is_add_vehicle_data = True
        return True



