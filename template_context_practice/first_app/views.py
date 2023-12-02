from django.shortcuts import render

import datetime

# Create your views here.

def home(request):
    d={'name':'mamun', 'age':23, 'course':[
        
        {
            'id':2,
            'name':'python',
            'fee': 5000
        },
        
        {
            'id':3,
            'name': 'django',
            'fee': 5500
        },
        {
            'id':1,
            'name':'C',
            'fee': 2000
        }
    ], 'fun': ['python','is', 'fun'], 'start_course': datetime.datetime.now(), 'love':'I love Bangladesh', 'numbers':[10,4,8,7,30]}
    return render(request, 'home.html', d)