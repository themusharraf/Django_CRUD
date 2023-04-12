from django.urls import path
from apps.views import HomeView, HomeAdd, HomeDeleteView, HomeUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', HomeAdd.as_view(), name='add_page'),
    path('delete/<int:pk>', HomeDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', HomeUpdateView.as_view(), name='update'),
]
