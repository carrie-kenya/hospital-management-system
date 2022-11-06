from django.urls import path
from .views import index, patients, logout

urlpatterns = [    
    path('', index, name="Home"),
    path('patients', patients, name="Patients"),
    path('logout', patients, name="logout"),
]
