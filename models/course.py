# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _inherit = 'product.template'
    _description = 'Courses'

    name = fields.Char(string="Course Name")
    teacher_id = fields.Many2one(comodel_name='teacher.teacher', string="Teacher")
