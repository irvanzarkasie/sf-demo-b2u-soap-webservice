import sys
import json
from flask import Flask, request, jsonify, make_response, Response
import pprint
import logging
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
import uuid
import socket
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# CONSTANTS
api_host = socket.gethostname()
api_port = 38000
api_id = "b2u_mock_ws"

# Work directory setup
script_dir = os.path.dirname(os.path.realpath(__file__))
home_dir = "/".join(script_dir.split("/")[:-1])
log_dir = "{home_dir}/logs".format(home_dir=home_dir)

@app.route('/getRoutes', methods=['POST'])
def getRoutes():
  response_payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:book="http://www.example.org/Bookings/">
   <soapenv:Header/>
   <soapenv:Body>
      <book:getRoutesResponse>
         <!--Zero or more repetitions:-->
         <routes>
            <departureCode>MY-Z1001</departureCode>
            <destinationCode>MY-Z1002</destinationCode>
         </routes>
         <routes>
            <departureCode>MY-Z1001</departureCode>
            <destinationCode>SG-S1001</destinationCode>
         </routes>
         <routes>
            <departureCode>MY-Z1001</departureCode>
            <destinationCode>SG-S1002</destinationCode>
         </routes>
         <routes>
            <departureCode>MY-Z1002</departureCode>
            <destinationCode>MY-Z1001</destinationCode>
         </routes>
         <routes>
            <departureCode>MY-Z1002</departureCode>
            <destinationCode>SG-S1001</destinationCode>
         </routes>
         <routes>
            <departureCode>MY-Z1002</departureCode>
            <destinationCode>SG-S1002</destinationCode>
         </routes>
         <routes>
            <departureCode>SG-S1001</departureCode>
            <destinationCode>MY-Z1001</destinationCode>
         </routes>
         <routes>
            <departureCode>SG-S1001</departureCode>
            <destinationCode>MY-Z1002</destinationCode>
         </routes>
         <routes>
            <departureCode>SG-S1001</departureCode>
            <destinationCode>SG-S1002</destinationCode>
         </routes>
         <routes>
            <departureCode>SG-S1002</departureCode>
            <destinationCode>MY-Z1001</destinationCode>
         </routes>
         <routes>
            <departureCode>SG-S1002</departureCode>
            <destinationCode>MY-Z1002</destinationCode>
         </routes>
         <routes>
            <departureCode>SG-S1002</departureCode>
            <destinationCode>SG-S1001</destinationCode>
         </routes>
      </book:getRoutesResponse>
   </soapenv:Body>
</soapenv:Envelope>
  """
  response = Response(response=response_payload, status=200, mimetype='application/xml')
  response.headers['Content-Type'] = 'text/xml; charset=utf-8'
  return response
# end def

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=api_port)
# end if