from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name=''),
    path('contact',views.contact,name='contact'),
    path('single',views.singlepage,name='single'),
    path('trip',views.trips1,name='trip'),
    path('Goa',views.goa,name='Goa'),
    path('kovalam',views.kovalam,name='kovalam'),
]