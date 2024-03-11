from django.shortcuts import render
import datetime

def home(request):
    UsersArray = {
        "users" : [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "date": datetime.datetime.now()
        },
        {
            "id": 2,
            "name": "Robert Hook",
            "username": "Hook",
            "email": "Hook@april.biz",
            "phone": "1-886-779-8031 x56442",
            "website": "Hook.org",
            "date": datetime.datetime.now()
        },
    ]
    }
    return render(request, 'home.html',context=UsersArray)
