# -*- coding: utf-8 -*-
import io
import os
import json
import contextlib

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.core.window import Window

from lessons import LESSONS
from rtl import fa

FONT_NAME = "Vazirmatn"
LabelBase.register(name=FONT_NAME, fn_regular="assets/Vazirmatn-Regular.ttf")

Window.clearcolor = (0.12, 0.12, 0.18, 1)


# ---------- ذخیره‌ی پیشرفت ----------
def _progress_path():
    base = App.get_running_app().user_data_dir
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "progress.json")


def load_progress():
    path = _progress_path()
    if not os.path.exists(path):
        return {"completed": []}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"completed": []}


def mark_completed(lesson_id):
    data = load_progress()
    if lesson_id not in data["completed"]:
        data["completed"].append(lesson_id)
    with open(_progress_path(), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return data


# ---------- ویجت‌های کمکی ----------
def fa_label(text, **kwargs):
    kwargs.setdefault("font_name", FONT_NAME)
    kwargs.setdefault("halign", "right")
    kwargs.setdefault("valign", "top")
    lbl = Label(text=fa(text), **kwargs)
    lbl.bind(size=lambda inst, val: setattr(inst, "text_size", (val[0], None)))
    return lbl


def fa_button(text, **kwargs):
    kwargs.setdefault("font_name", FONT_NAME)
    return Button(text=fa(text), **kwargs)


def nav_bar(manager):
    bar = BoxLayout(size_hint_y=None, height=dp(56), spacing=dp(4), padding=dp(4))
    items = [("خانه", "home"), ("آموزش", "lessons"), ("تمرین", "exercises"), ("پیشرفت", "progress")]
    for label, screen_name in items:
        btn = fa_button(label)
        btn.bind(on_release=lambda inst, s=screen_name: setattr(manager, "current", s))
        bar.add_widget(btn)
    return bar


# ---------- صفحه‌ی خانه ----------
class HomeScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation="vertical")
        content = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))
        content.add_widget(Widget())
        title = fa_label("به Python Learn خوش اومدی", font_size=dp(24), halign="center", size_hint_y=None, height=dp(50))
        subtitle = fa_label("از پایین، آموزش یا تمرین رو انتخاب کن.", font_size=dp(16), halign="center", size_hint_y=None, height=dp(40))
        content.add_widget(title)
        content.add_widget(subtitle)
        content.add_widget(Widget())
        root.add_widget(content)
        root.add_widget(nav_bar(manager))
        self.add_widget(root)


# ---------- صفحه‌ی آموزش ----------
class LessonsScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.manager_ref = manager
        self.root_box = BoxLayout(orientation="vertical")
        self.body = BoxLayout(orientation="vertical")
        self.root_box.add_widget(self.body)
        self.root_box.add_widget(nav_bar(manager))
        self.add_widget(self.root_box)
        self.show_list()

    def show_list(self):
        self.body.clear_widgets()
        scroll = ScrollView()
        layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(6), padding=dp(10))
        layout.bind(minimum_height=layout.setter("height"))
        for lesson in LESSONS:
            btn = fa_button(lesson["title"], size_hint_y=None, height=dp(50))
            btn.bind(on_release=lambda inst, l=lesson: self.show_detail(l))
            layout.add_widget(btn)
        scroll.add_widget(layout)
        self.body.add_widget(scroll)

    def show_detail(self, lesson):
        self.body.clear_widgets()
        wrapper = BoxLayout(orientation="vertical")

        back_btn = fa_button("→ بازگشت به لیست درس‌ها", size_hint_y=None, height=dp(44))
        back_btn.bind(on_release=lambda inst: self.show_list())
        wrapper.add_widget(back_btn)

        scroll = ScrollView()
        content_box = BoxLayout(orientation="vertical", size_hint_y=None, padding=dp(14), spacing=dp(8))
        content_box.bind(minimum_height=content_box.setter("height"))

        title_lbl = fa_label(lesson["title"], font_size=dp(20), size_hint_y=None, height=dp(40))
        content_box.add_widget(title_lbl)

        body_lbl = fa_label(lesson["content"], font_size=dp(15), size_hint_y=None)
        body_lbl.bind(texture_size=lambda inst, val: setattr(inst, "height", val[1]))
        content_box.add_widget(body_lbl)

        scroll.add_widget(content_box)
        wrapper.add_widget(scroll)

        done_btn = fa_button("علامت‌گذاری به‌عنوان تکمیل‌شده", size_hint_y=None, height=dp(48))

        def mark(inst):
            mark_completed(lesson["id"])
            done_btn.text = fa("تکمیل شد!")

        done_btn.bind(on_release=mark)
        wrapper.add_widget(done_btn)

        self.body.add_widget(wrapper)


# ---------- صفحه‌ی تمرین ----------
class ExercisesScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.body = BoxLayout(orientation="vertical")
        root = BoxLayout(orientation="vertical")
        root.add_widget(self.body)
        root.add_widget(nav_bar(manager))
        self.add_widget(root)
        self.show_list()

    def show_list(self):
        self.body.clear_widgets()
        scroll = ScrollView()
        layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(6), padding=dp(10))
        layout.bind(minimum_height=layout.setter("height"))
        for lesson in LESSONS:
            btn = fa_button(lesson["title"], size_hint_y=None, height=dp(50))
            btn.bind(on_release=lambda inst, l=lesson: self.show_exercise(l))
            layout.add_widget(btn)
        scroll.add_widget(layout)
        self.body.add_widget(scroll)

    def show_exercise(self, lesson):
        self.body.clear_widgets()
        ex = lesson["exercise"]
        wrapper = BoxLayout(orientation="vertical", padding=dp(8), spacing=dp(8))

        back_btn = fa_button("→ بازگشت به لیست تمرین‌ها", size_hint_y=None, height=dp(44))
        back_btn.bind(on_release=lambda inst: self.show_list())
        wrapper.add_widget(back_btn)

        instr = fa_label(ex["instructions"], size_hint_y=None, height=dp(70), font_size=dp(14))
        wrapper.add_widget(instr)

        editor = TextInput(text=ex["starter_code"], font_name=FONT_NAME, size_hint_y=0.4,
                            font_size=dp(14))
        wrapper.add_widget(editor)

        output = TextInput(text="", readonly=True, font_size=dp(13), size_hint_y=0.3,
                            background_color=(0.05, 0.05, 0.05, 1), foreground_color=(0.2, 1, 0.2, 1))
        wrapper.add_widget(output)

        run_btn = fa_button("▶ اجرای کد", size_hint_y=None, height=dp(48))

        def run(inst):
            code = editor.text
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                    exec(code, {"__name__": "__main__"})
            except Exception as e:
                buf.write("\nخطا: " + str(e))
            result = buf.getvalue().strip()
            output.text = result if result else "(بدون خروجی)"

        run_btn.bind(on_release=run)
        wrapper.add_widget(run_btn)

        self.body.add_widget(wrapper)


# ---------- صفحه‌ی پیشرفت ----------
class ProgressScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.root_box = BoxLayout(orientation="vertical")
        self.body = BoxLayout(orientation="vertical", padding=dp(14), spacing=dp(6))
        self.root_box.add_widget(self.body)
        self.root_box.add_widget(nav_bar(manager))
        self.add_widget(self.root_box)

    def on_pre_enter(self):
        self.body.clear_widgets()
        data = load_progress()
        completed = set(data.get("completed", []))
        title = fa_label(f"پیشرفت شما: {len(completed)} از {len(LESSONS)} درس",
                          font_size=dp(18), size_hint_y=None, height=dp(44), halign="center")
        self.body.add_widget(title)
        scroll = ScrollView()
        layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(4))
        layout.bind(minimum_height=layout.setter("height"))
        for lesson in LESSONS:
            mark = "✅" if lesson["id"] in completed else "⬜"
            row = fa_label(f"{mark} {lesson['title']}", size_hint_y=None, height=dp(36))
            layout.add_widget(row)
        scroll.add_widget(layout)
        self.body.add_widget(scroll)


class PythonLearnApp(App):
    def build(self):
        self.title = "Python Learn"
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(HomeScreen(sm, name="home"))
        sm.add_widget(LessonsScreen(sm, name="lessons"))
        sm.add_widget(ExercisesScreen(sm, name="exercises"))
        sm.add_widget(ProgressScreen(sm, name="progress"))
        return sm


if __name__ == "__main__":
    PythonLearnApp().run()
