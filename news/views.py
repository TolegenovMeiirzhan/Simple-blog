from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm # form for users
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

# Create your views here.
from .models import *
from .forms import Newsform, RegisterForm, User_loginForm, ContactForm
from .utils import My_ex

# ----------------send mail ----------------------
def contact_mail(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['message'],
'tolegenovmeiirzhan@inbox.ru',[form.cleaned_data['email']], fail_silently=False)
            if mail:
                messages.success(request,'Message sended')
                return redirect('mail')
            else:
                messages.error(request,'Error with send!')
        else:
            messages.error(request,'Validation error!')
    else:
        form = ContactForm()
    return render(request,'news/contact.html',{'form': form})


# --------------------user create-----------------------------

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User success created!')
            return redirect('login')
        else:
            messages.error(request, 'You have error with register!')
    else:
        form = RegisterForm()
    return render(request, 'news/register.html', {'form': form})

# -------------------login---------------------------------

def user_login(request):
    if request.method == 'POST':
        form = User_loginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,'You succes Autenthicated!')
            return redirect('index')
        else:
            messages.error(request, 'You have errors!')
    else:
        form = User_loginForm()
    return render(request,'news/login.html',{'form': form})

# ------------------log out---------------------------
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been successfully logged out!')
    return redirect('index')

# --------------------------pagination def------------------------------------
def test(request):
    objects = ['1','2','3','4','5']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page',1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj':page_obj})


# --------------------------index------------------------------------
class HomeNews(ListView):
    model = News
#     defoult template name = 'app_name/model_name(lower)_list.html -- news/news_list.html
#     defoult context for object is -- object_list
    template_name = 'news/index.html'
    context_object_name = 'news'
    # queryset = News.objects.select_related('category') # its for sql requests
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Жаңалықтар"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')



# def index(request):
#     news = News.objects.all()
#     # categories = Category.objects.all()
#     context = {'news': news}
#     return render(request, 'news/index.html', context)
# ----------------------------------- ---------------------------------- ------------------------------

# --------------------------category------------------------------------

class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False
    # если катеогория жок или категорияда новости жок болуга руксат бермиди
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     # categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {'news': news, 'category': category}
#     return render(request, 'news/category.html', context)
# ----------------------------------- ---------------------------------- ------------------------------

# --------------------------single_news------------------------------------

class View_news(DetailView):
    model = News
    template_name = 'news/single.html'
    # defoult template name = 'app_name/modelName(news)_detail.html - 'news/news_detail.html
    context_object_name = 'news_item'

#     defoult context name = 'object'
#     pk_url_kwarg = 'news_id'  # give name for pk like : news_id = pk

# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request,'news/single.html',{'news_item': news_item})
# ----------------------------------- ---------------------------------- ------------------------------

# --------------------------add_news------------------------------------
class Add_news(LoginRequiredMixin, CreateView):
    form_class = Newsform
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('view_news') # redirecting to the single news page
    # login_url = reverse_lazy('index')
    raise_exception = True

# def add_news(request):
#     if request.method == 'POST':
#         form = Newsform(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = Newsform()
#     return render(request, 'news/add_news.html', {'form': form})