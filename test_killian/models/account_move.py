from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    test_killian = fields.Boolean()
