from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from .models import Login
from .forms import LoginForm

# Create your views here.
def index(request):

	#return render(request, 'login.html')
	playlist = [{'class':"Female Abnormal","dt":"08/21/2019,21:09:04","class_type":"danger"},
	{'class':"Child Normal","dt":"08/21/2019,22:09:04","class_type":"normal"}]
	return render(request, 'index1.html',{'recent_class':"Female Normal Voices",'datetime': datetime.now().strftime("%m/%d/%Y,%H:%M:%S"),'playlist':playlist,'class_type':"normal"})


def login(request):
	#print("login")
	#request.session['username'] = "user"
	#return HttpResponseRedirect('/index/')
	
	submitted = False
	if request.method == 'POST':
		form=LoginForm(request.POST)
		inputdata = request.POST.copy()
		email = inputdata.get('email')
		pwd = inputdata.get('password')
		print(email,pwd)
		#if name==db_name and pwd==db_pwd:
			#request.session['username'] = name
			#return HttpResponseRedirect('/admin/')
			#return render(request,"/admin/")
			#return HttpResponse(request.session['username'])
			#return HttpResponse("session created!")
		name = "Mary"
		if email =="user@gmail.com" and pwd == "user123":
			request.session['username'] = name

		return HttpResponseRedirect('/index/')
	else:
		form = LoginForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request,"login.html")
	

def signup(request):

	return render(request, 'signup.html')


def logout(request):

	try:
		del request.session['username']
	except KeyError:
		pass
	return HttpResponseRedirect('/index/')
    #return HttpResponseRedirect('/login/?submitted=False')


def playlists(request):
	playlist = [{'class':"Female Abnormal","dt":"08/21/2019,21:09:04","class_type":"danger"},
	{'class':"Child Normal","dt":"08/21/2019,22:09:04","class_type":"normal"}]
	return render(request, 'playlists.html',{'recent_class':"Female Normal Voices",'datetime': datetime.now().strftime("%m/%d/%Y,%H:%M:%S"),'playlist':playlist,'class_type':"normal"})



	#return render(request, 'playlists.html')
