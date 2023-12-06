{
    'name': "School Management",
    'version': '16.0.1.0.0',
    'summary': 'Manage your School Data!',
    'sequence': -200,
    'description': """
        Student managemnet module which help to maintain the student data.
    """,
    'category': "School",
    'website': "https://krushaalkalkani.github.io/Krushal-Kalkani-Online-Resume/",
    'depends': ['base', 'mail', 'sale', 'website'],
    'author': "Krushal Kalkani",
    'assets': {
        'web.assets_backend': [
            'school_management/static/src/components/**/*',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/school_management.xml',
        'views/teacher_management.xml',
        'views/res_config_setting.xml',
        'views/sales_res_config_setting.xml',
        'report/student_report_template.xml',
        'report/student_email_template.xml',
        'data/cron_job.xml',
        'views/menu.xml'
    ],
    'demo': [
        'demo/demo_data.xml'
    ],
    'license': "LGPL-3",
    'application': True,
    'demo': True,
    'auto_install': True,
    'installable': True
}
