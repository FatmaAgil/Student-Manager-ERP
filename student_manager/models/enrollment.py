from odoo import models, fields, api

class Enrollment(models.Model):
    _name = 'student.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('student.student', string="Student")
    course_id = fields.Many2one('student.course', string="Course")
    date = fields.Date(string="Enrollment Date")
    grade = fields.Float(string="Grade")

    status = fields.Selection(
        [('passed', 'Passed'), ('failed', 'Failed')],
        compute="_compute_status",
        store=True
    )

    @api.depends('grade')
    def _compute_status(self):
        for record in self:
            record.status = 'passed' if record.grade >= 50 else 'failed'

    # 🔥 AUTOMATION
    @api.model
    def create(self, vals):
        record = super().create(vals)

        print("✅ Enrollment created for student:", record.student_id.name)

        return record