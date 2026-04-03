{
    'name': 'Student Manager',
    'version': '1.0',
    'summary': 'Simple Student Management App',
    'author': 'Fatma',
    'category': 'Education',
    'depends': ['base'],
    'data': [
    'security/student_groups.xml',
    'security/ir.model.access.csv',
    'views/student_views.xml',
    'views/course_views.xml',
    'views/enrollment_views.xml',
    'data/cron.xml',
    ],
    'installable': True,
    'application': True,
}