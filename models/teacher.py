# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'teacher.teacher'
    _description = 'Teachers'

    name = fields.Char(string="Teacher Name")
    code = fields.Char(string="Teacher code")
    biography = fields.Text(string="Teacher Biography")
    course_ids = fields.One2many(comodel_name='product.template', inverse_name='teacher_id', string="Courses",
                                           domain=lambda self: [('public_categ_ids', 'in', self.env.ref('my_website.category_courses').id)])


