# -*- coding: utf-8 -*-
{
    'name': "My Website",
    'summary': """ Building a website. """,
    'description': """
Build a website based on a Tutorial of Odoo Official Documentation.
""",
    'author': "Ahlem Mehri",
    'website': "http://www.mehriahlem-dz.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Developpement - Version Odoo 14',
    'version': '0.1',
    'sequence': '1',
    # any module necessary for this one to work correctly
    'depends': ['website_sale'],
    # always loaded
    'data': [
        # demo : data for demontration
        'demo/product_template_demo.xml',
        'demo/teacher_demo.xml',
        'demo/student_demo.xml',
        'demo/course_demo.xml',
        # data : files to load at module install
        'data/mywebsite_templates.xml',
        'data/my_website_data.xml',
        # Security : always load groups first
        #          : load access rights after groups
        'security/ir.model.access.csv',
        # views
        'views/teacher_teacher_views.xml',
        'views/student_student_views.xml',
        'views/course_course_views.xml',
        # menus
        'views/mywebsite_menuitem.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    # 'qweb': [
    # ],
    # 'images': [
    # ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
