from odoo import api, fields, models


class CustomFieldsPos(models.Model):
    _inherit = "pos.config"

    locations = fields.Many2many(
        'sale.location', string='Locations', help='Locations available')


class CustomFieldsRes(models.TransientModel):
    _inherit = 'res.config.settings'
    # _name = "custom.field"

    pos_locations = fields.Many2many(
        readonly=False, related='pos_config_id.locations', string='Locations', help='Locations available')


class ConfigLocation(models.Model):
    _name = "sale.location"
    _rec_name = "sale_location"

    sale_location = fields.Char(string="Location")


class LoadDataPos(models.Model):
    _inherit = "pos.session"

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result.append("sale.location")
        print(result)
        return result

    def _loader_params_sale_location(self):
        return {
            "search_params": {
                "fields": ["sale_location"],
            }
        }

    def _get_pos_ui_sale_location(self, params):
        return self.env["sale.location"].search_read(**params["search_params"])
