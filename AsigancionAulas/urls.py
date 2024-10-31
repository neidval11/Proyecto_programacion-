from django.contrib import admin
from django.urls import path, include
from Asignaciones import views

urlpatterns = [

    path('ingresaradmin/', admin.site.urls),
    path('verasignacion/',views.verAsignacion),
    path('dashboard/',views.mostrarDashboard),
    path('nav/', views.mostrarNav),
    path('realizarasignaciones/',views.realizarAsignacion)

]