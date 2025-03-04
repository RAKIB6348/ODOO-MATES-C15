{
    'name': 'Hospital Management',
    'version': '1.1.1',
    'summary': 'odoo15 tutorials by odoo mates',
    'description': 'odoo15 tutorials by odoo mates',
    'depends': ['mail', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',

        'data/patient_tag_load_data.xml',
        'data/patient.tag.csv',
        'data/patient_sequence.xml',
        'data/appointment_sequence.xml',

        'wizard/cancel_appointment_wiz.xml',

        'views/menu_items.xml',
        'views/patient_view.xml',
        'views/female_patient.xml',
        'views/appointment_view.xml',
        'views/patient_tag.xml',
        'views/operation_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
