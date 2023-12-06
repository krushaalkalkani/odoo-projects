{
    'name': 'Web Site - Task',
    'sequence': '-100',
    'version': '1.1',
    'category': 'Apps',
    'summary': 'Website Which Help to Create a You Business',
    'description': """
        It Help to buy and sale your...
        ============================================
    """,
    'author': 'Krushal Kalkani',
    'website': 'http://www.kanakinfosystems.com',
    'images': ['static/description/icon.png'],
    'assets': {
        'web.assets_frontend': [
            'website_task/static/src/scss/styles.css',
            'website_task/static/src/js/dynamic_template.js',
            'website_task/static/src/js/main.js',
            # 'website_task/static/src/js/success.js',
            # 'website_task/static/src/xml/main_template.xml',
        ],
    },
    'data': [
        "security/ir.model.access.csv",
        "views/snippets/school_info.xml",
        "views/snippets/snippets.xml",
        "views/school_info.xml",
        "views/main_template.xml",
        "views/menu.xml",
    ],
    'application': True,
    'license': 'LGPL-3',
}
