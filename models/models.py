# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Player(models.Model):
    _name = 'team.player'
    _description = 'Player'

    name = fields.Char(string="Player Name", required=True)
    contact = fields.Char(string="Contact Number")
    address = fields.Text(string="Address")
    picture = fields.Binary(string="Profile Picture")

class Team(models.Model):
    _name = 'team.team'
    _description = 'Team'

    name = fields.Char(string="Team Name")
    address = fields.Text(string="Address")
    logo = fields.Binary(string="Logo")
    description = fields.Text(string="Description")

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
    player_id = fields.Many2one('team.player', string="Player")
    date_in = fields.Date(string="Date In")
    date_out = fields.Date(string="Date Out")

class TeamCoach(models.Model):
    _name = 'team.team_coach'
    _description = 'Team Coach'

    team_id = fields.Many2one('team.coach', string="Team")
    coach_id = fields.Many2one('team.coach', string="Coach")
    date_in = fields.Date(string="Date In")
    date_out = fields.Date(string="Date Out")
