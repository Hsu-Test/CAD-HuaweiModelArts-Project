from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from .models import Login
from .forms import LoginForm
from .models import category

# Create your views here.
def index(request):
	p = category.objects.raw('SELECT categoryId FROM RecordCategory ORDER BY startDate')
	startDate = str(p[len(p)-1].startDate).split()
	voice = p[len(p)-1].typeOfVoice.split()
	current = {'class_type':voice[1],
    	'typeOfVoice':voice[0],
    	'startDate':startDate[0]+","+startDate[1]}
	
	return render(request, 'index1.html',{'current':current,'playlists':p})



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
	playlist = [{'class':"Female Abnormal","dt":"2019/08/24 00:33:56","class_type":"danger"},
	{'class':"Child Normal","dt":"2019/08/24 00:33:56","class_type":"normal"}]
	return render(request, 'playlists.html',{'recent_class':"Female Normal Voices",'datetime': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'playlist':playlist,'class_type':"normal"})

def add_category(request):

    #data = category.objects.filter(userId="u0000001")
    #print(data)
    #test = category.objects.all()
    #for p in category.objects.raw('SELECT categoryId FROM RecordCategory where categoryId = "c000001"'):
    	#print(p.categoryId)

    #category.objects.raw('INSERT into RecordCategory values ("c000002","Child Abnormal","2019/08/24 00:34:57","2019/08/24 00:35:57","u0000001")')
    b = category(categoryId='c000007', typeOfVoice='Woman normal',startDate = "2019-08-24 00:34:58",endDate = "2019-08-24 00:35:57",userId = "u0000001")
    b.save()
    p = category.objects.raw('SELECT categoryId FROM RecordCategory ORDER BY startDate')
    print(len(p))
    startDate = str(p[len(p)-1].startDate).split()
    voice = p[len(p)-1].typeOfVoice.split()
    current = {'class_type':voice[1],
    'typeOfVoice':voice[0],
    'startDate':startDate[0]+","+startDate[1]}
    
    playlists = []
    for pp in p:
    	startDate = str(pp.startDate).split()
    	voice = pp.typeOfVoice.split()
    	playlists.append({'class_type':voice[1],
    	'typeOfVoice':voice[0],
    	'startDate':startDate[0]+","+startDate[1]})


    #return render(request, 'login.html')
    return render(request, 'index1.html',{'current':current,'playlists':playlists})




	#return render(request, 'playlists.html')
