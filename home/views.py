from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Invoice
from .forms import InvoiceForm, InvoiceItemFormSet


class HomeView(View):
    def get(self, request):
        return render(request, "home/home.html")


# ۱. لیست فاکتورها
class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/invoice_list.html"
    context_object_name = "invoices"
    ordering = ["-date"]


# ۲. نمایش جزئیات فاکتور
class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = "home/invoice_detail.html"
    context_object_name = "invoice"


# کلاس پایه برای مدیریت مشترک فرم و فرم‌ست (Create و Update)
class InvoiceBaseView:
    model = Invoice
    form_class = InvoiceForm
    template_name = "invoices/invoice_form.html"
    success_url = reverse_lazy("invoice_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = InvoiceItemFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context["formset"] = InvoiceItemFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


# ۳. ایجاد فاکتور جدید
class InvoiceCreateView(InvoiceBaseView, CreateView):
    object = None


# ۴. ویرایش فاکتور
class InvoiceUpdateView(InvoiceBaseView, UpdateView):
    pass


# ۵. حذف فاکتور
class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = "invoices/invoice_confirm_delete.html"
    success_url = reverse_lazy("invoice_list")
    context_object_name = "invoice"
