# -*- coding: utf-8 -*-
# Email: sales@creyox.com

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MrpWorkOrder(models.Model):
    _inherit = 'mrp.workorder'

    def button_start(self):
        for record in self:
            if record.production_id.components_availability != 'Available' and self.user_has_groups("shvm_restrict_workorder.group_restrict_wo"):
                raise ValidationError('Components are not available!')
            elif record.production_id.components_availability != 'Available' and self.user_has_groups("shvm_restrict_workorder.group_confirmation_wo") and not record.env.context.get('skip_component_status'):
                return {
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'view_id': self.env.ref('shvm_restrict_workorder.wo_confirmation_form_view').id,
                    'res_model': 'wo.confirmation',
                    'res_id': record.id,
                    'target': 'new',
                }
            elif record.production_id.components_availability != 'Available' and self.user_has_groups("shvm_restrict_workorder.group_confirmation_wo") and record.env.context.get('skip_component_status'):
                return super(MrpWorkOrder, record).button_start()
        return super(MrpWorkOrder, self).button_start()
