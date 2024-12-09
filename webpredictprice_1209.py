import urllib.request
import json
import os
import ssl
from dotenv import load_dotenv
load_dotenv()

def allowSelfSignedHttps(allowed):  
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
# data = {}
data = {
  "Inputs": {
    "WebServiceInput0": [
      {
        "symboling": 3,
        "normalized-losses": 122,
        "city-mpg": 25,
        "height": 50,
        "highway-mpg": 30,
        "aspiration": "std",
        "fuel-type": "gas",
        "body-style": "sedan",
        "engine-type": "dohc",
        "drive-wheels": "rwd",
        "compression-ratio": 9.0,
        "width": 65.5,
        "horsepower": 130,
        "length": 180,
        "engine-location": "front",
        "price": 5000,
        "num-of-cylinders": "four",
        "curb-weight": 2200,
        "engine-size": 140,
        "bore": 3.4,
        "stroke": 3.4,
        "make": "toyota",
        "num-of-doors": "four",
        "wheel-base": 100,
        "peak-rpm": 5000,
        "fuel-system": "mpfi"
      }
    ]
  }
}


body = str.encode(json.dumps(data))

url = 'http://c44be83a-acd0-4334-adaa-0dfdbb8aeff0.japaneast.azurecontainer.io/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = os.getenv("1209predict_key")
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
    