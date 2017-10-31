from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .firebasesetup import auth

form = UserForm

def index(request):
    # template = loader.get_template('main/profile.html')
    #  context = {'':''}
     return render(request, 'main/index.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'main/index.html'

    def get(self,request):
        pass

    def post(self,request):
        pass
def sign_in(request):
    # If the user has hit "login"
    if request.method == "POST":

        # Keep the user's username and power for verification
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = auth.sign_in_with_email_and_password(username=username, password=password)

        # If the user exists in our database
        # if user is not None:
        #
        #     # If the user's account has not been disabled
        #     if user.is_active:
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
    return render(request, 'main/login.html', {'form': form})
