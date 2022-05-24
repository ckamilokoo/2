from dataclasses import fields
from django import forms
from .models import Contacto ,notificacion,residente,reserva,area,estado_cuenta,pago_estado,pago_reserva

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'
        

class NotificacionForm(forms.ModelForm):
    
    class Meta:
        model = notificacion
        fields = '__all__'
            
class ResidenteForm(forms.ModelForm):
    
    class Meta:
        model = residente
        fields = '__all__'
        
        
class Pago_reservaForm(forms.ModelForm):
    
    class Meta:
        model = pago_reserva
        fields = '__all__'
        
class Pago_estadoForm(forms.ModelForm):
    
    class Meta:
        model = pago_estado
        fields = '__all__'

class Estado_cuentaForm(forms.ModelForm):
    
    class Meta:
        model = estado_cuenta
        fields = '__all__'

class AreaForm(forms.ModelForm):
    
    class Meta:
        model = area
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = reserva
        fields = '__all__'