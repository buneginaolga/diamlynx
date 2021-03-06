from django.contrib import admin

# Register your models here.

from stock.models import Stock, Currency

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name", "description")
    pass
    
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass