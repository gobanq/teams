# -*- coding: utf-8 -*-
from odoo import http

# class Team(http.Controller):
#     @http.route('/team/team/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/team/team/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('team.listing', {
#             'root': '/team/team',
#             'objects': http.request.env['team.team'].search([]),
#         })

#     @http.route('/team/team/objects/<model("team.team"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('team.object', {
#             'object': obj
#         })