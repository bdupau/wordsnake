import logging, os, uuid
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.web

from tornado.concurrent import Future
from tornado import gen
from messagebuffer import MessageBuffer

global_message_buffer = MessageBuffer()

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MessageNewHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        message = {
            "id": str(uuid.uuid4()),
            "from": tornado.escape.to_basestring(self.current_user),
            "body": self.get_argument("body"),
        }

        message["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=message))

        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)

        global_message_buffer.new_messages([message])

class MessageUpdatesHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def post(self):
        cursor = self.get_argument("cursor", None)
        # Save the future returned by wait_for_messages so we can cancel
        # it in wait_for_messages
        self.future = global_message_buffer.wait_for_messages(cursor=cursor)
        messages = yield self.future
        if self.request.connection.stream.closed():
            return
        self.write(dict(messages=messages))

    def on_connection_close(self):
        global_message_buffer.cancel_wait(self.future)


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = tornado.escape.xhtml_escape(self.current_user)
        self.render(
            "index.html", 
            messages = global_message_buffer.cache, 
            username = username
        )

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.write("You are now logged out")
