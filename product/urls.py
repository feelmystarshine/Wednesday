from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('', views.items, name="items"),
    path('check/<str:id>', views.check, name ="check"),
     path('buy/<str:id>', views.buy, name ="buy")
]