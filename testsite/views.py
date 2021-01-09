from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
	return render(request, 'index.html')

def result(request):
	lr = joblib.load('finalized_model.sav')

	lis=[]
	lis.append(request.GET['carat'])
	lis.append(request.GET['cut'])
	lis.append(request.GET['depth'])
	lis.append(request.GET['table'])
	lis.append(request.GET['area'])

	ans = lr.predict([lis])
	ans=ans.round(2)

	return render(request, 'result.html',{"ans":ans, 'lis':'\n'.join(lis)})