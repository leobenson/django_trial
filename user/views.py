from django.shortcuts import redirect, render
from user.models import *
def upload(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        image = request.FILES.get('image')
        name = data.get('name')
        des = data.get('des')
        print(name)
        print(des)
        print(image)
        reg.objects.create(
            image = image,
            name = name,
            des = des,
        )
        return redirect('/upload')
    
    queryset = reg.objects.all()
    context = {'upload':queryset}
    return render(request,"upload.html",context)        

def my_view(request):
    if request.method == "POST":
        return redirect('display')

    
def delete(request, id):
    queryset = reg.objects.get(id = id)
    queryset.delete()
    return redirect('/upload')

def update(request , id):
    queryset = reg.objects.get(id = id)
    if request.method == "POST":
        data=request.POST
        image = request.FILES.get('image')
        name = data.get('name')
        des = data.get('des')

        queryset.name= name
        queryset.des = des
        if image:
            queryset.image=image

        queryset.save()    
    context = {"update" : queryset}
    return render(request, 'update.html',context)

