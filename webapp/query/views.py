# query/views.py

from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import reverse
from query.models import Tweet
from analysis.models import Study, Tumblr_Study
from accounts.models import Profile
from subprocess import Popen, PIPE
from django.contrib.auth.decorators import login_required
from geopy.geocoders import Nominatim
import pexpect
import subprocess
import os
import json
import time
#### 11/17/2020 ####
from textblob import TextBlob
from django.views.generic.base import TemplateView
from datetime import date, datetime
import easy_date
#import date_converter
#### 11/17/2020 ####

def index(request):
	 render(request, 'index.html')

def twitter(request):
	return render(request, 'query/query.html', {})

def tumblr(request):
	return render(request, 'query/tumblr.html', {})

def validate_massmine(request):
	#sadhana_testuser_59
	#my_profile = request.user.profile
	my_profile = Profile.objects.filter(user_id = request.user.id, social_platform=request.POST.get('txtPlatformType')).first()
	consumer_key = my_profile.consumer_key
	consumer_secret = my_profile.consumer_secret
	access_token = my_profile.access_token
	access_token_secret = my_profile.access_token_secret

	child = pexpect.spawn('/usr/local/bin/massmine/./massmine --task=twitter-auth')
	#child4 = pexpect.spawn('/usr/local/bin/massmine/./massmine --help')
	child.expect('[No]')
	child.sendline('yes')
	child.expect('Consumer key:')
	child.sendline(consumer_key)
	child.expect('Consumer secret:')
	child.sendline(consumer_secret)
	child.expect('Access token')
	child.sendline(access_token)
	child.expect('Access token secret')
	child.sendline(access_token_secret)

	child.expect("Will you access Twitter's premium.*")
	child.sendline('no')
	child.expect ("Will you access Twitter's premium.*")
	child.sendline('no')
	child.wait()
	#child.wait()
	#exit status should be 0 on a success, 1 on a fail. signal status is if something else interrupted the command.
	return(child.exitstatus)
	#return(0)


#
# def validate_massmine_facebook(request):
#
# 	my_profile_fbook = instance_fbook=request.user.profile
# 	app_id = my_profile_fbook.app_id
# 	app_secret = my_profile_fbook.app_secret
# 	access_token = my_profile_fbook.access_token
# 	child1 = pexpect.spawn('massmine --task=facebook-auth')
# 	child1.expect('[No]')
# 	child1.sendline('yes')
# 	child1.expect('app ID')
# 	child1.sendline(app_id)
# 	child1.expect('app Secret')
# 	child1.sendline(app_secret)
# 	child1.expect('Access token')
# 	child1.sendline(access_token)
#
# 	child1.wait()
# 	#exit status should be 0 on a success, 1 on a fail. signal status is if something else interrupted the command.
# 	return(child1.exitstatus)
# 	#return(0)

#
# def validate_massmine_instagram(request):
#
# 	my_profile_insta = instance_insta=request.user.profile
# 	client_id = my_profile_insta.app_id
# 	client_secret = my_profile_insta.app_secret
# 	access_token_insta = my_profile_insta.access_token
# 	child2 = pexpect.spawn('massmine --task=instagram-auth')
# 	child2.expect('[No]')
# 	child2.sendline('yes')
# 	child2.expect('Client Id')
# 	child2.sendline(client_id)
# 	child2.expect('Client Secret')
# 	child2.sendline(client_secret)
# 	child2.expect('Access token')
# 	child2.sendline(access_token_insta)
# 	child2.wait()
# 	#exit status should be 0 on a success, 1 on a fail. signal status is if something else interrupted the command.
# 	return(child2.exitstatus)

#
# def validate_massmine_youtube(request):
#
# 	my_profile_ytube = instance_ytube=request.user.profile
# 	client_id = my_profile_ytube.app_id
# 	client_secret = my_profile_ytube.app_secret
# 	#oauth_client_id = my_profile_ytube.oauth_client_id
# 	#oauth_client_secret = my_profile_ytube.oauth_client_secret
# 	refresh_token_ytube = my_profile_ytube.access_token
# 	child3 = pexpect.spawn('massmine --task=youtube-auth')
# 	child3.expect('[No]')
# 	child3.sendline('yes')
# 	child3.expect('Client Id')
# 	child3.sendline(client_id)
# 	child3.expect('Client Secret')
# 	child3.sendline(client_secret)
# 	child3.expect('refresh token')
# 	child3.sendline(refresh_token_ytube)
# 	child3.wait()
# 	#exit status should be 0 on a success, 1 on a fail. signal status is if something else interrupted the command.
# 	return(child3.exitstatus)



def validate_massmine_tumblr(request):
	my_profile_tumblr = Profile.objects.filter(user_id=request.user.id,
										social_platform=request.POST.get('txtPlatformType')).first()
	#my_profile_tumblr = instance_tumblr = request.user.profile
	consumer_key = my_profile_tumblr.consumer_key
	consumer_secret = my_profile_tumblr.consumer_secret
	access_token = my_profile_tumblr.access_token
	access_token_secret = my_profile_tumblr.access_token_secret

	child4 = pexpect.spawn('/usr/local/bin/massmine/./massmine --task=tumblr-auth')
	#child4 = pexpect.spawn('/usr/Documents/django/Massmine_new/massmine/./massmine --task=tumblr-auth')
	child4.expect('[No]')
	child4.sendline('yes')
	child4.expect('Consumer key:')
	child4.sendline(consumer_key)
	child4.expect('Consumer secret:')
	child4.sendline(consumer_secret)
	child4.expect('Token')
	child4.sendline(access_token)
	child4.expect('Token secret')
	child4.sendline(access_token_secret)
	child4.wait()
	#exit status should be 0 on a success, 1 on a fail. signal status is if something else interrupted the command.
	return(child4.exitstatus)
	#return(0)

def platforms(request): 
			return render(request,'query/platform.html')


def platforms1(request):
			return render(request,'query/platform.html')


@login_required
def make_query(request):

	if (validate_massmine(request) != 0):
		return render(request, 'query/query_error.html', {})

	else:
		keyword = request.POST.get('keyword')
		mydropdown1=request.POST.get('mydropdown1')
		keyword2 = request.POST.get('keyword2')
		mydropdown2 = request.POST.get('mydropdown2')
		keyword3 = request.POST.get('keyword3')
		count = request.POST.get('count')
		location = request.POST.get('location')
		geolocator = Nominatim(user_agent='my_user_agent')
		Location = geolocator.geocode(location)
		p2=Location.latitude
		p1=Location.longitude
		p3 = str(p1)+","+str(p2)+","+str(p1+1)+","+str(p2+1)
		#### 11/17/2020 ###
		From = request.POST.get("From")
		To = request.POST.get("To")
		my_time = datetime.min.time()

		#new_from_date = easy_date.convert_from_string(From,'%yyyy-%mm-%dd','%yyyy-%mm-%dd')
		from_1 = datetime.fromisoformat(From)
		#new_to_date = easy_date.convert_from_string(To,'%mm-%dd-%yyyy','%yyyy-%mm-%dd')
		to_1 = datetime.fromisoformat(To)

		#### 11/17/2020 ####


		command = '/usr/local/bin/massmine/./massmine --task=twitter-stream --geo=' + str(p3) + ' --count=' + '"' + count + '"' + ' --query=' + '"' + keyword + '"' + '"' + mydropdown1 + '"' + keyword2 + '"' + mydropdown2 + '"' + keyword3 + '"' + str(from_1) + '"' + str(to_1)
		#command = '/usr/local/bin/massmine/./massmine --task=twitter-stream --geo='  + str(p3) +' --count=' + '"' + count + '"' + ' --query=' + '"' + keyword + '"'
		#command = '/usr/bin/massmine/./massmine --task=twitter-stream --geo=35.2272,-80.843083 --count=' + '"' + count + '"' + ' --query=' + '"' + keyword + '"'
		#command = r"/usr/bin/massmine/./massmine --task=twitter-stream --query=facts --count=30 --dur='2019-10-11 14:30:00'"
		#command = '/usr/bin/massmine/./massmine --task=twitter-stream --geo=-74,40,-73,41 --count=' + '"' + count + '"' + ' --query=' + '"' + keyword + '"'
		#command = '/usr/bin/massmine/./massmine --task=twitter-stream  --dur=''2019-10-11 14:30:00'' --count=' + '"' + count + '"' + ' --query=' + '"' + keyword + '"'

		#command = '/usr/bin/massmine/./massmine --task=twitter-search --count=' + count + ' --query=' + '"'+keyword+'"' +
		#command = '/usr/bin/massmine/./massmine --task=twitter-stream --count=' + count + ' --query=' + '"' + keyword+ '"'
		#command = '/usr/bin/massmine/./massmine --task=twitter-stream --count=' + count + ' --query=' + '"' + keyword + '"' + '--dur= 2015-10-11 14:30:00' + 'geo = -74'


		for key, value in request.POST.items():
			if key.startswith('customElementInput'):
				customId = key.split('customElementInput',1)[1]
				customDDValue = request.POST.get('customElementDD' + customId)
				customInputValue = request.POST.get('customElementInput' + customId)
				print(customDDValue + ":   " + customInputValue)
				command = command + '"' + customDDValue + '"' + customInputValue

		#command = "/usr/local/bin/massmine/./massmine --task=twitter-stream --count=300 --geo=-74,40,-73,41"
		#command =  "/usr/local/bin/massmine/./massmine --task=tumblr-posts --query=kingjamesprogramming --count=10"
		stdout = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

		output = stdout.readlines()
		#stdout.writelines(output)
		hshtg = None
		keyword = keyword.replace(' ','_')
		new_study = Study(user=str(request.user),study_id=keyword+str(int(time.time())), count=count)
		new_study.save()

		for i in output:
			string = i.decode("utf-8")
			if(string == '\n'):
				continue
			data = json.loads(string)

			try:

				for key,value in data.items():
					if (key == 'id_str'):
						tid = value
	
					if (key == 'created_at'):
						ca = value
					if (key == 'text'):
						txt = value
					if (key == 'source'):
						src = value
					if (key == 'truncated'):
						trunc = value
					if (key == 'retweet_count'):
						re_count = value
					if (key == 'metadata'):
						for key,value in data['metadata'].items():
							if (key == 'iso_language_code'):
								language = value
							else:
								language = 'en'
					else:
						language = 'en'
					if (key == 'entities'):
						for key,value in data['entities'].items():
							if (key == 'hashtags'):
								for n in data['entities']['hashtags']:
									hshtg  = n['text']
					if (key == 'user'):
						for key,value in data['user'].items():
							if (key == 'id_str'):
								uid = value
							if (key == 'location'):
								cntry = value

							if (key == 'name'):
								nme = value
							if (key == 'screen_name'):
								scr_name= value
							if (key == 'url'):
								u = value
							if (key == 'description'):
								desc = value
							if (key == 'verified'):
								verify = value
							if (key == 'followers_count'):
								fol_count = value
							if (key == 'listed_count'):
								list_count = value
							if (key == 'favourites_count'):
								fav_count = value
							if (key == 'statuses_count'):
								tw_count = value
							if (key == 'utc_offset'):
								utc_off = value
							if (key == 'friends_count'):
								fr_count = value
							if (key == 'time_zone'):
								tz = value
							if (key == 'geo_enabled'):
								geo_en = value
					if (key == 'in_reply_to_status_id_str'):
						reply_sid = value
					if (key == 'in_reply_to_user_id_str'):
						reply_uid = value
					if  	(key == 'in_reply_to_screen_name'):
						reply_scrname = value

				##print(txt)
				textBlob = TextBlob(txt)

				if textBlob.sentiment[0] < 0:
					sentimentvalue = textBlob.sentiment[0]
				elif textBlob.sentiment[0] == 0:
					sentimentvalue = textBlob.sentiment[0]
				else:
					sentimentvalue = textBlob.sentiment[0]
				#sentimentvalue = "test"
				new_study.tweets.create(tweet_id_str=tid,created_at=ca,text=txt,device=src,truncated=trunc,
						retweet_count=re_count,lang=language, country=cntry,user_id_str=uid,name=nme,
						screen_name=scr_name,in_reply_to_status_id_str=reply_sid,in_reply_to_user_id_str=reply_uid,
						in_reply_to_screen_name=reply_scrname,hashtags=hshtg,url=u,
						description=desc,verified=verify,followers_count = fol_count,friends_count=fr_count,
						listed_count=list_count,favourites_count=fav_count,num_tweets=tw_count,
						utc_offset=utc_off,time_zone=tz,geo_enabled=geo_en,sentiment=sentimentvalue)

			except Exception as e:
				print(e)
			
		return render(request, 'query/query_complete.html', {})

#lang=language#lang=language


def make_query_tumblr(request):
	keyword = None
	count = None
	command = None
	if (validate_massmine_tumblr(request) == 1):
		return render(request, 'query/query_error.html', {})
	else :
		#print("Hello Tumblr")
		queryType = request.POST.get('hdnTumblrQueryType')

		if queryType == "TumblrTags":
			keyword = request.POST.get('keyword_tags')
			count = request.POST.get('count_tags')
			command = '/usr/local/bin/massmine/./massmine --task=tumblr-tag --count=' + count + ' --query=' + '"' + keyword
		else:
			keyword = request.POST.get('keyword_posts')
			count = request.POST.get('count_posts')
			command = '/usr/local/bin/massmine/./massmine --task=tumblr-posts --count=' + count + ' --query=' + '"' + keyword

		for key, value in request.POST.items():
			if key.startswith('customElementInput'):
				customId = key.split('customElementInput',1)[1]
				#customDDValue = request.POST.get('customElementDD' + customId)
				customInputValue = request.POST.get('customElementInput' + customId)
				#print(customDDValue + ":   " + customInputValue)
				command = command + ',' + customInputValue

		command = command + '"'
		#command =  '/usr/local/bin/massmine/./massmine --task=tumblr-posts --query=' + keyword + ' --count=' + '"' + count + '"'
		stdout = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

		output = stdout.readlines()

		new_study = Tumblr_Study(user=str(request.user),tumblr_study_id=keyword+str(int(time.time())), count=count)
		new_study.save()

		now_Time = datetime.now()
		currentTime = now_Time.strftime("%H%M%S")

		for i in output:
			string = i.decode("utf-8")
			if(string == '\n'):
				continue
			data = json.loads(string)
			try:
				for key,value in data.items():
					if (key == 'type'):
						type = value
					if (key == 'id_string'):
						tpid = value + currentTime
					if (key == 'blog_name'):
						b_name = value
					if (key == 'blog'):
						for key,value in data['blog'].items():
							if (key == 'name'):
								name = value
							if (key == 'title'):
								title = value
							if (key == 'description'):
								desc = value
							if (key == 'url'):
								url = value
							if (key == 'uuid'):
								uuid = value
							if (key =='updated'):
								updated = value
					if (key == 'post_url'):
						p_url = value
					if (key == 'date'):
						date = value
					if (key == 'timestamp'):
						t_stamp = value
					if (key == 'state'):
						state = value
					if (key == 'format'):
						format = value
					if (key == 'reblog'):
						for key,value in data['reblog'].items():
							if (key == 'comment'):
								comment = value
					if (key == 'can_reblog'):
						can_reblog = value
					if (key == 'can_reply'):
						can_reply = value

				new_study.posts.create(tumblr_id_str = tpid ,tumblr_type_str = type, blogname_str= b_name, blog_name_str = name, blog_title_str= title, blog_description_str= desc,
											  blog_url_str=url,
											  blog_uuid_str= uuid,
											  updated_at= updated,
											  post_url_str= p_url,
											  date = date,
											  timestamp= t_stamp,
											  state= state,
											  format= format,
											  comment= comment,
											  can_reblog= can_reblog,
											  can_reply= can_reply )

			except Exception as e:
				print(e)
		return render(request, 'query/query_complete_tumblr.html', {})


