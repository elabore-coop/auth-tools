from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
import uuid

class AuthSignupHoneypot(AuthSignupHome):

    def _get_honeypot_name(self):
        """ Génère dynamiquement le nom du champ honeypot """
        return str(uuid.uuid4()).replace('-', '')

    @http.route(['/web/signup'], type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        """ Surcharge de la méthode pour inclure le champ honeypot dynamique """
        honeypot_name = request.session.get('honeypot_name','')
        if honeypot_name == '':
            honeypot_name = self._get_honeypot_name()
            request.session['honeypot_name'] = honeypot_name
        response = super(AuthSignupHoneypot, self).web_auth_signup(*args, **kw)
        response.qcontext['honeypot_name'] = honeypot_name
        return response

    def do_signup(self, qcontext):
        """ Vérifie le champ honeypot avant de créer le compte """
        honeypot_name = request.session.get('honeypot_name', '')
        honeypot_field = request.params.get(honeypot_name, '')
        if honeypot_field:
            return http.local_redirect('/web/login', keep_hash=True)

        # Si le champ n'est pas rempli, continuer avec l'inscription normale
        super(AuthSignupHoneypot, self).do_signup(qcontext)

