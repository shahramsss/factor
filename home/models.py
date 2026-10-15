from django.db import models

class Invoice(models.Model):
    # اطلاعات هدر فاکتور
    invoice_number = models.CharField(max_length=50, unique=True, verbose_name="شماره فاکتور")
    date = models.DateField(verbose_name="تاریخ صدور")
    sender = models.CharField(max_length=200, verbose_name="از طرف (فروشنده)")
    receiver = models.CharField(max_length=200, verbose_name="به فلان (خریدار)")
    
    # فیلدهای محاسباتی و تکمیلی
    discount = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name="تخفیف کل")
    tax = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name="مالیات")
    
    # توضیحات و وضعیت
    status = models.CharField(
        max_length=20, 
        choices=[('paid', 'پرداخت شده'), ('unpaid', 'پرداخت نشده')], 
        default='unpaid', 
        verbose_name="وضعیت"
    )
    notes = models.TextField(blank=True, null=True, verbose_name="توضیحات فاکتور")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد سیستمی")

    def __str__(self):
        return f"فاکتور شماره {self.invoice_number} - {self.receiver}"

    # متد برای محاسبه جمع کل اقلام (Subtotal)
    @property
    def subtotal(self):
        return sum(item.total_price for item in self.items.all())

    # متد برای محاسبه مبلغ نهایی قابل پرداخت
    @property
    def final_amount(self):
        return self.subtotal - self.discount + self.tax


class InvoiceItem(models.Model):
    # ارتباط با فاکتور اصلی
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items', verbose_name="فاکتور")
    
    # جزئیات آیتم
    description = models.CharField(max_length=255, verbose_name="شرح کالا / خدمت")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    unit_price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="فی (قیمت واحد)")

    def __str__(self):
        return f"{self.description} ({self.quantity} عدد)"

    # محاسبه قیمت کل سطر (تعداد * فی) به صورت پویا
    @property
    def total_price(self):
        return self.quantity * self.unit_price