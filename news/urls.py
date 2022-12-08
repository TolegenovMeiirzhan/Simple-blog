from django.urls import path
from .views import *
urlpatterns = [
    path('login/', user_login, name='login'),
    path('mail/', contact_mail, name='mail'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('test/', test, name='test'),
    # path('', index, name='index'),
    path('', HomeNews.as_view(), name='index'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', View_news.as_view(), name='view_news'),
    path('news/add-news', Add_news.as_view(), name='add_news'),
    # path('news/', include('news.urls')),
]
