# -*- coding: utf-8 -*-
"""
Kivy به‌صورت پیش‌فرض حروف فارسی/عربی رو به هم متصل نمایش نمی‌ده (هر حرف جدا میفته).
این تابع متن فارسی رو قبل از نمایش، "شکل‌دهی" (reshape) می‌کنه تا درست و بهم‌چسبیده دیده بشه.
هر جا متن فارسی به یک ویجت Kivy (Label, Button, TextInput) داده می‌شه، باید از این تابع رد بشه.
"""
import arabic_reshaper
from bidi.algorithm import get_display

_reshaper = arabic_reshaper.ArabicReshaper(configuration={
    "delete_harakat": False,
    "support_ligatures": True,
})


def fa(text):
    """متن فارسی رو برای نمایش درست در Kivy آماده می‌کنه."""
    reshaped = _reshaper.reshape(text)
    return get_display(reshaped)
