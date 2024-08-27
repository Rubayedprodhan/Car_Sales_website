from django.urls import path,include
from . import views
urlpatterns = [

    path('singup/',views.RegisterView.as_view() ,name='singup'  ),
    path('loging/',views.UserLoginView.as_view() ,name='loging'  ),
    path('logout/',views.user_logout ,name='logout'),



]
