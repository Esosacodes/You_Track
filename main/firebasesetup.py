__author__ = 'mrs Ojoodide'

import pyrebase
config = {
  "apiKey": "AIzaSyDQB_RdFzfdFrezB4yVrkZS36U9GS0c71k",
  "authDomain": "you-track-f7ffb.firebaseapp.com",
  "databaseURL": "https://https://you-track-f7ffb.firebaseio.com/",
  "storageBucket": "you-track-f7ffb.appspot.com",
  "serviceAccount": "main\static\main\js\google-services.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()

def getFireBaseAut():
    return auth
