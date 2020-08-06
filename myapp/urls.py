from django.urls import path
app_name="myapp"
from myapp import views
urlpatterns=[
    path('profile/',views.profile,name="profile"),
]