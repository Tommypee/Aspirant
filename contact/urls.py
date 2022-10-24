from django.urls import path
from contact.views import *

urlpatterns = [
    path('app_candidates/myolevel', wacepage, name='C_homepage'),
    path('add-new-student', new_candidate, name='add_candidates'),
    path('delete/<int:id>/', delete_candidate, name='delete_candidates'),
    path('update/<int:id>/', update_candidate, name='update_candidates'),
]
