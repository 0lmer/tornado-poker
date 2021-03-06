# -*- coding: utf-8 -*-


import os.path

from tornado.options import define


define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

settings = {}

settings["project_name"] = 'chat'

settings["debug"] = True
settings["cookie_secret"] = "askdfjpo83q47r9haskldfjh8"
settings["login_url"] = "/login"
settings["root_path"] = os.path.dirname(__file__)
settings["static_path"] = os.path.join(settings['root_path'], "static")
# settings["template_path"] = settings['root_path']  # os.path.join(settings['root_path'], "templates")
settings["xsrf_cookies"] = False

settings["apps"] = [
    'core',
    'chatapp',
    'pokerapp',
]

settings["mongo_db_name"] = settings["project_name"]
settings["mongo_host"] = "127.0.0.1"
settings["mongo_port"] = 27017