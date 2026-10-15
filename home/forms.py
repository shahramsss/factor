from django import forms
from .models import Invoice, InvoiceItem
from django.forms import inlineformset_factory

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'date', 'sender', 'receiver', 'discount', 'tax', 'status', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'sender': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'tax': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# فرم‌ست برای مدیریت همزمان آیتم‌های فاکتور همراه با خود فاکتور
InvoiceItemFormSet = inlineformset_factory(
    Invoice, 
    InvoiceItem, 
    fields=['description', 'quantity', 'unit_price'],
    extra=1,  # تعداد سطر خالی اولیه برای ثبت آیتم جدید
    can_delete=True # امکان حذف آیتم از طریق فرم
)