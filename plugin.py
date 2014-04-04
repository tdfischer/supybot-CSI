###
# Copyright (c) 2011-2014, Torrie Fischer
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class CSI(callbacks.Plugin):
    """Add the help for "@plugin help CSI" here
    This should describe *how* to use this plugin."""
    def __init__(self, irc):
        self.__parent = super(CSI, self)
        self.__parent.__init__(irc)
        self.delays = ircutils.IrcDict()
    
    def shades(self, irc, msg, args, channel):
        """[<channel>]

        You'll figure it out."""
        self.delays[channel] = 2
    shades = wrap(shades, ['channeldb'])

    def doPrivmsg(self, irc, msg):
        (recipients, text) = msg.args
        for channel in recipients.split(','):
            if irc.isChannel(channel):
                if channel in self.delays:
                    self.delays[channel] -= 1
                    if self.delays[channel] == 0:
                        irc.reply("YEAHHHHHHHH", prefixNick=False)


Class = CSI


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
