import logging
from spyne import Application, rpc, ServiceBase, \
    String, Long
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.complex import ComplexModel, Array

logging.basicConfig(level="WARNING")

class event(ComplexModel):
    eid = String
    eventMessage = String
    eventSeverity = String
    eventTime = Long
    eventTypeName = String
    meterId = String

class eventQueryResult(ComplexModel):
    queryId = String
    queryStatus = String
    events = Array(event)

class someResponse(ComplexModel):
    eventIds = Array(String)

class EventPushService(ServiceBase):
    @rpc(eventQueryResult, _body_style='bare', _returns=someResponse)
    def receiveEvents(ctx, req):
        print(req)

        return someResponse(eventIds = [ i.eid for i in req.events ] )

application = Application([EventPushService],
    tns='http://pushevent.nbapi.cgms.cisco.com/',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.

    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()

