from django.shortcuts import render

# Create your views here.

def main(request):
	return render(request, 'base/main.html')

def home(request):
		return render(request, 'base/home.html')

def blog(request):
	return render(request, 'base/blog.html')



def Q1(request):
	return render(request, 'base/Q1.html')


def Q2(request):
	return render(request, 'base/Q2.html')

def Q3(request):
	return render(request, 'base/Q3.html')

def Q4(request):
	return render(request, 'base/Q4.html')
