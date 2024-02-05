from django.contrib import admin
from .models import Travel,Book,Order

# Register your models here.
class TravelAdmin(admin.ModelAdmin):
    list_display=["t_id","image","place_name","price"]

class BookAdmin(admin.ModelAdmin):
    list_display=["t_id","no_people","userid","dates"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id","userid","t_id","no_people","dates"]

admin.site.register(Travel,TravelAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Order,OrderAdmin) 







