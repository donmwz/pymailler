import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QTextEdit, QPushButton, QMessageBox, QComboBox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class kayitApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyMailler')
        self.setGeometry(650, 200, 1100, 670)
        self.setFixedSize(800, 600)

        """css/ssh"""
        self.setStyleSheet("""
            QLineEdit {
                background-color: transparent;
                border: none;
                color: black;
            }
            QTextEdit {
                background-color: transparent;
                border: none;
                color: black;
            }
            QComboBox {
                background-color: transparent;
                border: none;
                color: black;
            }           
        """)
        """css/ssh"""

        self.black_label = QLabel(" Yeni Posta", self)
        self.black_label.setGeometry(0, 0, 800, 60)
        self.black_label.setStyleSheet("""
            background-color: #1C1C1C;
            border-bottom: 1px solid #666666;
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
            color: white;
            font-size: 22px;
            font-family: 'Roboto', sans-serif;
            padding: 10px 20px;
            letter-spacing: 0.5px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        """)

        self.you_mail_label = QLabel("Gönderici E-Mail:", self)
        self.you_mail_label.setGeometry(20, 90, 150, 30)
        self.you_mail_label.setStyleSheet("color: gray;")

        self.you_mail_input = QComboBox(self)
        self.you_mail_input.addItems(["pymailler.py@gmail.com"])
        self.you_mail_input.setGeometry(120, 90, 650, 30)

        self.underlined = QLabel("_" * 700 , self)
        self.underlined.setGeometry(20, 110, 750, 15)
        self.underlined.setStyleSheet("color: gray;")

        self.recipient_mail_label = QLabel("Alıcı E-Mail:", self)
        self.recipient_mail_label.setGeometry(20, 130, 150, 30)
        self.recipient_mail_label.setStyleSheet("color: gray;")

        self.recipient_mail_input = QLineEdit(self)
        self.recipient_mail_input.setGeometry(90, 130, 680, 30)

        self.underlined = QLabel("_" * 700 , self)
        self.underlined.setGeometry(20, 150, 750, 15)
        self.underlined.setStyleSheet("color: gray;")

        self.title_label = QLabel("Başlık:", self)
        self.title_label.setGeometry(20, 170, 150, 30)
        self.title_label.setStyleSheet("color: gray;")

        self.title_input = QLineEdit(self)
        self.title_input.setGeometry(70, 170, 700, 30)

        self.underlined = QLabel("_" * 700 , self)
        self.underlined.setGeometry(20, 190, 750, 15)
        self.underlined.setStyleSheet("color: gray;")

        self.mail_label = QLabel("Posta:", self)
        self.mail_label.setGeometry(20, 210, 150, 30)
        self.mail_label.setStyleSheet("color: gray;")

        self.mail_input = QTextEdit(self)
        self.mail_input.setGeometry(70, 210, 700, 300)

        self.send_button = QPushButton('Gönder', self)
        self.send_button.setGeometry(330, 520, 150, 40)
        self.send_button.clicked.connect(self.send_email)
        self.send_button.setStyleSheet("""
            QPushButton:hover {
            background-color: lightgreen;
            border-radius: 10px;
            }           
        """)

        self.by_label = QLabel("Power By: donmwz", self)
        self.by_label.setGeometry(345, 560, 150, 30)


    def send_email(self):
        smtp_server = "smtp-relay.brevo.com"
        port = 587
        sender_email = self.you_mail_input.currentText()
        login = "7b88d1001@smtp-brevo.com"
        password = "1MQ82zkhFEWRZtmN"
        receiver_email = self.recipient_mail_input.text()   # E-posta alıcısı
        subject = self.title_input.text()
        body = self.mail_input.toPlainText()
        

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(login, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            QMessageBox.information(self, 'Başarılı', 'E-posta başarıyla gönderildi.\nE-postanızı görememeniz durumunda spam ve gereksiz mail kutusunu kontrol ediniz.')
        except Exception as e:
            QMessageBox.warning(self, 'Hata', f'E-posta gönderilemedi. Hata: {e}')


app = QApplication(sys.argv)
ex = kayitApp()
ex.show()
sys.exit(app.exec_())
