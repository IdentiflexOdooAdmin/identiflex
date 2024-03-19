# -*- coding: utf-8 -*-
# Email: sales@creyox.com
{
    'name': "Restrict the Work Order when component not available | Confirmation on work order start",
    'author': 'Creyox Technologies',
    'version': '15.0',
    'price': '20.0',
    'currency': 'USD',
    'category': 'MRP',
    'sequence': '1',
    'depends': ['mrp'],
    'license': 'LGPL-3',
    'summary': 'Give the confirmation popup on work order start or restrict the work order to start if component status is not available.',
    'description': """
    Give the confirmation popup on work order start or restrict the work order to start if component status is not available.
    """,
    'data': [
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'wizard/wo_confirmation_wizard_views.xml',
        'views/res_config_settings_form_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.png'],
    'application': True,
    'installable': True,
    'auto_install': False
}
