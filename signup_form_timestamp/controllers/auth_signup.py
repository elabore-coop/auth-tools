from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
import uuid
from datetime import datetime

class AuthSignupTimestamp(AuthSignupHome):

    MIN_SIGNUP_DELAY = 5
    MAX_SIGNUP_DELAY = 3600
    
    def _get_field_timestamp_name(self):
        """ Génère dynamiquement le nom du champ timestamp """
        return str(uuid.uuid4()).replace('-', '')

    @http.route(['/web/signup'], type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        """ Surcharge de la méthode pour inclure le champ timestamp dynamique """
        timestamp_name = request.session.get('timestamp_name','')
        if timestamp_name == '':
            timestamp_name = self._get_field_timestamp_name()
            request.session['timestamp_name'] = timestamp_name

        # Générer un timestamp actuel
        signup_timestamp = request.session.get('signup_timestamp','')
        if signup_timestamp == '':
            signup_timestamp = int(datetime.now().timestamp())
            request.session['signup_timestamp'] = signup_timestamp
        
        response = super(AuthSignupTimestamp, self).web_auth_signup(*args, **kw)
        response.qcontext['signup_timestamp'] = signup_timestamp
        response.qcontext['timestamp_name'] = timestamp_name

        return response

    def do_signup(self, qcontext):
        """ Vérifie le timestamp avant de créer le compte """
        timestamp_name = request.session.get('timestamp_name', '')
        signup_timestamp = request.params.get(timestamp_name,'')
        if not signup_timestamp:
            return http.local_redirect('/web/login', keep_hash=True)

        try:
            # Convertir en entier
            signup_timestamp = int(signup_timestamp)
            current_timestamp = int(datetime.now().timestamp())
            elapsed_time = current_timestamp - signup_timestamp

            # Vérifier si le délai est acceptable
            if elapsed_time < self.MIN_SIGNUP_DELAY or elapsed_time > self.MAX_SIGNUP_DELAY:
                return http.local_redirect('/web/login', keep_hash=True)

        except ValueError:
            # Si le timestamp n'est pas valide
            return http.local_redirect('/web/login', keep_hash=True)

        # Si le champ n'est pas rempli, continuer avec l'inscription normale
        super(AuthSignupTimestamp, self).do_signup(qcontext)

