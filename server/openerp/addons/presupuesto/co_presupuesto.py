# -*- coding: utf-8 -*-
##############################################################################
# Hereda el modulo res.parner y se agregan los campo para la localizacion colombiana
# Inherits res.parner module and add the field to the Colombian location
##############################################################################

import openerp
import re
import codecs
from openerp.osv import fields, osv
from openerp.tools.translate import _

import time


#~ Creación de campos
#~ Creating Fields 

class co_presupuesto(osv.osv):
    _name = 'presupuesto'
    _order = 'idcodigo'    
    _columns = {
        'idcodigo': fields.char('Code', size=25, requerid=True),
        'name': fields.char('Name', size=150),
        }

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name','idcodigo'], context)
        res = []
        for record in reads:
            name = record['name']
            if record['idcodigo']:
                name = record['idcodigo'] + ' - ' + name
            res.append((record['id'], name))
        return res

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
        args = args or []
        ids = []
        if name:
            ids = self.search(cr, uid, [('idcodigo', 'ilike', name)] + args, limit=limit, context=context)
            if not ids:
                ids = self.search(cr, uid, [('name', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)    
    
co_presupuesto()


