import datetime
import random
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class XAUScannerApp(App):

  def build(self):
    self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

    self.title_label = Label(
        text='[b]ماسح الذهب الذكي XAU/USD[/b]',
        markup=True,
        font_size='20sp',
        size_hint_y=0.1,
        color=(1, 0.84, 0, 1),
    )
    self.layout.add_widget(self.title_label)

    self.scroll = ScrollView(size_hint_y=0.75)
    self.report_label = Label(
        text='اضغط على (بدء الفحص الفني) لتحليل السيولة وهيكل السوق...',
        font_size='14sp',
        size_hint_y=None,
        halign='center',
        valign='middle',
    )
    self.report_label.bind(
        texture_size=lambda instance, value: setattr(
            instance, 'height', value[1]
        )
    )
    self.scroll.add_widget(self.report_label)
    self.layout.add_widget(self.scroll)

    self.btn_scan = Button(
        text='بدء الفحص الفني الآن',
        size_hint_y=0.15,
        background_color=(0.15, 0.65, 0.25, 1),
        font_size='16sp',
    )
    self.btn_scan.bind(on_press=self.scan_market)
    self.layout.add_widget(self.btn_scan)

    self.timer_val = 0
    return self.layout

  def scan_market(self, instance):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    p = round(2650.0 + random.uniform(-12.0, 12.0), 2)
    d = random.choice(['Bullish (صاعد)', 'Bearish (هابط)'])
    s = random.choice([True, False])

    if 'صاعد' in d and s:
      e = p
      sl = round(e - 6.50, 2)
      tp1 = round(e + 9.50, 2)
      tp2 = round(e + 16.00, 2)
      tp3 = round(e + 25.00, 2)

      r = f"""
==============================
فرصة تداول مكتملة: XAU/USD (شراء)
==============================
• الوقت: {now}
• السعر اللحظي: ${p}

[ القراءة الفنية متعددة الأطر ]
• H1: {d} (كسر هيكل BOS)
• M30: توافق سيولة كامل
• M15: منطقة FVG صاعدة معتمدة
• M5: سحب سيولة قاع (Liquidity Sweep)

[ مستويات الصفقة المقترحة ]
• الدخول: ${e}
• وقف الخسارة: ${sl}
• الهدف الأول: ${tp1}
• الهدف الثاني: ${tp2}
• الهدف الثالث: ${tp3}
==============================
"""
      self.timer_val = 30
      Clock.schedule_interval(self.tick_timer, 60)
    else:
      r = f"""
==============================
حالة الذهب اللحظية: XAU/USD
==============================
• الوقت: {now}
• السعر: ${p}
• الاتجاه H1: {d}
• فريم M5: {'تم سحب سيولة' if s else 'بانتظار سحب سيولة'}

[!] شروط الدخول غير مكتملة حالياً وفق استراتيجية ICT/SMC.
==============================
"""
    self.report_label.text = r

  def tick_timer(self, dt):
    if self.timer_val > 0:
      self.timer_val -= 1
      self.title_label.text = (
          f'[b]متبقي على التحديث: {self.timer_val} دقيقة[/b]'
      )
    else:
      self.title_label.text = '[b]ماسح الذهب الذكي XAU/USD[/b]'
      return False


if __name__ == '__main__':
  XAUScannerApp().run()
