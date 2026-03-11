from odoo import models, fields

class Enrollment(models.Model):
    _name = 'student.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one(
        'student.student',
        string="Student",
        required=True
    )

    course_id = fields.Many2one(
        'student.course',
        string="Course",
        required=True
    )

    date = fields.Date(string="Enrollment Date")
    grade = fields.Float(string="Grade")