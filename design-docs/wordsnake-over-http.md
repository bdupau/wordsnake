# Wordsnake over http

Als je wordsnake wilt spelen via de browser dan zal je berichten van spelers moeten kunnen ontvangen. Bijvoorbeeld, een speler (client) die aan de beurt is geeft een nieuw woord door wat wordt ontvangen door de server. Je moet ook berichten kunnen verzenden naar de spelers. Bijvoorbeeld wanneer een nieuw woord is doorgegeven, dan stuur je vanaf de server een update over de gamestate naar de spelers (clients).

Bij http verkeer ligt van oudsher het initiatief bij de client. Bijvoorbeeld: in het geval van een website stuurt de gebruiker een http request en de server antwoordt met een http response die een html pagina bevat.

Wat bij wordsnake afwijkt van dit patroon is dat er in het spel soms gegevens gestuurd moeten worden op initiatief van de server. Wanneer de gamestate verandert wil je een bericht aan alle clients doorgeven. 

Een typische workaround om berichtgeving van de serverkant mogelijk te maken is 'polling'. De clients sturen herhaaldelijk een request naar de server voor een update van de spelstatus. 

> En heb je nog nieuws?
> En heb je nog nieuws?
> En heb je nog nieuws?
> En heb je nog nieuws?
> En heb je nog nieuws?

Een alternatief voor dit 'pollen' is het gebruik van een socket. In dit geval stuurt de client een verzoek met een callback adres waarop de client boodschappen van de server zal ontvangen. 

> Als je nieuws hebt dan bel maar even op dit nummer

Op het spectrum tussen polling en het gebruik van sockets liggen nog een aantal technieken die hetzelfde doel voor ogen hebben. Om voor elke client de best mogelijke techniek aan te wenden zijn er speciale frameworks. Deze kiezen naargelang de technische mogelijkheden van de client de optimale techniek en bieden de programmeur een uniforme interface. [Socket.IO](http://socket.io/) is een voorbeeld wat ik heb leren kennen via [NodeJS](http://nodejs.org/). NodeJS is een server die je programmeert in javascript. Voor onze spelengine gaan we python gebruiken.

De vraag is nu of er voor python ook een equivalent van Socket.IO is, of dat we een 1-2-tje moeten opzetten tussen een NodeJS server en een Python service die als game engine werkt.


## Op zoek naar socket implementaties voor Python

Googlen op 'python websockets' gaf o.a. de volgende resultaten:

- [Websockets 2.3](https://pypi.python.org/pypi/websockets)
- [Autobahn](http://autobahn.ws/python/)
- [tornado.websocket](http://www.tornadoweb.org/en/branch2.1/websocket.html)

Mijn eerste inschatting is dat het niet nodig zal zijn om NodeJS als tussenstation te gebruiken.

