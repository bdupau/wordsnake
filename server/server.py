#!/usr/bin/env python

# Initiele implementatie voor game server gebaseerd op chatserver
# 
# *beter goed gejat dan slecht zelf gedaan*

import logging, os, uuid
import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line
from handlers import *

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
            (r"/a/message/new", MessageNewHandler),
            (r"/a/message/updates", MessageUpdatesHandler)
        ],
        cookie_secret="__WIE_HET_GROTE_NIET_EERT_is_het_kleine_niet_weerd__",
        login_url="/login",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug
    )

    app.listen(options.port)
    print("Server listening on port " + str(options.port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
