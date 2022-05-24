from django.urls import path
from .views import agregar_residente, eliminar_residente, home,residentes , directiva, listar_residentes, modificar_residente   , contactos , agregar_notificacion, listar_notificaciones , modificar_notificacion , eliminar_notificacion


urlpatterns = [
    path('', home,name="home"),
    path('directiva/',directiva , name="directiva"),
    path('residente/',residentes, name="residente" ),
    path('contacto/',contactos, name="contacto" ),
    path('agregar-notificacion/',agregar_notificacion, name="agregar_notificacion" ),
    path('listar-notificaciones/',listar_notificaciones,name="listar_notificaciones"),
    path('modificar-notificacion/<id>/',modificar_notificacion,name="modificar_notificacion"),
    path('eliminar-notificacion/<id>/',eliminar_notificacion,name="eliminar_notificacion"),
    path('agregar-residente/',agregar_residente, name="agregar_residente" ),
    path('listar-residente/',listar_residentes,name="listar_residentes"),
    path('modificar-residente/<id>/',modificar_residente,name="modificar_residente"),
    path('eliminar-residente/<id>/',eliminar_residente,name="eliminar_residente")
]