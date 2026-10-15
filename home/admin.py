from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1  # تعداد سطر خالی اولیه برای افزودن آیتم

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'receiver', 'date', 'status', 'final_amount']
    list_filter = ['status', 'date']
    search_fields = ['invoice_number', 'receiver', 'sender']
    inlines = [InvoiceItemInline]

# نیازی به ثبت جداگانه InvoiceItem نیست چون از طریق Inline داخل Invoice مدیریت میشه