# -*- coding: utf-8 -*-
# Copyright 2015-2017 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "Custom Pnt",
    'version': '12.0.0.0.1',
    'category': 'Generic Modules/Accounting',
    'summary': "Personalizaciones Cliente",
    'author': "Carlos Ramos Hernandez <cramos@puntsistemes.es>",
    'website': 'https://github.com/OCA/account-financial-tools',
    'license': 'AGPL-3',
    'depends': ['analytic'],
    'data': [
        'security/ir.model.access.csv',
        'view/name_view.xml',
        # 'wizard/name_wizard.xml',
    ],
    'test': [
    ],
    'installable': True,
}
