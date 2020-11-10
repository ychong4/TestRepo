from django.urls import path
from . import views
app_name = 'pets'
urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('<slug:category_slug>/', views.pet_list,
         name='pet_list_by_category'),
    path('<int:id>/<slug:slug>/', views.pet_detail,
         name='pet_detail'),
    path('pets/about_us/', views.about_us, name='about_us'),
    path('pets/donate/', views.donate, name='donate'),
]