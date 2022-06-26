# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyWebsite(http.Controller):

    """ Controller methods are associated with routes via the route() decorator which takes a «routing string»
        and a number of attributes to customise its behavior or security.

        routing string: -->  1. «literal»: which matches a URL section exactly (see: route() decorator in methods:index_static(), index_fetch_data(), index_fetch__data().
                        \
                         ->  2. «converter patterns»^^ which match bits of URLs and make those available as local variables.

        «converter patterns»^^: routing strings are URL paths with placeholders for variable parts in the format <converter(arguments):name>.
                  |             converter() and arguments are optional.
                  |
                  --> 1. PathConverter:    route('/<path:wikipage>') or route('/<path:wikipage>/edit'), .....
                  --> 2. AnyConverter:     route('/<any(about, help, imprint, class, "foo,bar"):page_name>'), .....
                  --> 3. UnicodeConverter: route('/<string(length=2):name>'), .....
                  --> 4. IntegerConverter: route("/page/<int:page>") or route("/page/<int(signed=True):page>"), .....
                  --> 5. FloatConverter:   route("/probability/<float:probability>") or route("/offset/<float(signed=True):offset>"), .....
                  --> 6. Model Converter:  provided by Odoo which provides records directly when given their id:
                                            route('/academy/<model("academy.teachers"):teacher>/')
    """

    # 1. routing string: literal
    @http.route(['/mywebsite/index/1'], auth='public')
    def index_static(self, **kw):
        """ Displaying a list of string entered statically in python code. """
        vals = {'teachers': ["Diana Padilla", "Jody Carol", "Lester Vaughn"]}
        return request.render('my_website.index_page_1', vals)

    # 2. routing string: literal
    @http.route(['/mywebsite/index/4'], auth='public')
    def index_fetch_data(self, **kw):
        """ Fetch the records from database instead of having a static list.
            Here the module 'my_website' still not depending on 'website' stander module.
        """
        Teacher = request.env['teacher.teacher']
        return request.render('my_website.index_page_4', {'teachers': Teacher.search([])})

    # 3. routing string: literal
    @http.route(['/mywebsite/teachers'], auth="public", website=True)
    def display_teachers(self, **kw):
        """ Same as previous Controller. """
        Teacher = request.env['teacher.teacher']
        return request.render('my_website.teacher_display', {'teachers': Teacher.search([])})

    # 4. routing string: Model Converter
    @http.route(['/mywebsite/teacher_biography/<model("teacher.teacher"):teacher>/'], auth="public", website=True)
    def teacher_biography(self, teacher, **kw):
        """ Here the module 'my_website' depends on 'website' stander module,
            you can note that through the param 'website=True' passed in 'route()' decorator.

        :param teacher: object.
        """
        return request.render('my_website.teacher_biography', {'person': teacher})





#     @http.route('/my_website/my_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_website.listing', {
#             'root': '/my_website/my_website',
#             'objects': http.request.env['my_website.my_website'].search([]),
#         })

#     @http.route('/my_website/my_website/objects/<model("my_website.my_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_website.object', {
#             'object': obj
#         })
