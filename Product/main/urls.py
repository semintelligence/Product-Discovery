from django.urls import path
from main import views

urlpatterns = [
    path("", views.main ,name="main"),
    path("search/",views.index,name="index"),
    path("detail/<str:ModelNumber>",views.detail,name="detail"),
    path("sparql/",views.sparql,name="sparql"),
    path("login/",views.login,name="login"),
]