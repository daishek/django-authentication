from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignupForm, UserForm, ProfileForm

from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):
    if request.method == 'POST': # save form...
        form = SignupForm(request.POST)
        # CHECK IF FORM IS VALID
        if form.is_valid():
            # then create & save 
            form.save()
            # After thaaaat log in the user
            # to authenticate we need username & password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            # then login with this data [user] and redirect to home page
            login(request, user)
            return redirect('/accounts/profile')


    else: # != 'POST'  show form...
        form = SignupForm()
    context = {'form':form}

    return render(request, 'registration/signup.html', context)

def profile(request):
    print(request.user)
    profile = Profile.objects.get(user=request.user)
    print(profile)
    context = {'profile':profile}
    return render(request, 'profile/profile.html', context)

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myform = profileform.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    context = {
        'profile':profile,
        'userform':userform,
        'profileform':profileform,

    }
    return render(request, 'profile/profile_edit.html', context)