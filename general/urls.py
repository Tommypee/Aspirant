from django.urls import path
from general.views import *
from contact.views import contact, wacepage, new_candidate

urlpatterns = [
    path('', homepage, name='index'),
    path('about', about_us, name='about'),
    path('contact', contact, name='contact'),
    path('service', service, name='service'),
    path('portfolio', portfolio, name='portfolio'),
    path('login', login_page, name='login'),
    path('logout', logout_page, name='logout_page'),
    path('dashboard', dashboard, name='dashboard'),
    path('register', register, name='register'),
    path('app_candidates/myolevel', wacepage, name='C_homepage'),
    path('add-new-student', new_candidate, name='add_candidates'),
]
