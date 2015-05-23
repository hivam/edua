# -*- coding: utf-8 -*-
##############################################################################
#  Modulo para crear terceros según las normas Colombianas
##############################################################################

{
    'name' : 'Localización Colombia',
    'version': '1.0',
    'depends': [
        'base','account', 'presupuesto',
        ],
    'author': 'Maelcoc',
    'category': '',
    'description': """
Modificación para localización de tercero en colombia
    """,
    'website': '',
    'data': ['base_co_view.xml', 'account_invoice_imp.xml',],
    'update_xml': [ 'resolucion.xml', ],
    'auto_install': False,
    'installable': True,
}
