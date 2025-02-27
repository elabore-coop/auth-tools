from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome as Home
from odoo.http import request


class Home(Home):
    @http.route()
    def web_login(self, *args, **kw):
        if request.httprequest.method == "POST" and request.params.get("login"):
            request.params["login"] = request.params.get("login").strip()
        return super().web_login(*args, **kw)
