
from django.contrib import admin
from django.urls import path
from Asignaciones import views

#   Se crean las diferentes urls para acceder a cada una de las vistas

urlpatterns = [


    path('ingresaradmin/', admin.site.urls),
    path('verasignacion/',views.verAsignacion),
    path('dashboard/',views.mostrarDashboard),
    path('nav/', views.mostrarNav),
    path('realizarasignaciones/',views.realizarAsignacion)
]