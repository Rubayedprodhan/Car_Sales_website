from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('profile/', views.profile_view, name=''),
    path('car/<int:id>/', views.car_details, name='car_detail'),
    path('buy/<int:id>/', views.car_buy, name='car_buy'),
    path('orders/', views.order_history, name='profile'),
 
    path('orders/', views.order_history, name='profile'),
    path('orders/edit_profile/', views.EditProfileView.as_view(), name='edit'),
    path('orders/pass_change/', views.PassChangeView.as_view(), name='pass_change')



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
