from django import forms
from .models import CaseiUser, UserTipo, Documento
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class RegistrarUsuarioForm(forms.ModelForm):
    TIPOS_USUARIO = (
        (None, 'Seleccione una opción'),
        ('tutor', 'Tutor'),
        ('estudiante', 'Estudiante'),
        ('coordinador', 'Coordinador')
        )
    
    tipo_user = forms.ChoiceField(choices=TIPOS_USUARIO)
    
    class Meta:
        model = CaseiUser
        fields = ['nombre', 'email', 'telefono', 'username', 'password']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Roberto Mariano García Perez'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ej. sus_prz@....com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 4921234567'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Roberto1234'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        } 
        
    def save(self, commit=True):
        user = super().save(commit=False)
        tipo_usuario = self.cleaned_data['tipo_user']
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
            # Revisa si ya existe un UserTipo asociado y actualízalo o crea uno nuevo si no existe
            user_tipo, created = UserTipo.objects.update_or_create(
                caseiuser=user, 
                defaults={'tipoUser': tipo_usuario}
            )
        return user
#Form para el login de usuarios
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Usuario o contraseña incorrectos")
        return cleaned_data
   

class NotificacionForm(forms.Form):
    TIPOS_USUARIO = (
        (None, 'Seleccione una opción'),
        ('tutor', 'Tutor'),
        ('coordinador', 'Coordinador'),
        ('estudiante', 'Estudiante'),
        ('todos', 'Todos los usuarios'),
        )
    
    asunto = forms.CharField(max_length=50)
    mensaje = forms.CharField(widget=forms.Textarea)
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIO)

#Form para el documento de actitidades    
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('nombre', 'archivo',)

class SolicitudCambioActividadesForm(forms.Form):
    asunto = forms.CharField(max_length=100, label='Asunto')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')
    estudiante = forms.ModelChoiceField(queryset=CaseiUser.objects.filter(usertipo__tipoUser='estudiante'), label='Estudiante')