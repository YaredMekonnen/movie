from django.http import HttpResponse
from django.shortcuts import render

data={
    'movies': [
       {
        'id':5,
        'title' : 'Jaws',
        'year': 1600

       },
       {
        
        'id':5,
        'title' : 'Jaws',
        'year': 1600

       },
       {
        
        'id':5,
        'title' : 'Jaws',
        'year': 1600

       },
       {
        
        'id':5,
        'title' : 'Jaws',
        'year': 1600

       }



    ]
}


def movies(request):
    return render(request,'movies/movies.html',data)


def home(request):
    return(HttpResponse("Home Page!"))

