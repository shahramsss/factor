from django.contrib import admin
from .models import Invoice, InvoiceItem

# class InvoiceItemInline(admin.TabularInline):
#     model = InvoiceItem
#     extra = 1  # تعداد سطر خالی اولیه برای افزودن آیتم

# @admin.register(Invoice)
# class InvoiceAdmin(admin.ModelAdmin):
#     list_display = ['invoice_number', 'receiver', 'date', 'status', 'final_amount']
#     list_filter = ['status', 'date']
#     search_fields = ['invoice_number', 'receiver', 'sender']
#     inlines = [InvoiceItemInline]

# # نیازی به ثبت جداگانه InvoiceItem نیست چون از طریق Inline داخل Invoice مدیریت میشه

from django.contrib import admin
from .models import Invoice, InvoiceItem


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1
    fields = (
        "description",
        "quantity",
        "unit_price",
    )


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "invoice_number",
        "date",
        "sender",
        "receiver",
        "subtotal_display",
        "discount",
        "tax",
        "final_amount_display",
        "status",
    )

    list_filter = (
        "status",
        "date",
        "created_at",
    )

    search_fields = (
        "invoice_number",
        "sender",
        "receiver",
    )

    list_display_links = (
        "invoice_number",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "created_at",
        "subtotal_display",
        "final_amount_display",
    )

    fieldsets = (
        ("اطلاعات اصلی فاکتور", {
            "fields": (
                "invoice_number",
                "date",
                "sender",
                "receiver",
            )
        }),
        ("اطلاعات مالی", {
            "fields": (
                "discount",
                "tax",
                "subtotal_display",
                "final_amount_display",
            )
        }),
        ("وضعیت و توضیحات", {
            "fields": (
                "status",
                "notes",
            )
        }),
        ("اطلاعات سیستمی", {
            "fields": (
                "created_at",
            ),
            "classes": ("collapse",),
        }),
    )

    inlines = [InvoiceItemInline]

    @admin.display(description="جمع اقلام")
    def subtotal_display(self, obj):
        if obj is None:
            return "—"
        return f"{obj.subtotal:,.0f} تومان"

    @admin.display(description="مبلغ نهایی")
    def final_amount_display(self, obj):
        if obj is None:
            return "—"
        return f"{obj.final_amount:,.0f} تومان"


@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "invoice",
        "quantity",
        "unit_price",
        "total_price_display",
    )

    search_fields = (
        "description",
        "invoice__invoice_number",
        "invoice__receiver",
    )

    list_filter = (
        "invoice__status",
        "invoice__date",
    )

    @admin.display(description="قیمت کل")
    def total_price_display(self, obj):
        return f"{obj.total_price:,.0f} تومان"
