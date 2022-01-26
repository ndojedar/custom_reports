# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    albaran = fields.Char(string='Albarán', readonly=True, required=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('albaran', 'New') == 'New':
            vals['albaran'] = self.env['ir.sequence'].next_by_code('acc.alb') or 'New'
        result = super(AccountMove, self).create(vals)
        return result

