from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from AnaCafe.userApp.views import SignUpView
from . import settings

# if I should comment what is below here, I won't be able to acess the admin page on my browser
urlpatterns = [
    path("admin/", admin.site.urls),
    # The next line of code is what made it possible to view my template instead of djnago installation page
    path('', TemplateView.as_view(template_name='index.html'), name='homepage'),
    path('drinks/', TemplateView.as_view(template_name='drinks.html'), name='drinks'),
    path('food/', TemplateView.as_view(template_name='food.html'), name='food'),
    path('bakery/', TemplateView.as_view(template_name='bakery.html'), name='bakery'),
    path('protein/', TemplateView.as_view(template_name='protein.html'), name='protein'),
    # it's inside this link below we have access to django login, logout, reset password, set password etc
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    # signup link is different from login and the rest
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name="signup"),
]
