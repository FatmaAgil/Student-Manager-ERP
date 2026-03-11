from odoo import models, fields, api

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")

    enrollment_ids = fields.One2many(
        'student.enrollment',
        'student_id',
        string="Enrollments"
    )

    total_courses = fields.Integer(
        string="Total Courses",
        compute="_compute_total_courses",
        store=True
    )

    average_grade = fields.Float(
        string="Average Grade",
        compute="_compute_average_grade",
        store=True
    )

    @api.depends('enrollment_ids')
    def _compute_total_courses(self):
        for record in self:
            record.total_courses = len(record.enrollment_ids)

    @api.depends('enrollment_ids.grade')
    def _compute_average_grade(self):
        for record in self:
            grades = record.enrollment_ids.mapped('grade')
            if grades:
                record.average_grade = sum(grades) / len(grades)
            else:
                record.average_grade = 0