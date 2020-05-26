from django.shortcuts import render,  get_object_or_404,  redirect
from .models import Person
from .forms import PostForm

# Create your views here.
#Views sind Verbindung zwischen Models und Templates
def post_list(request):
    person = Person.objects.order_by('lastName')
    return render(request,  'adressverwaltung/post_list.html', {'person':person})
#    
def post_detail(request,  pk):
    person= get_object_or_404(Person,  pk=pk)
    return render(request,  'adressverwaltung/post_detail.html',  {'person':person})
#
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.is_valid()
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('post_detail',  pk=person.pk)
    else:
        form = PostForm()
    return render(request,  'adressverwaltung/post_edit.html',  {'form':form})
#
def post_edit(request,  pk):
    person = get_object_or_404(Person,  pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,  instance = person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('post_detail',  pk=person.pk)
    else:
            form = PostForm(instance=person)
    return render(request,  'adressverwaltung/post_edit.html',  {'form':form})
    
