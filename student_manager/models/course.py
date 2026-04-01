from odoo import models, fields, api

class Course(models.Model):
    _name = 'student.course'
    _description = 'Course'

    name = fields.Char(string="Course Name", required=True)

    enrollment_ids = fields.One2many(
        'student.enrollment',
        'course_id',
        string="Enrollments"
    )

    total_enrollments = fields.Integer(
        string="Total Enrollments",
        compute="_compute_total_enrollments",
        store=True
    )

    @api.depends('enrollment_ids')
    def _compute_total_enrollments(self):
        for record in self:
            record.total_enrollments = len(record.enrollment_ids)