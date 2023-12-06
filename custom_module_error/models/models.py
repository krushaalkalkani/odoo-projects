from odoo import models, fields, api


class AddVehicle(models.Model):
    _name = 'vehicles.data'

    vehicle_part_number = fields.Char(string="Vehicle Part Number")
    licence_number = fields.Char(string="License Number")

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # vehicle_info = fields.Char(string='Vehicle Info')

    # @api.depends('vehicle_info')
    # def _compute_button_visibility(self):
    #     for order in self:
    #         order.show_update_information_button = bool(order.vehicle_info)

    # show_update_information_button = fields.Boolean(
    #     compute='_compute_button_visibility', string='Show Update Information Button', default=False
    # )

    vehicle_part_number = fields.Char(
        string="Vehicle Part Number",
        related='vehicles_data_id.vehicle_part_number',
        store=True
    )
    licence_number = fields.Char(
        string="License Number",
        related='vehicles_data_id.licence_number',
        store=True
    )

    vehicles_data_id = fields.Many2one('vehicles.data', string='Vehicles Data')
