from django.contrib import admin


# Register your models here.
from .models import Customer
from .models import Mechanic
from .models import Request
from .models import Feedback

admin.site.register(Customer)
admin.site.register(Mechanic)
admin.site.register(Request)
admin.site.register(Feedback)
