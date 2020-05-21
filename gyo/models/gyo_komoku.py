# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gyo_komoku(models.Model):
    _name = 'gyo.gyo_komoku'
    _description = 'gyo.gyo_komoku'

    gyo_komoku_cd = fields.Char(string='業務番号')
    gyo_komoku_nm = fields.Char(string='業務名')