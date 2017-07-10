import sys	
from PySide.QtGui import QApplication
from PySide.QtCore import QUrl
from PySide.QtWebKit import QWebView

app = QApplication(sys.argv)
b = QWebView()
# b.load(QUrl('https://canary.discordapp.com/login'))
b.load(QUrl('https://discordapp.com/login'))
b.show()
app.exec_()
