# -*- coding: utf-8 -*-
import logging

from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.http import request
from odoo import _


_logger = logging.getLogger(__name__)


class AuthSignupHome(AuthSignupHome):
    def get_auth_signup_qcontext(self):
        """Add recaptcha to the context"""
        qcontext = super(AuthSignupHome, self).get_auth_signup_qcontext()
        if request.params.get("g-recaptcha-response"):
            qcontext["g-recaptcha-response"] = request.params.get(
                "g-recaptcha-response"
            )
        return qcontext

    def do_signup(self, qcontext):
        """Validate the captcha before signup"""
        ## Check if g-recaptcha-response is in the context
        _logger.debug("qcontext: %s", qcontext.get("g-recaptcha-response"))

        if "g-recaptcha-response" not in qcontext:
            _logger.debug("No captcha in context")

            # FIXME The qcontext error message is not displayed
            qcontext["error"] = _("the captcha has not been validated")
            raise SignupError(_("the captcha has not been validated"))

        # Validate the captcha
        if not request.env["portal.mixin"].is_captcha_valid(
            qcontext.get("g-recaptcha-response")
        ):
            qcontext["error"] = _("the captcha is not valid")
            raise SignupError(_("the captcha is not valid"))

        # If the captcha is valid, call the parent method
        super(AuthSignupHome, self).do_signup(qcontext)
