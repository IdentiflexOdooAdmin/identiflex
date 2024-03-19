# -*- coding: utf-8 -*-
# Email: sales@creyox.com

from odoo import models, fields, api, _


class ResCompany(models.TransientModel):
    _inherit = 'res.config.settings'

    group_restrict_wo = fields.Boolean(implied_group='shvm_restrict_workorder.group_restrict_wo')
    group_confirmation_wo = fields.Boolean(implied_group='shvm_restrict_workorder.group_confirmation_wo')

    @api.onchange('group_restrict_wo')
    def onchange_wo_restrict(self):
        if self.group_restrict_wo:
            self.group_confirmation_wo = False

    @api.onchange('group_confirmation_wo')
    def onchange_wo_confirmation(self):
        if self.group_confirmation_wo:
            self.group_restrict_wo = False

