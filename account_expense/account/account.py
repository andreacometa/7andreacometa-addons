# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
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

from openerp.osv import fields, orm
from tools.translate import _


class account_expense(orm.Model):

    _name = "account.expense"
    _description = "Account expenses"

    _columns = {
        'name': fields.char('Name', size=64),
        'account_id': fields.many2one('account.account', 'Account'),
        'price': fields.float('Price'),
        'tax_id': fields.many2one('account.tax', 'Tax'),
        'type': fields.selection(
            (('bank', 'Bank'), ('delivery', 'Delivery')),
            'Type'),
        }

account_expense()


class account_payment_term_line(orm.Model):

    _name = "account.payment.term.line"
    _inherit = "account.payment.term.line"

    _columns = {
        'expense_id': fields.many2one('account.expense', 'Expense'),
        }

account_payment_term_line()
