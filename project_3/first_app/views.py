from django.shortcuts import render

# Create your views here.

def home(request):
    d={"author":"Shakil", "age":5, "lst":[2,3,4], "courses":[
        {
            "id": 1,
            "name":"python",
            "fee":10000
        },
        {
            "id": 2,
            "name":"Django",
            "fee":5000
        },
        {
            "id": 3,
            "name":"React",
            "fee":10000
        },
    ]}
    return render(request, 'first_app/home.html', d)
