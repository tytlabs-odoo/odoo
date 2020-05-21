# -*- coding: utf-8 -*-
# from odoo import http


# class Gyo(http.Controller):
#     @http.route('/gyo/gyo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gyo/gyo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gyo.listing', {
#             'root': '/gyo/gyo',
#             'objects': http.request.env['gyo.gyo'].search([]),
#         })

#     @http.route('/gyo/gyo/objects/<model("gyo.gyo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gyo.object', {
#             'object': obj
#         })
