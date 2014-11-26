# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Andrea Cometa - Perito informatico
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

from osv import osv
from tools.translate import _


class account_invoice(osv.osv):

    _inherit = "account.invoice"

    def unlink(self, cr, uid, ids, context=None):
        for invoice in self.browse(cr, uid, ids, context):
            # ----- get the sequence from journal
            sequence_id = invoice.journal_id.sequence_id and \
                invoice.journal_id.sequence_id.id or False
            if not sequence_id:
                raise osv.except_osv(
                    _('Error'),
                    _('Set a sequence for the journal!'))
            # ----- Recovers the sequence
            self.pool.get('ir.sequence_recovery').set(
                cr, uid, [invoice.id], 'account.invoice',
                'internal_number', '', sequence_id)
        return super(account_invoice, self).unlink(cr, uid,
                                                   ids, context)

account_invoice()
