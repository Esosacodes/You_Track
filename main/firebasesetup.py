__author__ = 'mrs Ojoodide'

import pyrebase
config = {
    "apiKey": "AIzaSyDQB_RdFzfdFrezB4yVrkZS36U9GS0c71k",
    "authDomain": "you-track-f7ffb.firebaseapp.com",
    "databaseURL": "https://you-track-f7ffb.firebaseio.com",
    "projectId": "you-track-f7ffb",
    "storageBucket": "you-track-f7ffb.appspot.com",
    "messagingSenderId": "662108324290",
     "serviceAccount": "/Users/danijax/Documents/projects/Dara/You_Track/main/you-track-f7ffb-firebase-adminsdk-1nrc3-978f50d3e8.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()

