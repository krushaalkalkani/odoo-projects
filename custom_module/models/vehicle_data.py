# models.py

from odoo import models, fields
from odoo.exceptions import AccessError


class AddVehicle(models.TransientModel):
    _name = 'vehicles.data'

    vehicle_part_number = fields.Char(
        string="Vehicle Part Number", required=True)
    vehicle_chassis_number = fields.Char(
        string="License Number", required=True)

    security_group_id = fields.Many2one('res.groups', string='Security Group', required=True,
                                        default=lambda self: self.env.ref('custom_module.vehicle_admin_group'))

    def add_vehicle_data(self):
        user_has_access = self.env.user.groups_id & self.security_group_id
        if not user_has_access:

            raise AccessError(
                "You do not have the required permissions to perform this action.")

        context = dict(self._context)
        print(context, ">>>>>>>>>>>>>>>>>>>>hello")
        order_id = context.get('default_sale_order_id') or False
        sale_order_id = self.env['sale.order'].browse(order_id)
        sale_order_id.vehicle_part_number = self.vehicle_part_number or " "
        sale_order_id.vehicle_chassis_number = self.vehicle_chassis_number or ""
        sale_order_id.is_add_vehicle_data = True
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'The Vehicle data update successfully',
                'type': 'rainbow_man'
            }
        }
