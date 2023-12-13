
{
    'name': 'Custom Module',
    'sequence': -100,
    'version': '1.1',
    'category': 'Apps',
    'summary': 'Sales Teams - Marketing',
    'author': 'Krushal Kalkani',
    'depends': ['product', 'sale', 'stock'],
    'data': [
        "security/ir.model.access.csv",
        "security/security_group.xml",
        "views/vehicle_data.xml",
        "views/sale_view_order_form_inherit.xml",
        'views/stock_picking_inherited.xml',
        "views/vehicle_data_quotation_report.xml",
        "views/insurance_details.xml",
        "views/insurance_configuration.xml",
        "views/menu.xml",
    ],
    'license': 'LGPL-3',
}
