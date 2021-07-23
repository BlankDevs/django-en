from django.urls import path
from customers import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # url for image manipulator using pillow
    # path(actionUrl, views.manipulator),

    # url for the labeler's date picking
    # path(actionUrl, views.labeler_dates)
]
