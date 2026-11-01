from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1  # تعداد فرم‌های خالی پیش‌فرض برای افزودن آیتم جدید

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'date', 'sender', 'receiver', 'status', 'final_amount')
    list_filter = ('status', 'date')
    search_fields = ('invoice_number', 'sender', 'receiver', 'receiver_national_id')
    
    # گروه‌بندی فیلدها در پنل ادمین برای نظم بیشتر
    fieldsets = (
        ('اطلاعات اصلی فاکتور', {
            'fields': ('invoice_number', 'date', 'status', 'notes')
        }),
        ('اطلاعات فروشنده و بانکی', {
            'fields': ('sender', 'card_number', 'account_number')
        }),
        ('اطلاعات خریدار', {
            'fields': ('receiver', 'receiver_national_id', 'receiver_address')
        }),
        ('محاسبات مالی', {
            'fields': ('discount', 'tax')
        }),
    )
    
    inlines = [InvoiceItemInline]

# اگر خواستید InvoiceItem رو به صورت جداگانه هم در ادمین داشته باشید (اختیاری)
@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'quantity', 'unit_price', 'total_price')
    search_fields = ('description', 'invoice__invoice_number')