from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime

# Create your views here.
def index(request):

	#return render(request, 'login.html')
	playlist = [{'class':"Female Abnormal","dt":"08/21/2019,21:09:04","class_type":"danger"},
	{'class':"Child Normal","dt":"08/21/2019,22:09:04","class_type":"normal"}]
	return render(request, 'index1.html',{'recent_class':"Female Normal Voices",'datetime': datetime.now().strftime("%m/%d/%Y,%H:%M:%S"),'playlist':playlist,'class_type':"normal"})


def login(request):
	print("login")
	request.session['username'] = "user"
	return HttpResponseRedirect('/index/')
	'''
	submitted = False
	if request.method == 'POST':
		form=AdminForm(request.POST)
		inputdata = request.POST.copy()
		name = inputdata.get('username')
		pwd = inputdata.get('password')
		admin_data=Admin.nodes.get(username='admin')
		db_name=admin_data.username
		db_pwd=admin_data.password
		print(db)
		if name==db_name and pwd==db_pwd:
			request.session['username'] = name
			return HttpResponseRedirect('/admin/')
			#return render(request,"/admin/")
			#return HttpResponse(request.session['username'])
			#return HttpResponse("session created!")
		else:
			return HttpResponseRedirect('/login/?submitted=False')
	else:
		form = Admin()
		if 'submitted' in request.GET:
			submitted = True

	return render(request,"login.html")
	'''
	#return render(request, 'login.html')

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
