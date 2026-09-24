# -*- coding: utf-8 -*-
LESSONS = [
    {
        "id": "vars",
        "title": "۱. متغیرها و انواع داده",
        "content": (
            "متغیرها و انواع داده\n\n"
            "در پایتون برای ساختن متغیر کافیه یک اسم انتخاب کنی و مقدار بدی:\n\n"
            "name = \"Ali\"\nage = 20\nheight = 1.75\nis_student = True\n\n"
            "انواع اصلی داده:\n"
            "- str : رشته متنی\n- int : عدد صحیح\n- float : عدد اعشاری\n- bool : درست/نادرست\n\n"
            "برای دیدن نوع یک متغیر از type() استفاده می‌کنیم:\n"
            "print(type(age))"
        ),
        "exercise": {
            "instructions": "یک متغیر به نام city بساز و مقدار شهر خودت رو داخلش بریز، بعد با print چاپش کن.",
            "starter_code": "city = \"\"\nprint(city)\n",
        },
    },
    {
        "id": "condition",
        "title": "۲. شرط‌ها (if / else)",
        "content": (
            "شرط‌ها\n\n"
            "با if می‌تونیم بر اساس یک شرط، تصمیم بگیریم:\n\n"
            "age = 18\nif age >= 18:\n    print(\"بزرگسال هستی\")\nelse:\n    print(\"هنوز بزرگسال نیستی\")\n\n"
            "می‌تونیم چند شرط پشت سر هم بذاریم با elif:\n"
            "score = 75\nif score >= 90:\n    print(\"عالی\")\nelif score >= 60:\n    print(\"قبول\")\nelse:\n    print(\"مردود\")"
        ),
        "exercise": {
            "instructions": "یک متغیر number با مقدار دلخواه بساز و چاپ کن که زوجه یا فرده.",
            "starter_code": "number = 7\n\nif number % 2 == 0:\n    print(\"زوج\")\nelse:\n    print(\"فرد\")\n",
        },
    },
    {
        "id": "loops",
        "title": "۳. حلقه‌ها (for / while)",
        "content": (
            "حلقه‌ها\n\n"
            "حلقه for برای تکرار روی یک مجموعه استفاده می‌شه:\n"
            "for i in range(5):\n    print(i)\n\n"
            "حلقه while تا وقتی شرط برقراره ادامه پیدا می‌کنه:\n"
            "count = 0\nwhile count < 3:\n    print(count)\n    count += 1"
        ),
        "exercise": {
            "instructions": "با یک حلقه، اعداد ۱ تا ۱۰ رو چاپ کن.",
            "starter_code": "for i in range(1, 11):\n    print(i)\n",
        },
    },
    {
        "id": "functions",
        "title": "۴. توابع (Functions)",
        "content": (
            "توابع\n\n"
            "تابع بخشی از کده که یک کار مشخص انجام میده:\n"
            "def greet(name):\n    return \"سلام \" + name\n\nprint(greet(\"Ali\"))\n\n"
            "توابع می‌تونن چند ورودی بگیرن و مقدار برگردونن:\n"
            "def add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)"
        ),
        "exercise": {
            "instructions": "تابعی به نام square بنویس که یک عدد می‌گیره و مربعش رو برمی‌گردونه.",
            "starter_code": "def square(n):\n    return n * n\n\nprint(square(4))\n",
        },
    },
    {
        "id": "lists",
        "title": "۵. لیست‌ها (Lists)",
        "content": (
            "لیست‌ها\n\n"
            "لیست مجموعه‌ای مرتب از داده‌هاست:\n"
            "fruits = [\"apple\", \"banana\", \"cherry\"]\n"
            "print(fruits[0])\nfruits.append(\"kiwi\")\nprint(len(fruits))\n\n"
            "for f in fruits:\n    print(f)"
        ),
        "exercise": {
            "instructions": "لیستی از ۳ عدد بساز و مجموعشون رو چاپ کن.",
            "starter_code": "numbers = [4, 8, 15]\nprint(sum(numbers))\n",
        },
    },
]
