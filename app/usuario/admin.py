from django.contrib import admin
from .models import CaseiUser, UserTipo, Documento

# Register your models here.
admin.site.register(CaseiUser)
admin.site.register(UserTipo)
admin.site.register(Documento)
