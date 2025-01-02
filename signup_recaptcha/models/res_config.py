from odoo import fields, models


class PortalConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    recaptcha_key_site = fields.Char(
        config_parameter="signup_recaptcha.recaptcha_key_site"
    )
    recaptcha_key_secret = fields.Char(
        config_parameter="signup_recaptcha.recaptcha_key_secret"
    )
