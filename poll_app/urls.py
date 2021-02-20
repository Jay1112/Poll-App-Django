from django.contrib import admin
from django.urls import path

from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('give_poll/<int:pk>',views.give_poll,name="give_poll"),
    path('poll_results/<int:pk>',views.poll_results,name="poll_results"),
]
