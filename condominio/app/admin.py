from django.contrib import admin
from .models import notificacion  ,Contacto , residente, estado_cuenta,reserva,area,pago_estado,pago_reserva
# Register your models here.
admin.site.register(notificacion)
admin.site.register(Contacto)
admin.site.register(estado_cuenta)
admin.site.register(residente)
admin.site.register(reserva)
admin.site.register(area)
admin.site.register(pago_estado)
admin.site.register(pago_reserva)
