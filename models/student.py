# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.student'
    _description = 'Students'

    name = fields.Char(string="Student Name")
    code = fields.Char(string="Student code")
    biography = fields.Html(string="Student Biography")
