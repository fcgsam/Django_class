from django.urls import path
from . import views              #from views import home_page

urlpatterns = [
    path('',views.home_page,name='home'),
]