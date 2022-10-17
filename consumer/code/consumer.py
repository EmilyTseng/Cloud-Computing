from traceback import print_tb
from unittest import result
from flask import Flask
import random
import json
import requests
app = Flask(__name__)

@app.route('/consumer')
def hello_world():
   # result = requests.get('index').content
   # print(result)


   resp = requests.get('http://api:5000/api').content
   data = json.loads(resp)
   key = ''
   valu = ''

   for itemK, itemV in data.items():
      key = itemK
      value = itemV

   print(resp)


   html_template = f'''
    <!DOCTYPE html>
      <html>
      <body>

      <h1>Food: Price</h1>

      <p>{key}: {value}</p>

      </body>
      </html>
   '''

   return html_template


@app.route('/index')
def index():
   return "index"

if __name__ == '__main__':
   # app.run(host="localhost", port=5001, debug=True)
    app.run(host="0.0.0.0", port=80, debug=True)