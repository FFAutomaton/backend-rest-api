from flask import Flask
from flask_restful import Api
from turk_gecko_rest_api.endpoints.index import Index
from turk_gecko_rest_api.endpoints.dataref import DataRef
from turk_gecko_rest_api.endpoints.dataprocess import DataProcess
from turk_gecko_rest_api.endpoints.orderinfo import OrderInfo
import datetime
import os
from flask import render_template
from flask import Flask
# from turkgeckorestapi.config import init_config


app = Flask(__name__)
# init_config(app)
api = Api(app)

# print(app.config)
api.add_resource(Index, '/')
api.add_resource(DataRef, '/dataref')
api.add_resource(DataProcess, '/dataprocess')
api.add_resource(OrderInfo, '/orderinfo')

