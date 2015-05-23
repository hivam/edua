# -*- coding: cp1252 -*-
##Función para calcular el dígito de verificación
from osv import fields,osv
import tools
import pooler
from tools.translate import _

class res_partner(osv.osv):
    _description='Partner'
    _inherit = "res.partner"
    _order = "ref"

   def onchange_doc_number(self, cr, uid, ids, doc_type,doc_number):
        result = {}
         if doc_type == 'NIT':
                if doc_number != False:
                    if doc_number.isdigit():
                        b= '0'*(15-len(doc_number)) + doc_number
                        vl=list(b)
                        op=(int(vl[0])*71+int(vl[1])*67+int(vl[2])*59+int(vl[3])*53+int(vl[4])*47+int(vl[5])*43+int(vl[6])*41+int(vl[7])*37+int(vl[8])*29+int(vl[9])*23+int(vl[10])*19
                            +int(vl[11])*17+int(vl[12])*13+int(vl[13])*7+int(vl[14])*3)%11
                        
                        if op in (0,1):
                            result['value']['check_digit']=str(op)
                        else:
                            result['value']['check_digit']=str(11-op)
            else:
                result['value']['check_digit']=''
        if person_type == 'legal':
            result['value']['show_legal_name']=True
        else:
            if person_type == 'natural' and doc_type != 'NIT':
                result['value']['show_legal_name']=False
            else:
                result['value']['show_legal_name']=True
        
        return result
