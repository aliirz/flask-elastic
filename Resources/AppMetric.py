from flask import request
from flask_restful import Resource
from elasticsearch import Elasticsearch
from datetime import datetime
import os


# create elasticsearch object
es = Elasticsearch(host=os.getenv('ES_HOST'), port=os.getenv('ES_PORT'))


class AppMetric(Resource):
  """Get Infra Metrics based on some query"""
  def get(self):
    return 'WIP'

  def post(self):
    try:
      payload = request.get_json(force=True)
      # timestamp our payload
      payload['created_on'] = datetime.now()
      res = es.index(index='app', doc_type='_doc', body=payload)
      return res
    except Exception as e:
      print (e)
      return e
