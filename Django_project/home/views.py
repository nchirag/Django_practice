from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'John', 'age': 25, 'contact': '12345'},
        {'name': 'Doe', 'age': 30, 'contact': '67890'},
        {'name': 'Jane', 'age': 35, 'contact': '54321'},
        {'name': 'Dane', 'age': 12, 'contact': '98765'},
    ]
    availability_data = {'John': True, 'Jane': True, 'Doe': False, 'Dane': False}
    available_peoples = [{'name': person['name'], 'age': person['age'], 'contact': person['contact'], 'available': availability_data[person['name']]} for person in peoples]

        
    
    return render(request, 'index.html', context={'peoples': peoples, 'peoples_availability': available_peoples})

def success_pages(request):
    success_status = [
        {'name': 'John', 'status': 'Successful'},
        {'name': 'Dane', 'status': 'Successful'},
        {'name': 'Doe', 'status': 'Failure'},
        {'name': 'Jane', 'status': 'Failure'},
    ]
    return render(request,'success.html',context = {'success_status':success_status})
