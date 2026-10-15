from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

# یک دیکشنری برای تبدیل اعداد انگلیسی به فارسی
english_to_persian_digits = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

@register.filter
def persian_intcomma(value):
    # اضافه کردن کاما و تبدیل اعداد انگلیسی به فارسی
    return intcomma(value).translate(english_to_persian_digits)

@register.filter
def persian_int(value):
    value_str = str(value)
    # تبدیل اعداد انگلیسی به فارسی
    return value_str.translate(english_to_persian_digits)

