from odoo import models, fields

class Course(models.Model):
    _name = 'student.course'
    _description = 'Course'

    name = fields.Char(string="Course Name", required=True)
    credits = fields.Integer(string="Credits")


    enrollment_ids = fields.One2many(
        'student.enrollment',
        'course_id',
        string="Enrollments"
    )