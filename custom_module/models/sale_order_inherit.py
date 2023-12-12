from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = ['sale.order']

    vehicle_part_number = fields.Char(
        string="Vehicle Part Number", store=True, tracking=True)
    vehicle_chassis_number = fields.Char(
        string="License Number", store=True, tracking=True)
    is_add_vehicle_data = fields.Boolean(
        default=False, string="Is Add Vehicle Data?")

    def update_vehicle_data(self):
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
                'default_sale_order_id': self.id,
                'default_vehicle_part_number': self.vehicle_part_number,
                'default_vehicle_chassis_number': self.vehicle_chassis_number
            },
        }

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        for picking in self.picking_ids:
            picking.write({
                'vehicle_part_number': self.vehicle_part_number,
                'vehicle_chassis_number': self.vehicle_chassis_number,
            })

        return res
