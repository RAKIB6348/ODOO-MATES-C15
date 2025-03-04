from odoo import api, fields, models


class PatientTags(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tags'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string='Color')
    sequence = fields.Integer(string='Sequence')

    _sql_constraints = [
        ('unique_tag_name', 'unique (name)', 'The tag name must be unique !'),
        ('check_sequence', 'check(sequence > 0)', 'The sequence must be greater than 0!')
    ]