from django.urls import path
from .views import *

urlpatterns = [
    path('list/', List.as_view(), name='list'),
    path('pub-<str:uri>/', Pub.as_view(), name='pub'),
    path('', Add.as_view(), name='add'),
]
