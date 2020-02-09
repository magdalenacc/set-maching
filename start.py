from PyQt5.QtWidgets import QApplication

from models import Model
from views import StartWindow

app = QApplication([])
model = Model()
start_window = StartWindow(model)
start_window.show()
app.exit(app.exec_())
