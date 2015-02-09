from django.shortcuts import render

import json
from django.template import RequestContext
import datetime
import time
import json
import random
from datetime import date
from django.contrib import messages
from django.http import HttpResponse
from django.db import transaction
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from dailytask.models import *


def index(request):
	if request.method == "GET":
		return render_to_response("index.html", context_instance=RequestContext(request))
	elif request.method == "POST":
		email = request.POST.get("email")
		if User.objects.filter(email = email).exists():
			return render_to_response("home.html",{'email': email }, context_instance=RequestContext(request))
		else:
			task = User.objects.create(email = email)
			return render_to_response("home.html",{'email': email }, context_instance=RequestContext(request))
	else:
		return render_to_response("index.html", context_instance=RequestContext(request))


def home(request):
	if request.method == "GET":
		email = request.POST.get("email")
		return render_to_response("home.html",{'email': email }, context_instance=RequestContext(request))
	elif request.method == "POST":
		email = request.POST.get("email")
		if User.objects.filter(email = email).exists():
			todolist = TodayTask.objects.filter(email = email)
			return render_to_response("workdairy.html",{'todos': todolist, 'email': email }, context_instance=RequestContext(request))
		else:
			task = User.objects.create(email = email)
			return render_to_response("home.html",{'email': email }, context_instance=RequestContext(request))
	else:
		return render_to_response("index.html", context_instance=RequestContext(request))



def dairy(request):
	if request.method == "GET":
		email = request.user
		todolist = TodayTask.objects.filter(email = email, status = 'OPEN')
		
		return render_to_response("workdairy.html",{'todos': todolist, 'email': email }, context_instance=RequestContext(request))
	elif request.is_ajax():
		email = request.POST.get("email")
		wid = request.POST.get("wid")
		action = request.POST.get("action")
		
		if TodayTask.objects.filter(pk=wid).exists():
			task = TodayTask.objects.get(pk=wid)
			if(action == 'completed'):
				task.status = 'COMPLETED';
			else:
				task.status = 'CLOSE';
			task.save()
		content = {'msg': 'true'}
		return HttpResponse(json.dumps(content), mimetype='application/json')
	elif request.method == "POST":
		email = request.POST.get("email")
		
		name = request.POST.get("wname")
		
		timein = request.POST.get("start_time")
		time = datetime.datetime.strptime(timein, "%H:%M")
		creation_date = date.today()
		task = TodayTask.objects.create(email = email, date = creation_date, task_name = name, task_time = time)
		messages.success(request, "Task is added to todo list ")
		todolist = TodayTask.objects.filter(email = email, status = 'OPEN')
		
		return render_to_response("workdairy.html",{'todos': todolist, 'email': email }, context_instance=RequestContext(request))
	else:
		return render_to_response("index.html", context_instance=RequestContext(request))


def profile(request):
	if request.method == "GET":
		return render_to_response("profile.html", context_instance=RequestContext(request))
	elif request.method == "POST":
		email = request.POST.get("email")
		userinfo = User.objects.filter(email = email)
		pk = request.POST.get("pk")
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		if User.objects.filter(email = email).exists():
			user = User.objects.filter(email = email)
			user.name = name
			user.phone = phone
		userinfo = User.objects.filter(email = email)
		
		return render_to_response("profile.html", {'user': userinfo, 'email': email }, context_instance=RequestContext(request))

