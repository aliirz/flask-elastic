# sparrow_flask/app.py
from flask import Flask
from flask_restful import Api

# settings to load env vars and other bootstrap stuff
import settings

from Resources.AppMetric import *
from Resources.InfraMetric import *
import os


# init the API
app = Flask(__name__)
api = Api(app)


# connect to ES instance
# es = Redis(host='es01', port=6379)


api.add_resource(AppMetric, '/appmetric')
api.add_resource(InfraMetric, '/inframetric')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
