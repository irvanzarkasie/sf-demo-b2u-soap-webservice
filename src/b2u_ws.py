import logging
from spyne import Application, rpc, ServiceBase, String, Long
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.complex import ComplexModel, Array

logging.basicConfig(level="INFO")

DEP_CODE_LIST = [
    "MY-Z1001",
    "MY-Z1002",
    "SG-S1001",
    "SG-S1002"
]

DEST_CODE_LIST = [
    "MY-Z1001",
    "MY-Z1002",
    "SG-S1001",
    "SG-S1002"
]

class routeModel(ComplexModel):
    departureCode = String
    destinationCode = String
# end class

class getRoutes(ComplexModel):
    departureCode = String
    destinationCode = String
# end class

class getRoutesResponse(ComplexModel):
    routes = Array(routeModel)
# end class

class GetRoutesService(ServiceBase):
    @rpc(getRoutes, _body_style='bare', _returns=getRoutesResponse)
    def getRoutes(ctx, req):
        print(req)
        return getRoutesResponse(routes = [])
    # end def
# end class

application = Application([GetRoutesService],
    tns='http://www.example.org/Bookings/',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.

    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 38000, wsgi_app)
    server.serve_forever()
# end if

