import telepathy

from .protocol import HangupsProtocol
from .text_channel import HangupsTextChannel

class HangupsConnectionManager(telepathy.server.ConnectionManager):
    def __init__(self):
        telepathy.server.ConnectionManager.__init__(self, 'hangups')
        self._implement_protocol('hangouts', HangupsProtocol) #protocol is still hangouts, _NOT_ hangups