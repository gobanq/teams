# -*- coding: utf-8 -*-
import base64
from odoo import models, fields, api
from odoo import tools

from odoo.modules.module import get_module_resource

class Player(models.Model):
    _name = 'team.player'
    _description = 'Player'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('team', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))

    name = fields.Char(string="Player Name", required=True)
    contact = fields.Char(string="Contact Number")
    address = fields.Text(string="Address")
    image = fields.Binary(string="Profile Picture", default=_default_image, attachment=True,
        help="This field holds the image used as photo for the player, limited to 1024x1024px.")
    image_medium = fields.Binary(
    "Medium-sized photo", attachment=True,
    help="Medium-sized photo of the player. It is automatically "
         "resized as a 128x128px image, with aspect ratio preserved. "
         "Use this field in form views or some kanban views.")
    image_small = fields.Binary(
        "Small-sized photo", attachment=True,
        help="Small-sized photo of the player. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")
    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(Player, self).create(vals)

    @api.multi
    def write(self, vals):
         tools.image_resize_images(vals)
         return super(Player, self).write(vals)

class Team(models.Model):
    _name = 'team.team'
    _description = 'Team'

    name = fields.Char(string="Team Name")
    address = fields.Text(string="Address")
    logo = fields.Binary(string="Logo")
    description = fields.Text(string="Description")
    player_line = fields.One2many('team.team_player', 'team_id', string="Player")
    coach_line = fields.One2many('team.team_coach', 'team_id', string="Coach")

class Coach(models.Model):
    _name = 'team.coach'
    _description = 'Coach'

    name = fields.Char(string="Coach Name", required=True)
    contact = fields.Char(string="Contact Number")
    address = fields.Text(string="Address")
    picture = fields.Binary(string="Profile Picture")

class TeamPlayer(models.Model):
    _name = 'team.team_player'
    _description = 'Team Player'

    team_id = fields.Many2one('team.coach', string="Team")
    player_id = fields.Many2one('team.player', string="Player", required=True)
    date_in = fields.Date(string="Date In")
    date_out = fields.Date(string="Date Out")
    position = fields.Char(string="Position")
    number = fields.Integer(string="Number")

class TeamCoach(models.Model):
    _name = 'team.team_coach'
    _description = 'Team Coach'

    team_id = fields.Many2one('team.coach', string="Team")
    coach_id = fields.Many2one('team.coach', string="Coach")
    date_in = fields.Date(string="Date In")
    date_out = fields.Date(string="Date Out")
