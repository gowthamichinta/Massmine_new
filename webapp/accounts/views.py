# accounts/views.py
import django_tables2
from dateutil.parser import parse
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import UserRegistrationForm, ProfileForm, EditUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.db import transaction

from accounts.models import Profile, SocialPlatformProfile


def index(request):
    return render(request,'index.html')
    
def twitter_index(request):
    return render(request,'twitter_index.html')

def login_error(request):
    return render(request,'login_error.html')

def account_inactive_error(request):
    return render(request,'account_inactive_error.html')

@login_required
def password_change_error(request):
    return render(request,'password_change_error.html')

def platform(request):
    return render(request,'accounts/platform.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)

        #platformType = form.data.get('txtPlatformType')
        #if (platformType == 'twitter'):
        #    redirectURL = '/accounts/platform/'
        #elif (platformType == 'tumblr'):
        #    redirectURL = '/accounts/platform/'

        if("username") in form.errors:
                if form.errors["username"][0] == 'A user with that username already exists.':
                    return redirect('/accounts/platform/')
        if form.is_valid():
            user = form.save()
            username = form.data.get('username')

        return redirect('/accounts/platform/')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/registration_user.html',
                  {'form':form})

def register_twitter(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)

        if True:
            userDetails = User.objects.get(username=form.data.get('hdnUserNameTwitter'))
            profileExists = Profile.objects.filter(user_id = userDetails.id, social_platform=form.data.get('txtPlatformType')).first()

            if (profileExists == None):
                 Profile.objects.create(user_id=userDetails.id,
                                                 consumer_key=form.data.get('consumer_key'),
                                                 consumer_secret=form.data.get('consumer_secret'),
                                                 access_token=form.data.get('access_token'),
                                                 access_token_secret=form.data.get('access_token_secret'),
                                                 social_platform=form.data.get('social_platform'))
            return redirect('/accounts/user_login/')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration_twitter.html',
                  {'form':form})


def register_tumblr(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)

        if True:
            userDetails = User.objects.get(username=form.data.get('hdnUserNameTumblr'))
            profileExists = Profile.objects.filter(user_id=userDetails.id,
                                                social_platform=form.data.get('social_platform')).first()

            if (profileExists == None):
                Profile.objects.create(user_id=userDetails.id,
                                       consumer_key=form.data.get('consumer_key'),
                                       consumer_secret=form.data.get('consumer_secret'),
                                       access_token=form.data.get('access_token'),
                                       access_token_secret=form.data.get('access_token_secret'),
                                       social_platform=form.data.get('social_platform'))
            return redirect('/accounts/user_login/')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration_tumblr.html',
                  {'form':form})


@login_required
@transaction.atomic
def edit_user_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('twitter_index'))
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', 
            {'user_form':user_form, 'profile_form': profile_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('twitter_index'))
        else:
            return render(request,'accounts/password_change_error.html', {})
	    #form not valid
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request,'accounts/change_password.html', args)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'twitter_index.html', {})
                #return HttpResponseRedirect(reverse('twitter_index'))
            else:
                return render(request,'accounts/account_inactive_error.html',{})
        else:
            return render(request,'accounts/login_error.html', {}) 
	    #username or password incorrect
    else:
        return render(request, 'accounts/login.html', {})