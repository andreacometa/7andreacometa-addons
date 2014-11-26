# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2013 Francesco OpenCode Apruzzese (<cescoap@gmail.com>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
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

from osv import fields, osv
from tools.translate import _

class res_partner(osv.osv):

	_inherit = "res.partner"

	def onchange_name(self, cr, uid, ids, name, context=None):
		if not name:
			return False
		warning = {}
		if not self.search(cr, uid, [('name', 'ilike', '%' + str(name) + '%')]):
			return False
		warning = {
			'title' : 'Attenzione!',
			'message' : 'Questo nome esiste già per un altro partner!'
			}
		return {'warning': warning}

res_partner()
