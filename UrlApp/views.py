from django.shortcuts import render
from .form import UserForm, SearchName
from .models import UrlForm



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