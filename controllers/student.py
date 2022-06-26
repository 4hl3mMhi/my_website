# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyWebsite(http.Controller):

    # 4. routing string: Model Converter
    @http.route(['/mywebsite/students'], auth="public", website=True)
    def teacher_biography(self, **kw):
        """ Here the module 'my_website' depends on 'website' stander module,
            you can note that through the param 'website=True' passed in 'route()' decorator.

        :param student: object.
        """
        Student = request.env['student.student']
        return request.render('my_website.student_display', {'students': Student.search([])})
