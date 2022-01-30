from django.urls import path , include
from . import views
from . import api

urlpatterns = [
    path('',views.Home_list),
    path('<int:id>',views.Home_details),
    path('api/list',api.Home_listAPI),

]