# Wordsnake over http

Als je wordsnake wilt spelen via de browser dan zal je berichten van spelers moeten kunnen ontvangen en ook weer berichten terug moeten kunnen sturen met bijvoorbeeld updates over de gamestate. 

Typisch van standaard http verkeer is dat het initiatief bij de client ligt. In het geval van een website stuurt de gebruiker typisch een http request en de server antwoordt met de response in de vorm van een html pagina.

Wat bij wordsnake afwijkt van die request / response patroon is dat er in het spel soms gegevens gestuurd moeten worden op initiatief van de server. Bijvoorbeeld: een speler geeft een nieuw woord. Aan de server kant wordt het woord volgens de spelregels verwerkt. Nu moet er een bericht naar alle deelnemers met deze update. 

Van origine is het http protocol hier niet op berust. Een typische truuk is om elke client telkens (bijv. per seconde) een request naar de server te laten sturen met als verzoek de spelstatus. Deze techniek heet 'polling'

Een alternatief voor dit 'pollen' is het gebruik van een socket. In dit geval stuurt de client een verzoek met een callback adres waarop de client boodschappen van de server zal ontvangen. 

Er zijn verschillende technieken die vergelijkbaar zijn met sockets. Er zijn ook frameworks die afhankelijk van de technische mogelijkheden van de client de juiste techniek kiezen en hierbovenop een uniforme API bieden. [Socket.IO](http://socket.io/) is een voorbeeld wat ik heb leren kennen via [NodeJS](http://nodejs.org/). NodeJS is een server die je programmeert in javascript. Voor onze spelengine gaan we python gebruiken.

De vraag is nu of er voor python ook een equivalent van Socket.IO is, of dat we een 1-2-tje moeten opzetten tussen een NodeJS server en een Python service die als game engine werkt.


## Op zoek naar socket implementaties voor Python

Googlen op 'python websockets' gaf o.a. de volgende resultaten:

- [Websockets 2.3](https://pypi.python.org/pypi/websockets)
- [Autobahn](http://autobahn.ws/python/)
- [tornado.websocket](http://www.tornadoweb.org/en/branch2.1/websocket.html)

Mijn eerste inschatting is dat het niet nodig zal zijn om NodeJS als tussenstation te gebruiken.

