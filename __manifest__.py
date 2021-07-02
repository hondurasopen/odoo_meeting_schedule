# -*- coding: utf-8 -*-
{
    'name': "Odoo Meeting Schedule",
    'summary': """
        Módule for Odoo Meeting Schedule
        """,
    'description': """
         Módule for Odoo Meeting Schedule
    """,
    'author': "César Alejandro Rodriguez Castillo",
    'category': 'General',
    'version': 'V14',
    'depends': ['base', 'account', 'analytic'],
    'data': [
        #"data/secuencias.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/main_menu_view.xml",
        "views/meeting_view.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
