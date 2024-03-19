# -*- coding: utf-8 -*-
# Email: sales@creyox.com

from odoo import models, fields, api, _


class MultiCompanySOPO(models.TransientModel):
    _name = 'wo.confirmation'
    _description = 'Work Order Confirmation'

    def action_apply(self):
        active_ids = self.env['mrp.workorder'].browse(self.env.context.get('active_ids'))
        context = self._context.copy()
        for wo in active_ids:
            context.update({'skip_component_status': wo.id})
            return wo.with_context(context).button_start()
