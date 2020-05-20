# -*- coding: utf-8 -*-
# from odoo import http


# class Gyomu(http.Controller):
#     @http.route('/gyomu/gyomu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gyomu/gyomu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gyomu.listing', {
#             'root': '/gyomu/gyomu',
#             'objects': http.request.env['gyomu.gyomu'].search([]),
#         })

#     @http.route('/gyomu/gyomu/objects/<model("gyomu.gyomu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gyomu.object', {
#             'object': obj
#         })
