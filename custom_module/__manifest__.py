
{
    'name': 'Custom Module',
    'sequence': -100,
    'version': '1.1',
    'category': 'Apps',
    'summary': 'Sales Teams - Marketing',
    'author': 'Krushal Kalkani',
    'depends': ['product', 'sale'],
    'data': [
        "security/ir.model.access.csv",
        "views/vehicle_data.xml",
        "views/vehicle_details.xml",
        "views/new_field.xml",
        "views/menu.xml",
    ],
    'license': 'LGPL-3',
}
