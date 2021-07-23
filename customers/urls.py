from django.urls import path
from customers import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path(actionUrl, views.make_thumbnail),
]
