from django.urls import path
from .views import IndexView, HomePage, AboutUs, SearchDatabase, loginUser, AddCar, registration, userLogOut, LogHomePage, LogAddCar, LogAboutUs, LogSearchDatabase

app_name = 'auto'

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('home/', HomePage.as_view(), name = 'home'),
    path('aboutus/', AboutUs.as_view(), name = 'aboutus'),
    path('searchdatabase/', SearchDatabase.as_view(), name = 'searchdatabase'),
    path('login/', loginUser , name = 'login'),
    path('logout/', userLogOut , name = 'logout'),
    path('addcar/', AddCar.as_view(), name = 'addcar'),
    path('registration/', registration, name = 'registration'),
    path('loghome/', LogHomePage.as_view(), name = 'loghome'),
    path('logaboutus/', LogAboutUs.as_view(), name = 'logaboutus'),
    path('logsearchdatabase/', LogSearchDatabase.as_view(), name = 'logsearchdatabase'),
    path('logaddcar/', LogAddCar.as_view(), name = 'addcar'),
]