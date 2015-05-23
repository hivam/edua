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

#~ Creación de campos
#~ Creating Fields 

class res_partner_co(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'tdoc': fields.selection((('12','Tarjeta de identidad'),
                                  ('13','Cédula de ciudadanía'),
                                  ('21','Tarjeta de extranjería'),
                                  ('22','Cédula de extranjería'),
                                  ('31','NIT'),
                                  ('41','Pasaporte'),
                                  ('42','Documento de identificación extranjero'),
                                  ('43','Sin identificación del exterior o para uso definido por la DIAN')),
                                  'Tipo de Documento', required=True),
        'dv': fields.char('dv', size=1),
        'lastname': fields.char('lastname', size=25),
        'surname': fields.char('surname', size=25),
        'firtsname': fields.char('firtsname', size=25),
        'middlename': fields.char('middlename', size=25),
    }
    
    _defaults = {
        'tdoc': '13',
        }
             
 #~ Función para concatenar los apellidos y nombres y almacenarlos en el campo name
 #~ Function to concatenate the names and surnames and store them in the name field

    def onchange_name(self, cr, uid, ids, lastname, surname, firtsname, middlename, context=None):
        res = {'value':{}}
        res['value']['name'] = "%s %s %s %s" %(lastname, surname or '', firtsname, middlename or '')
        return res


    def _check_name(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            is_company = record.is_company
            name = record.name
            lastname = record.lastname
            surname = record.surname
            firtsname = record.firtsname
            middlename = record.middlename
            newname = "%s %s %s %s" %(lastname, surname or '', firtsname, middlename or '')
            if not is_company and name != newname:
                return False
            elif is_company and (lastname or surname or firtsname or middlename):
                return self.write(cr, uid, ids, {'lastname': '', 'surname': '', 'firtsname': '', 'middlename':  ''}, context=context)
        return True

## Función para validar que la identificación sea sólo numerica
## Function to validate the numerical identification is only

    def _check_ident_num(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            ref = record.ref
            if ref != False:
                if re.match("^[0-9]+$", ref) == None:
                    return False
        return True
               
## Función para validar que la identificación tenga más de 6 y dígitos y menos de 11
## Function to validate that the identification is more than 6 and less than 11 digits

    def _check_ident(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            ref = record.ref
            if len(ref) <6:
                return False
            if len(ref) >11:
                return False
        return True


## Función para validar el dígito de verificación
## Function to validate the check digit

    def _check_dv(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            ref = record.ref
            dv = record.dv
            tdoc = record.tdoc
            dvcal = 'dvcal',
            if tdoc == '31':
                if ref != False:
                    if ref.isdigit():
                        b= '0'*(15-len(ref)) + ref
                        vl=list(b)
                        op=(int(vl[0])*71+int(vl[1])*67+int(vl[2])*59+int(vl[3])*53+int(vl[4])*47+int(vl[5])*43+int(vl[6])*41+int(vl[7])*37+int(vl[8])*29+int(vl[9])*23+int(vl[10])*19
                            +int(vl[11])*17+int(vl[12])*13+int(vl[13])*7+int(vl[14])*3)%11
                        
                        if op in (0,1):
                            dvcal = str(op)
                        else:
                            dvcal = str(11-op)
                        if  dv != dvcal:
                            return False
        return True                

# Mensajes de error
# Error Messages
 
    _constraints = [
        (_check_name, 'Error ! el nombre es diferente ', ['name']),
        (_check_ident, 'Error ! menor o mayor cantidad de números esperados', ['ref']),
        (_check_dv, 'Error ! revise el valor del digito de verificación',['dv']),
        (_check_ident_num, 'Error !''El número de identificación sólo permite números', ['ref']),

        ]

res_partner_co()
