from odoo import models, fields, api

class Enrollment(models.Model):
    _name = 'student.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('student.student', string="Student")
    course_id = fields.Many2one('student.course', string="Course")
    date = fields.Date(string="Enrollment Date")
    grade = fields.Float(string="Grade")

    status = fields.Selection(
        [
            ('passed', 'Passed'),
            ('failed', 'Failed')
        ],
        string="Status",
        compute="_compute_status",
        store=True
    )

    @api.depends('grade')
    def _compute_status(self):
        for record in self:
            if record.grade >= 50:
                record.status = 'passed'
            else:
                record.status = 'failed'