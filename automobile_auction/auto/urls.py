from django.urls import path
from .views import IndexView, HomePage, AboutUs, SearchDatabase, LogIn

app_name = 'auto'

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('home/', HomePage.as_view(), name = 'home'),
    path('aboutus/', AboutUs.as_view(), name = 'aboutus'),
    path('searchdatabase/', SearchDatabase.as_view(), name = 'searchdatabase'),
    path('login/', LogIn.as_view(), name = 'login'),
]