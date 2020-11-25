from django.url import path
from . import views

appname = "users"

urlpatterns = [path("login/", views.LoginView.as_view(), name="login")]
