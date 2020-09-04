#    sizzlews
#    Copyright (C) 2020 Dmitry Berezovsky
#    The MIT License (MIT)
#    
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import asyncio

import websockets

from sizzlews.server.annotation import rpc_method
from sizzlews.server.common import ClassBasedSizzleWSHandler, SizzleWSHandler, MethodDiscoveryMixin
from sizzlews.server.websockets import WebsocketsSizzleWSHandler, bootstrap_websockets_rpc_application


class MyApi(MethodDiscoveryMixin, SizzleWSHandler):
    METHOD_PREFXIX = "api."

    @rpc_method
    def some_method(self, a: int, b):
        return a + b


if __name__ == "__main__":
    bootstrap_websockets_rpc_application(MyApi(), 5555, '/wsrpc')
    asyncio.get_event_loop().run_forever()