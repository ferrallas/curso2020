# -*- coding: utf-8 -*-
# Copyright 2020 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions, _

class AccountDocumentTemplate(models.Model):
    _name = 'account.document.template'
    _inherit = 'name.module.inherited'

    name = fields.Char(required=True)
