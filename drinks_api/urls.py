from django.urls import path
from .views import drink_list, drink_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('drinks/', drink_list, name='drink_list'),
    path('drinks/<int:id>', drink_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)