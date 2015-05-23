# -*- coding: utf-8 -*-

import time
import l10n_co_invoice_amount_to_text

from openerp.report import report_sxw
from openerp import pooler


class resolucion(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(resolucion, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
                                  'time': time,
                                  })
        #~ self.context = context

report_sxw.report_sxw('report.resolucion', 'account.invoice',
                      'addons/base_co/report/resolucion.rml',
                      parser=resolucion)
