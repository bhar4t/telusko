from django.shortcuts import render

def home(request):
    return render(request, 'home.html', { 'name': 'Bharat' })

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 + num2
    return render(request, 'result.html', { 'result': res })