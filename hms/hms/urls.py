from django.contrib import admin
from django.urls import path
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),
    path('patient',views.patient_view),
    path('patient_signup', views.patient_signup)
]
