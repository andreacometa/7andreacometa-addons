# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from osv import osv, fields
import netsvc
from tools.translate import _


class account_invoice_line(osv.osv):

	_name = 'account.invoice.line'
	_inherit = 'account.invoice.line'

	def on_change_report_line_type(self, cr, uid, ids, report_line_type):
		if not report_line_type in ('t', 'n', 's'):
			return {}
		return {'value': {
			'product_id': False,
			'quantity': 0.0,
			'price_unit': 0.0,
			'uos_id': False,
			'discount' : 0.00,
			'invoice_line_tax_id' : False,
			}
		}

	_columns = {
		'report_line_type' : fields.selection(
			(('p', 'Product'),('t', 'Title'),('n', 'Note'),('s', 'Separator')),
			'Line Type'),
		}

	_defaults = {
		'report_line_type' : 'p',
		}

account_invoice_line()
