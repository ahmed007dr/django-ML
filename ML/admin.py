from django.contrib import admin

# Register your models here.
from .models import Iris

class  IrisAdmin(admin.ModelAdmin):
    list_display = ('classifiction','sepal_length', 'sepal_width','petal_length','petal_width')
    list_filter = ['classifiction']
    
admin.site.register(Iris, IrisAdmin)
