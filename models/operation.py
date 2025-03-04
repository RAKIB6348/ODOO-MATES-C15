from odoo import api, fields, models


class HospitalOperation(models.Model):
    _name = 'hospital.operation'
    _description = 'Hospital Operation'

    patient_id = fields.Many2one(comodel_name="hospital.patient", string="Patient", )
    gender = fields.Selection([
        ('others', 'Others'),
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', default='others')
    booking_date = fields.Date(string='Booking Date')
    operation_date = fields.Date(string="Operation Date")
    doctor_id = fields.Many2one(comodel_name="res.users", string="Doctor")
    reference_record = fields.Reference(
        selection=[('hospital.patient', 'Patient'),
                   ('hospital.appointment', 'Appointment')],
        string='Record'
    )

    # Selection Field for Different Operations
    operation_type = fields.Selection([
        ('surgery', 'Surgery'),
        ('diagnosis', 'Diagnosis'),
        ('therapy', 'Therapy'),
        ('consultation', 'Consultation'),
        ('emergency', 'Emergency'),
        ('other', 'Other')
    ], string="Operation Type", required=True, default="consultation")
