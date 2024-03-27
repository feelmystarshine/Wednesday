from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path('', views.user, name="staff"),
    path("create", views.create, name = 'create'),
    path("edit/<str:id>", views.edit, name = 'edit'),
    path("delete/<str:id>", views.delete, name = 'delete')
]