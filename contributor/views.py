from django.shortcuts import render
from customer.models import *
from account.models import *
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request, 'contributor/index.html')

def PublishBookView(request):
    # file = CustomUser.objects.get(id = user_id)
    if request.method =="POST":
        form = BookForm(data = request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contributor/index.html')
    else:
        form = BookForm(data = request.POST)
    return render(request, 'contributor/postapage.html', {'form': form}) 
    # if request.method == 'POST':
    #     form = BookForm(data = request.POST)
    #     if form.is_valid():
    #         form.save()
    # form = BookForm(data = request.POST)
    # return render(request, 'contributor/postapage.html', { 'form': form})