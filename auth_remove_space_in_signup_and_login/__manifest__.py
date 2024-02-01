# Copyright  Élabore (2023)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "auth_remove_space_in_signup_and_login",
    "version": "12.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Boris Gallet",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "remove space around email in signup  and login in order to prevent failure with login",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "auth_signup"
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}
