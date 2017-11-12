import json

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from django.contrib import messages
from requests.exceptions import HTTPError

from .forms import UserForm
from .firebasesetup import auth, db
import logging

logger = logging.getLogger('you_track_logs')


form = UserForm

def index(request):
    # template = loader.get_template('main/profile.html')
    #  context = {'':''}
     return render(request, 'main/login.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'main/login.html'

    def get(self,request):
        pass

    def post(self,request):
        pass


def sign_in(request):
    # If the user has hit "login"
    print("Running", flush=True)
    if request.method == "POST":

        # Keep the user's username and power for verification
        username = request.POST['username']
        password = request.POST['password']
        print(username, " ", password, flush=True)
        # Authenticate the user
        try:
            user = auth.sign_in_with_email_and_password(username, password)
            print(user, flush=True)
            id = user.get("localId", "")

            data = db.child("users").child(id).get().val()
            fname = data.popitem(last=False)
            locations = None
            for key, value in data.items():
                if key == 'location':
                    locations = value
            
            userLocations = []
            for key, value in locations.items():
                userLocations.append(value)
            return render(request, 'main/profile.html', {'form': form, 'name':fname[1], 'userLocations': userLocations})
        except HTTPError as exc:
            messages.add_message(request, messages.INFO, json.loads(exc.strerror)['error']['message'])
            return redirect('index')

def show_location_on_map(request):
        longitude = 6.43545
        latitude = 3.242455
        return render(request, 'main/mapview.html', {'lon':longitude, 'lat':latitude})

        # If the user exists in our database
        # if user is not None:
        #
        #     # If the user's account has not been disabled
        #     if user.is_active:1
        #
        #         # Sign the user in
        #         # login(request, user)
        #         #assigns = Assign.objects.filter(user=request.user)
        #         # If the user's details have been verified, redirect him/her to the JAM page
        #         #return redirect('/JAM/', {'jobs': jobs})
        #         # return redirect('/')
        #     else:
        #         else render(request, 'Base/login.html', {'error_message': 'Account Disabled', 'form': form})
        # else:
        #     return render(request, 'Base/login.html', {'error_message': 'Invalid login', 'form': form})


def getUserData(id):
    return db.child("users").child(id).get().val()



# def register(request):
#     if request.method == "POST"

#     email = username = request.POST['username']
#     password = request.POST['password']

#     fName = request.POST['firstName']
#     lName = request.POST['lastName'] FKWcniHIG4fLhvVpJTza9djJjDn2

#     user = auth.create_user_with_email_and_password(email, password)
#     if user not None

