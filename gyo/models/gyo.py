# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gyo(models.Model):
    _name = 'gyo.gyo'
    _description = 'gyo.gyo'

    gyo_cd = fields.Char(string="業務番号")
    gyo_nm = fields.Char(string="業務名")
    gyo_komoku_cd = fields.One2many('gyo_komoku.gyo_komoku','gyo_komoku_cd')