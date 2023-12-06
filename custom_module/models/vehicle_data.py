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


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vehicle_part_number = fields.Char(string="Vehicle Part Number", store=True)
    vehicle_chassis_number = fields.Char(string="License Number", store=True)
    is_add_vehicle_data = fields.Boolean(
        default=False, string="Is Add Vehicle Data?")

    def button_update_vehicle_data(self):
        for rec in self:
            rec.is_add_vehicle_data = False
            sale_order_id = rec.id

        return {
            'name': 'Update Vehicle Data',
            'type': 'ir.actions.act_window',
            'res_model': 'vehicles.data',
            'view_mode': 'form',
            'view_id': self.env.ref('custom_module.vehicle_data_form_view').id,
            'target': 'new',
            'context': {
                'default_vehicle_part_number': self.vehicle_part_number,
                'default_vehicle_chassis_number': self.vehicle_chassis_number
            },
        }
