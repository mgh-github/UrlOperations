import os

from django.conf import settings
from django.shortcuts import render
from .form import UserForm, SearchName, imgdown
from .models import UrlForm
from .image import imagedownload




def UrlDetails(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request, 'UrlForm.html', context)


def Search(request):
    form = SearchName()
    urlInfo = []
    if request.method == 'GET':
        form = SearchName(request.GET)
        if form.is_valid():
            searchText=request.GET.get('name')
            urlInfo=UrlForm.objects.filter(name__icontains=searchText)


    context = {'form' : form,'results':urlInfo}
    return render(request, 'Search.html', context)


def getimage(request):
    folderPath = settings.MEDIA_ROOT
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            os.remove(os.path.join(root, file))
    form = imgdown()
    imageList=[]
    if request.method == 'GET':
        form = imgdown(request.GET)
        if form.is_valid():
          imageurl = request.GET.get('name')
          imagedownload(imageurl, folderPath)
          imageList = get_image_path()



    context = {'form': form,'images':imageList }
    return render(request, 'GetImages.html', context)

def get_image_path():
    filelist=[]
    for root, dirs, files in os.walk('\Media'):
        for file in files:
            filelist.append( os.path.join('\Media', file))
    return filelist