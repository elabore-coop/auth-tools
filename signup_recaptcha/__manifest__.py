# Copyright 2024 Boris Gallet ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "signup_recaptcha",
    "version": "12.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Boris Gallet",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "google recaptcha V2 for signup form with server side validation",
    # any module necessary for this one to work correctly
    "depends": ["base", "portal", "auth_remove_space_in_signup_and_login"],
    "data": [
        "views/auth_signup.xml",
        "views/res_config.xml",
    ],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}
