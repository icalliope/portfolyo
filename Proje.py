from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout,
    QStackedWidget, QCalendarWidget, QTextEdit, QMessageBox, QComboBox,
    QListWidget, QHBoxLayout, QCheckBox, QScrollArea, QGroupBox
)
from PyQt5.QtCore import QTimer
import sys
import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("veritabani.db")
c = conn.cursor()
c.execute(""" 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
""")
c.execute("""
    CREATE TABLE IF NOT EXISTS yemek_kaydi (
        user_id INTEGER,
        tarih TEXT,
        sabah TEXT,
        ogle TEXT,
        aksam TEXT
    )
""")
c.execute("""
    CREATE TABLE IF NOT EXISTS egzersiz_kaydi (
        user_id INTEGER,
        tarih TEXT,
        egzersiz TEXT
    )
""")
conn.commit()


def show_message(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec_()


class GirisEkrani(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.kullanici_adi = ""
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Beslenme ve Egzersiz Takip Uygulaması")
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Beslenme ve Egzersiz Takip Uygulamasına Hoş Geldiniz")
        self.label.setObjectName("baslikLabel")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("E-posta")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Şifre")
        self.login_button = QPushButton("Giriş Yap")
        self.register_button = QPushButton("Üye Ol")

        self.login_button.clicked.connect(self.giris_yap)
        self.register_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

    def giris_yap(self):
        email = self.email_input.text()
        password = self.password_input.text()
        c.execute("SELECT id, name FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        if user:
            self.stacked_widget.widget(2).user_id = user[0]
            self.stacked_widget.widget(2).user_name = user[1]
            self.stacked_widget.widget(2).guncelle_mesaj()
            self.stacked_widget.setCurrentIndex(2)
        else:
            show_message("E-posta veya şifre yanlış!")


class UyeOlEkrani(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("İsim Soyisim")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("E-posta")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.register_button = QPushButton("Kaydol")
        self.register_button.clicked.connect(self.kayit_ol)

        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

    def kayit_ol(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        try:
            c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            show_message("Kayıt başarılı! Giriş yapabilirsiniz.")
            self.stacked_widget.setCurrentIndex(0)
        except sqlite3.IntegrityError:
            show_message("Bu e-posta zaten kayıtlı!")



class AnaMenu(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.user_id = None
        self.user_name = None
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Beslenme ve Egzersiz Takip Uygulamasına Hoş Geldiniz")
        self.yemek_button = QPushButton("Yemek Kaydı")
        self.egzersiz_button = QPushButton("Egzersiz Kaydı")
        self.haftalik_button = QPushButton("Haftalık Takip")
        self.motivasyon_button = QPushButton("Motivasyon Kartları")

        self.yemek_button.clicked.connect(self.yemek_penceresi_ac)
        self.egzersiz_button.clicked.connect(self.egzersiz_penceresi_ac)
        self.haftalik_button.clicked.connect(self.haftalik_penceresi_ac)
        self.motivasyon_button.clicked.connect(self.motivasyon_penceresi_ac)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.yemek_button)
        layout.addWidget(self.egzersiz_button)
        layout.addWidget(self.haftalik_button)
        layout.addWidget(self.motivasyon_button)
        self.setLayout(layout)

    def guncelle_mesaj(self):
        if self.user_name:
            self.label.setText(f"Merhaba {self.user_name}, Beslenme ve Egzersiz Takip Uygulamasına Hoş Geldin!")
            self.label.setObjectName("merhabaLabel")
        else:
            self.label.setText("Beslenme ve Egzersiz Takip Uygulamasına Hoş Geldin!")

    def yemek_penceresi_ac(self):
        self.yemek_pencere = YemekKaydi(self)
        self.yemek_pencere.setWindowTitle("Yemek Kaydı")
        self.yemek_pencere.resize(600, 600)
        self.yemek_pencere.show()

    def egzersiz_penceresi_ac(self):
        self.egzersiz_pencere = EgzersizKaydi(self)
        self.egzersiz_pencere.setWindowTitle("Egzersiz Kaydı")
        self.egzersiz_pencere.resize(600, 600)
        self.egzersiz_pencere.show()

    def haftalik_penceresi_ac(self):
        self.haftalik_pencere = HaftalikTakip(self)
        self.haftalik_pencere.setWindowTitle("Haftalık Takip")
        self.haftalik_pencere.resize(600, 600)
        self.haftalik_pencere.show()

    def motivasyon_penceresi_ac(self):
        self.motivasyon_pencere = MotivasyonKartlari()
        self.motivasyon_pencere.setWindowTitle("Motivasyon Kartları")
        self.motivasyon_pencere.resize(500, 300)
        self.motivasyon_pencere.show()


class YemekKaydi(QWidget):
    def __init__(self, ana_menu):
        super().__init__()
        self.ana_menu = ana_menu
        self.init_ui()

    def init_ui(self):
        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(350, 270)

        self.sabah_input = QTextEdit()
        self.ogle_input = QTextEdit()
        self.aksam_input = QTextEdit()
        self.kaydet_button = QPushButton("Kaydet")
        self.kaydet_button.clicked.connect(self.kaydet)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(QLabel("Sabah"))
        layout.addWidget(self.sabah_input)
        layout.addWidget(QLabel("Öğle"))
        layout.addWidget(self.ogle_input)
        layout.addWidget(QLabel("Akşam"))
        layout.addWidget(self.aksam_input)
        layout.addWidget(self.kaydet_button)
        self.setLayout(layout)

    def kaydet(self):
        tarih = self.calendar.selectedDate().toString("yyyy-MM-dd")
        sabah = self.sabah_input.toPlainText()
        ogle = self.ogle_input.toPlainText()
        aksam = self.aksam_input.toPlainText()

        c.execute("SELECT * FROM yemek_kaydi WHERE user_id=? AND tarih=?", (self.ana_menu.user_id, tarih))
        mevcut_kayit = c.fetchone()

        if mevcut_kayit:
            c.execute("""UPDATE yemek_kaydi SET sabah=?, ogle=?, aksam=? WHERE user_id=? AND tarih=?""",
                      (sabah, ogle, aksam, self.ana_menu.user_id, tarih))
            show_message("Mevcut kayıt güncellendi!")
        else:
            c.execute("INSERT INTO yemek_kaydi (user_id, tarih, sabah, ogle, aksam) VALUES (?, ?, ?, ?, ?)",
                      (self.ana_menu.user_id, tarih, sabah, ogle, aksam))
            show_message("Yemek kaydı başarıyla kaydedildi!")

        conn.commit()


class EgzersizKaydi(QWidget):
    def __init__(self, ana_menu):
        super().__init__()
        self.ana_menu = ana_menu
        self.init_ui()

    def init_ui(self):
        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(350, 270)

        self.egzersiz_listesi = [
            "Tricep Cable Rope Push / Pull Downs",
            "Standing Bicep Cable Curls",
            "Weighted Bench Dips",
            "Chair / Bench Tricep Dips",
            "Dumbbell Bicep Reverse Curls",
            "Barbell Bench Press / Chest Press",
            "Push-ups",
            "Butterflies / Pec Deck / Seated Machine Flyes",
            "Hammer Strength Machine / Seated Chest Press",
            "Standing Cable Chest Press",
            "Machine Seated Shoulder Press",
            "Seated Dual / Front Raises",
            "Seated Lateral / Side Shoulder Dumbbell Raises",
            "Upright Dumbbell Rows",
            "Barbell Squat",
            "Walking Lunge",
            "Leg Press",
            "Romanian Deadlift",
            "Hip Thrust",
            "Bulgarian Split Squat",
            "Abdominal Crunch",
            "Legs Up Crunch",
            "Lying Leg Raise",
            "Plank",
            "Bicycle Crunch",
            "Weighted Crunch",
            "Bodyweight Squat",
            "Goblet Squat",
            "Sumo Squat",
            "Jump Squat",
            "Overhead Squat"
        ]

        self.egzersiz_checkboxlar = [QCheckBox(e) for e in self.egzersiz_listesi]
        scroll_area = QScrollArea()
        group = QGroupBox()
        vbox = QVBoxLayout()
        for checkbox in self.egzersiz_checkboxlar:
            vbox.addWidget(checkbox)
        group.setLayout(vbox)
        scroll_area.setWidget(group)
        scroll_area.setWidgetResizable(True)

        self.kaydet_button = QPushButton("Kaydet")
        self.kaydet_button.clicked.connect(self.kaydet)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tarih Seçin:"))
        layout.addWidget(self.calendar)
        layout.addWidget(QLabel("Egzersiz Seçin:"))
        layout.addWidget(scroll_area)
        layout.addWidget(self.kaydet_button)
        self.setLayout(layout)

    def kaydet(self):
        tarih = self.calendar.selectedDate().toString("yyyy-MM-dd")
        secilenler = [cb.text() for cb in self.egzersiz_checkboxlar if cb.isChecked()]

        if secilenler:
            egzersiz = ", ".join(secilenler)
            c.execute("SELECT * FROM egzersiz_kaydi WHERE user_id=? AND tarih=?", (self.ana_menu.user_id, tarih))
            mevcut_kayit = c.fetchone()

            if mevcut_kayit:
                c.execute("UPDATE egzersiz_kaydi SET egzersiz=? WHERE user_id=? AND tarih=?",
                          (egzersiz, self.ana_menu.user_id, tarih))
                show_message("Mevcut kayıt güncellendi!")
            else:
                c.execute("INSERT INTO egzersiz_kaydi (user_id, tarih, egzersiz) VALUES (?, ?, ?)",
                          (self.ana_menu.user_id, tarih, egzersiz))
                show_message("Egzersiz kaydı başarıyla kaydedildi!")
            conn.commit()
        else:
            show_message("Lütfen en az bir egzersiz seçin!")


class HaftalikTakip(QWidget):
    def __init__(self, ana_menu):
        super().__init__()
        self.ana_menu = ana_menu
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Haftalık Takip")

        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(350, 270)

        self.goster_button = QPushButton("Haftalık Verileri Göster")
        self.liste = QListWidget()

        self.goster_button.clicked.connect(self.haftalik_verileri_goster)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tarih Seçin:"))
        layout.addWidget(self.calendar)
        layout.addWidget(self.goster_button)
        layout.addWidget(self.liste)
        self.setLayout(layout)

    def haftalik_verileri_goster(self):
        self.liste.clear()
        secilen_tarih = self.calendar.selectedDate().toPyDate()
        user_id = self.ana_menu.user_id

        for i in range(7):
            gun = secilen_tarih - timedelta(days=i)
            tarih_str = gun.strftime("%Y-%m-%d")

            self.liste.addItem(f"--- {tarih_str} ---")

            c.execute("SELECT sabah, ogle, aksam FROM yemek_kaydi WHERE user_id=? AND tarih=?", (user_id, tarih_str))
            yemek = c.fetchone()
            if yemek:
                sabah, ogle, aksam = yemek
                self.liste.addItem(f"  Sabah: {sabah}")
                self.liste.addItem(f"  Öğle: {ogle}")
                self.liste.addItem(f"  Akşam: {aksam}")
            else:
                self.liste.addItem("  Yemek verisi yok.")


            c.execute("SELECT egzersiz FROM egzersiz_kaydi WHERE user_id=? AND tarih=?", (user_id, tarih_str))
            egzersizler = c.fetchall()
            if egzersizler:
                for egzersiz in egzersizler:
                    self.liste.addItem(f"  Egzersiz: {egzersiz[0]}")
            else:
                self.liste.addItem("  Egzersiz verisi yok.")

            self.liste.addItem("")


class MotivasyonKartlari(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Motivasyon Kartları")
        self.setFixedSize(500, 200)
        self.init_ui()

    def init_ui(self):
        self.kartlar = [
            "Zafer, zafer benimdir diyebilenindir. Başarı ise “başaracağım” diye başlayarak sonunda “başardım” diyenindir. (Mustafa Kemal Atatürk)",
            "Sadece sınırlarını aşmanın riskini alanlar ne kadar ileri gidebildiklerini görürler. (T.S. Elliot)",
            "Spor yapmak kraldır. Beslenme ise kraliçedir. İkisini bir araya koyarsanız ise bir krallığınız olur. (Jack LaLanne)",
            "Öne geçmenin sırrı, başlamaktır. (Mark Twain)",
            "Girmeye korktuğun mağara, umduğun hazineyi saklıyor olabilir. (Joseph Campbell)",
            "Dünden ders çıkar, bugünü yaşa, yarın için umut et! (Albert Einstein)",
            "İnsan, sınırlarını zorladıkça gelişir. (Albert Einstein)",
            "Şayet bir gün çaresiz kalırsanız, bir kurtarıcı beklemeyin.Kurtarıcı kendiniz olun. (Mustafa Kemal Atatürk)"
        ]

        self.label = QLabel("")
        self.label.setWordWrap(True)
        self.label.setStyleSheet("font-size: 14px; padding: 10px;")

        self.buton = QPushButton("Kart Çek")
        self.buton.setStyleSheet("font-size: 16px; padding: 8px;")
        self.buton.clicked.connect(self.rastgele_kart_goster)

        layout = QVBoxLayout()
        layout.addWidget(self.buton)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def rastgele_kart_goster(self):
        kart = random.choice(self.kartlar)
        self.label.setText(kart)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    with open("stil.qss", "r") as file:
        app.setStyleSheet(file.read())
        
    giris_ekrani = GirisEkrani(stacked_widget)
    uye_ol_ekrani = UyeOlEkrani(stacked_widget)
    ana_menu = AnaMenu(stacked_widget)

    stacked_widget.addWidget(giris_ekrani)
    stacked_widget.addWidget(uye_ol_ekrani)
    stacked_widget.addWidget(ana_menu)

    stacked_widget.setFixedWidth(600)
    stacked_widget.setFixedHeight(600)
    stacked_widget.setCurrentIndex(0)

    stacked_widget.show()
    sys.exit(app.exec_())
