# -*- coding: utf-8 -*-
# from odoo import http


# class GyoKomoku(http.Controller):
#     @http.route('/gyo_komoku/gyo_komoku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gyo_komoku/gyo_komoku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gyo_komoku.listing', {
#             'root': '/gyo_komoku/gyo_komoku',
#             'objects': http.request.env['gyo_komoku.gyo_komoku'].search([]),
#         })

#     @http.route('/gyo_komoku/gyo_komoku/objects/<model("gyo_komoku.gyo_komoku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gyo_komoku.object', {
#             'object': obj
#         })
