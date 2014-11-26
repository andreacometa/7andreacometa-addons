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

import time
from report import report_sxw
import inspect
import os
from datetime import datetime
from osv import osv
from osv import fields


class Parser(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'datetime': datetime,
            'time': time,
            'cr': cr,
            'uid': uid,
            'GroupDueDate': self.group_by_due_date,
            'GetDueDateSum': self.get_due_date_sum,
        })

    def group_by_due_date(self, objects):
        # ----- Create list of valid maturities
        due_dates = []
        maturities = {}
        for maturity in objects:
            if not (maturity.date_maturity or maturity.date) in maturities:
                maturities.update({
                    (maturity.date_maturity or maturity.date): [maturity]})
            else:
                maturities[maturity.date_maturity or maturity.date].append(
                    maturity)
        return maturities

    def get_due_date_sum(self, lines, type):
        amount = 0.0
        for line in lines:
            if type == 'amount_residual':
                if line['debit'] == 0.0:
                    amount -= line[type]
                    continue
            amount += line[type]
        return amount
