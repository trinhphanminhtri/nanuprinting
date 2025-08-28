from django.contrib import admin

# Register your models here.
from .models import ExampleModel  # Replace ExampleModel with your actual model name
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Adjust fields as necessary
    
admin.site.register(ExampleModel,ExampleModelAdmin)  # Replace ExampleModel with your actual model name