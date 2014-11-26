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


class sale_order_line(osv.osv):

	_name = 'sale.order.line'
	_inherit = 'sale.order.line'

	def on_change_report_line_type(self, cr, uid, ids, report_line_type):
		if not report_line_type in ('t', 'n', 's'):
			return {}
		return {'value': {
			'product_id': False,
			'product_uom_qty': 0.0,
			'product_uos_qty': 0.0,
			'price_unit': 0.0,
			'discount' : 0.00,
			'tax_id' : False,
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

sale_order_line()
