from flask import *
import json, time
import requests
from PIL import Image, ImageFont, ImageDraw, ImageOps
import textwrap
import requesttest

app = Flask(__name__)


#MainPage
@app.route('/', methods=['GET'])
def home_page():
    data_set ={'Page': 'Home', 'Message': 'Successfully loaded', 'Timestamp':time.time()}
    json_dumb = json.dumps(data_set)

    return json_dumb

#TestRequest
@app.route('/githubUser/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user')) #/Test/?user=
    print(user_query)
    
    return send_file(requesttest.getUserImage(user_query), mimetype='image/gif')



if __name__ == '__main__':
    app.run(host="localhost", port=200820, debug=True)
