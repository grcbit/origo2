# -*- coding: utf-8 -*-
# from odoo import http


# class Origo(http.Controller):
#     @http.route('/origo/origo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/origo/origo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('origo.listing', {
#             'root': '/origo/origo',
#             'objects': http.request.env['origo.origo'].search([]),
#         })

#     @http.route('/origo/origo/objects/<model("origo.origo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('origo.object', {
#             'object': obj
#         })
