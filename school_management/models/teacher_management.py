from odoo import fields, models


class TeacherManagement(models.Model):
    _name = "teacher.management"
    _description = "Teacher Management"
    _rec_name = "teacher_name"
    _order = "standard asc"  # help for maintain the sequences of standard

    teacher_name = fields.Char(string="Teacher Name")
    division = fields.Char(string='Division')
    standard = fields.Integer(string="Standard")
