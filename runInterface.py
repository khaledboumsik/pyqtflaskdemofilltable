import sys
from PyQt5.QtWidgets import QApplication, QWidget
from tableexample import Ui_Form
import requests
def get_all_users():
    return requests.get("http://127.0.0.1:5000/users").json()

all_users=get_all_users()
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self,all_users)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
