from odoo import api, models, fields
from odoo.fields import datetime

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wiz'
    _description = 'Cancel Appointment Wizard'

    # default get_function
    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['cancel_date'] = datetime.now()
        return res

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment', domain=[('state','=','draft')])
    reason = fields.Text(string="Reason")
    cancel_date = fields.Datetime(string='Cancellation Date')

    def action_cancel(self):
        self.appointment_id.state = 'canceled'
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }