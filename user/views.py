from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm
from .forms import SignInForm



# Create your views here.
def index(request):
    return render(request,'user/index.html')

def signup_view(request):
    
    if request.method == 'POST':
        print("post:", request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('is_valid')
            form.save()  # Save the user to the database
            messages.success(request, 'The user has been created successfully.')
            return redirect('signin')  # Redirect to the login page
        else:
           
            return render(request, 'user/signup.html', {'form': form})
    else:
        
        form = SignUpForm()
        
    
    return render(request, 'user/signup.html', {'form': form})


def signin_view(request):
   
    if request.method == 'GET':
         form = SignInForm()
         return render(request, 'user/signin.html', {'form': form})
    
    if request.method == 'POST':

        form = SignInForm(request, data=request.POST)
        
        if form.is_valid():

            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate the user with the provided credentials
            user = authenticate(request, username=username, password=password)
           
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, 'Logged in successfully.')
                return redirect('dashboard')  # Redirect to the homepage or a dashboard
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = SignInForm()
       
        return redirect('/signin')

def dashboard(request):
    return render(request,'user/dashboard.html')