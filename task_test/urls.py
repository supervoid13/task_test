from django.contrib import admin
from django.urls import path
from menu import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('menus/', views.show_menus, name="main"),
    path('menus/<path:path>', views.pick_menu)
]

