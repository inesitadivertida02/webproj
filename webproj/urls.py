"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('Authors/', views.author, name = 'Authors'),
    path('Publisher/', views.publishers, name = 'Publisher'),
    path('Books/', views.books, name = 'Books'),
    path('BookQuery', views.bookquery, name = 'BookQuery'),

    path('authors/<str:author_name>/books/', views.author_books, name='author_books'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),

    path('add_book/', views.add_book, name='add_book'),  # URL for adding books
    path('buy/<int:book_id>/', views.buy_book, name='buy_book'),
    path('purchased-books/', views.purchased_books, name='purchased_books'),
]
