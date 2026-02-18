# todos/admin.py
from django.contrib import admin


  #todos.models იგივეა რაც .models
from .models import Todo

admin.site.register(Todo)



