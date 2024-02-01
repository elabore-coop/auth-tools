# -*- coding: utf-8 -*-
import logging

from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request


class AuthSignupHome(AuthSignupHome):
    def get_auth_signup_qcontext(self):
        qcontext = super(AuthSignupHome, self).get_auth_signup_qcontext()
        if request.params.get("email"):
            qcontext["email"] = request.params.get("email").strip()
        if request.params.get("login"):
            qcontext["login"] = request.params.get("login").strip()
            
        return qcontext