from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin', admin.site.urls),

    path('client/<int:user_id>/cars', read_cars_view),

    path('car/create', create_car_view),
    path('car/<int:car_id>/update', update_car_view),
    path('car/<int:car_id>/delete', delete_car_view),

    path('car/<int:car_id>/service', read_service_view),
    path('car/service/create', create_service_view),

    path('service/<int:service_id>/update', update_service_view),
    path('service/<int:service_id>/delete', delete_service_view),
    path('user/register', register_view),
    path('user/login', login_view),
]
