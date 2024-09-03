from django.shortcuts import render
import requests
def index(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    user=response.json()
    context= {
        "data":user
    }
    return render(request, "index.html",context)
