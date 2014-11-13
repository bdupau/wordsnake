# Wordsnake over http

Als je wordsnake wilt spelen via de browser dan zal je berichten van spelers
moeten kunnen ontvangen. Bijvoorbeeld, een speler (client) die aan de beurt is
geeft een nieuw woord door wat wordt ontvangen door de server. Je moet ook
berichten kunnen verzenden naar de spelers. Bijvoorbeeld wanneer een nieuw
woord is doorgegeven, dan stuur je vanaf de server een update over de
gamestate naar de spelers (clients).

Bij http verkeer ligt van oudsher het initiatief bij de client. Bijvoorbeeld:
in het geval van een website stuurt de gebruiker een http request en de server
antwoordt met een http response die een html pagina bevat.

Wat bij wordsnake afwijkt van dit patroon is dat er in het spel soms gegevens
gestuurd moeten worden op initiatief van de server. Wanneer de gamestate
verandert wil je een bericht aan alle clients doorgeven.

Een typische workaround om berichtgeving van de serverkant mogelijk te maken
is 'polling'. De clients sturen herhaaldelijk een request naar de server voor
een update van de spelstatus.

> En heb je nog nieuws?

> En heb je nog nieuws?

> En heb je nog nieuws?

> En heb je nog nieuws?

> En heb je nog nieuws?

Een alternatief voor dit 'pollen' is het gebruik van een socket. In dit geval
stuurt de client een verzoek met een callback adres waarop de client
boodschappen van de server zal ontvangen.

> Als je nieuws hebt dan bel maar even op dit nummer

Op het spectrum tussen polling en het gebruik van sockets liggen nog een
aantal technieken die hetzelfde doel voor ogen hebben. Om voor elke client de
best mogelijke techniek aan te wenden zijn er speciale frameworks. Deze kiezen
naargelang de technische mogelijkheden van de client de optimale techniek en
bieden de programmeur een uniforme interface. [Socket.IO](http://socket.io/)
is een voorbeeld wat ik heb leren kennen via [NodeJS](http://nodejs.org/).
NodeJS is een server die je programmeert in javascript. Voor onze spelengine
gaan we python gebruiken.

De vraag is nu of er voor python ook een equivalent van Socket.IO is, of dat
we een 1-2-tje moeten opzetten tussen een NodeJS server en een Python service
die als game engine werkt.


## Op zoek naar socket implementaties voor Python

Googlen op 'python websockets' gaf o.a. de volgende resultaten:

- [Websockets 2.3](https://pypi.python.org/pypi/websockets)
- [Autobahn](http://autobahn.ws/python/)
- [tornado.websocket](http://www.tornadoweb.org/en/branch2.1/websocket.html)

Mijn eerste inschatting is dat het niet nodig zal zijn om NodeJS als
tussenstation te gebruiken.


## Voorbeeld implementatie chatroom met tornado framework

Ik kwam de volgende voorbeeld implementatie tegen van een chatroom waarbij
gebruik gemaakt is van het [tornado](http://www.tornadoweb.org/en/stable/)
framework:

[tornado demo: chatroom](https://github.com/tornadoweb/tornado/tree/stable/demos/chat)

Zonder de andere opties bekeken te hebben lijkt dit al een prima uitgangspunt
voor onze server implementatie. Het framework handelt op elegante wijze in een
kort script diverse server taken af.

- __Configuratie en request routing__:

    ````py
    def main():
        parse_command_line()
        app = tornado.web.Application(
            [
                (r"/", MainHandler),
                (r"/auth/login", AuthLoginHandler),
                (r"/auth/logout", AuthLogoutHandler),
                (r"/a/message/new", MessageNewHandler),
                (r"/a/message/updates", MessageUpdatesHandler),
                ],
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            debug=options.debug,
            )
        app.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    ````

- __Authorisatie met [Open Id](http://openid.net/)__:

    ````py
    class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
        @gen.coroutine
        def get(self):
            if self.get_argument("openid.mode", None):
                user = yield self.get_authenticated_user()
                self.set_secure_cookie("chatdemo_user",
                                       tornado.escape.json_encode(user))
                self.redirect("/")
                return
            self.authenticate_redirect(ax_attrs=["name"])


    class AuthLogoutHandler(BaseHandler):
        def get(self):
            self.clear_cookie("chatdemo_user")
            self.write("You are now logged out")
    ````

