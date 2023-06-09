from django.shortcuts import render
from user.models import *
def register(request):
    data = request.POST
    print(data)
    image = request.FILES.get('image')
    name = data.get('username')
    email = data.get('email')
    print(name)
    print(email)
    print(image)
    reg.objects.create(
        image = image,
        username = name,
        email = email,
    )
    return render(request,"register.html")
    

    
    
