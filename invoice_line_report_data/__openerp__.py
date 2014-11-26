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

{
	'name': 'Invoice Line Report Data',
	'version': '1.0',
	'category': 'Account',
	'description': """ENG: This module allows you to insert report information in account invoice line and manage them in your report\n
	ITA: Questo modulo consente di inserire alcune informazioni utili ai report così da gestire meglio i dagti nel report stesso.
	""",
	'author': 'www.andreacometa.it',
	'website': 'http://www.andreacometa.it',
	'depends': ['account'],
	'update_xml': [
		'invoice_view.xml',
		],
	'installable': True,
	'active': False,
	'images' : ['images/invoice_line_report_note.jpg'],
}

