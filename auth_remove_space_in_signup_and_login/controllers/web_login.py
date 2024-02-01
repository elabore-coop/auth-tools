# -*- coding: utf-8 -*-
import logging

from odoo.addons.web.controllers.main import Home
from odoo import http
from odoo.http import request

class Home(Home):
    @http.route('/web/login', type='http', auth="none", sitemap=False)
    def web_login(self, *args, **kw):
        if request.httprequest.method == 'POST':
            if request.params.get("login"):
                request.params["login"] = request.params.get("login").strip()
        return super(Home, self).web_login(*args, **kw)