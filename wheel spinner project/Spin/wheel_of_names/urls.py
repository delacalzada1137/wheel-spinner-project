
from django.urls import path
from .views import pick_winner, save_name_view

urlpatterns = [
    # path('', pick_winner, name='pick_winner'),
    path('', save_name_view, name='save_name')
]
