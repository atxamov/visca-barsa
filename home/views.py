from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Book, Publisher
from django.core.files.storage import FileSystemStorage
from config import settings
from .forms import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.
class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher.html'

    def get_queryset(self):
        self.request.GET
        return Publisher.objects.filter(name__icontains='a')


class PublisherCreateView(CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'add-publisher.html'
    success_url = reverse_lazy('publishers')


class PublisherDetialView(DetailView):
    model = Publisher
    template_name = 'publisher-view.html'


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publisher_confirm_delete.html'
    success_url = reverse_lazy('publishers')


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher-update.html'
    fields = '__all__'
    success_url = reverse_lazy('publishers')


def index(request):
    query = {}
    for item in request.GET:
        query[item] = request.GET[item]
    
    ctx = {"books": Book.objects.filter(**query)}
    return render(request, 'index.html', context=ctx)

def glavnaya(request):
    return render(request, 'Главная.html')

def o_nas(request):
    return render(request, 'o-nas.html')

def add_book(request):
    if request.method == 'GET':
        return render(request, "add-book.html")
    else:
        book = Book(name=request.POST['book_name'], description=request.POST['book_desc'])
        
        image = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save('book-images/' + image.name, image)
        
        book.image = fss.url(file).replace('/media', '')
        book.save()
        return redirect(reverse_lazy('index'))

def view_book(request, id):
    if request.method == 'GET':
        book = Book.objects.get(pk=id)
        ctx = {'book': book}
        return render(request, 'view-book.html', context=ctx)
    else:
        book = Book.objects.get(pk=id)
        book.name = request.POST['book_name']
        book.description=request.POST['book_desc']


        if 'image' in request.FILES:
            fss = FileSystemStorage()

            fss.delete(str(settings.BASE_DIR) + str(book.image.url))

            image = request.FILES['image']
            file = fss.save('book-images/' + image.name, image)
        
            book.image = fss.url(file).replace('/media', '')

        book.save()
        return redirect(reverse_lazy('index'))

def delete_book(request, id):
    if request.method == 'GET':
        book = Book.objects.get(pk=id)
        ctx = {'book': book}
        return render(request, 'delete-book.html', context=ctx)
    else:
        book = Book.objects.get(pk=id)
        fss = FileSystemStorage()
        fss.delete(str(settings.BASE_DIR) + str(book.image.url))
        book.delete()
        return redirect(reverse_lazy('index'))

def manage(request):
    query = {}
    for item in request.GET:
        query[item] = request.GET[item]
    
    ctx = {"books": Book.objects.filter(**query)}
    return render(request, 'manage.html', context=ctx)
   
def login_view(request):
    if request.method =='GET':
        form = LoginForm()
        return render(request, template_name='login.html',context={'form':form})
    else:
        from django.contrib.auth import login,authenticate
        user = authenticate(request, username = request.POST['username'],password = request.POST['password'])
        if user:
            login(request, user)
            return redirect(reverse_lazy('index'))
        else:
            form = LoginForm()
            return render(request, template_name='login.html',context={'form':form, 'error_msg': 'Please, type correct user name and password'})

def logout_request(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse_lazy("index"))

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        form = RegisterForm(data=request.POST)
        if form.is_valid():

            user = form.instance
            user.set_password(request.POST['password'])
            form.save()

            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
                return redirect(reverse_lazy('index'))
            return render(request, template_name='register.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})
        
        return render(request, template_name='register.html', context={'form': form})