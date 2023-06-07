import sys
from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QButtonGroup
from PyQt5.QtWidgets import QMainWindow, QColorDialog, QFileDialog
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from prog import Ui_MainWindow
from datetime import datetime


DEFAULT_NAME = 'tmp.png'
WIDTH_INDENT = 240
HEIGHT_INDENT = 80


class AboutWindow(QWidget):  # окошко с информацией о приложении
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About')
        self.setGeometry(300, 300, 400, 20)
        self.info = QLabel(self)
        self.info.setText('Мини графическое приложение чисто поиграться с картинками :)')
        self.info.move(0, 0)


class PenPoint:  # класс, отвечающий за карандаш
    def __init__(self, x, y, lx=0, ly=0):
        self.x = x
        self.y = y
        self.lx = lx
        self.ly = ly

    def draw(self, painter, color=QColor(0, 0, 0)):
        pen = QPen(color, 4, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawLine(self.x - 1, self.y - 6, self.lx - 1, self.ly - 6)


class BrushPoint:  # класс, отвечающий за маркер
    def __init__(self, x, y, lx=0, ly=0):
        self.x = x
        self.y = y
        self.lx = lx
        self.ly = ly

    def draw(self, painter, color=QColor(0, 0, 0)):
        pen = QPen(color, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawLine(self.x - 1, self.y - 6, self.lx - 1, self.ly - 6)


class Line:  # класс, отвечающий за отрисовку линии
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey

    def draw(self, painter, color=QColor(0, 0, 0)):
        painter.setBrush(QBrush(color))
        painter.setPen(color)
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)


class Circle:  # класс, отвечающий за отрисовку круга
    def __init__(self, sx, sy, x, y):
        self.sx = sx
        self.sy = sy
        self.x = x
        self.y = y

    def draw(self, painter, color=QColor(0, 0, 0)):
        painter.setPen(color)
        painter.setBrush(QBrush(QColor(0, 0, 0, 0)))
        r = int(((self.sx - self.x) ** 2 + (self.sy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.sx - r, self.sy - r, 2 * r, 2 * r)


class ErasePoint:  # класс, отвечающий за стирашку
    def __init__(self, x, y, lx=0, ly=0):
        self.x = x
        self.y = y
        self.lx = lx
        self.ly = ly

    def draw(self, painter, color=QColor(255, 255, 255)):
        pen = QPen(Qt.white, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawLine(self.x - 1, self.y - 6, self.lx - 1, self.ly - 6)


class PAINT(Ui_MainWindow, QMainWindow):  # основное приложение, дизайн был создан в Qt Designer и импортируется
    def __init__(self):                   # из другого файла
        super().__init__()
        self.color = QColor(0, 0, 0)
        newim = Image.open(DEFAULT_NAME)
        pixels = newim.load()
        x, y = newim.size
        for i in range(x):
            for j in range(y):
                pixels[i, j] = 255, 255, 255
        newim.save(DEFAULT_NAME)
        self.setupUi(self)
        self.fname = ''
        self.aboutWindow = AboutWindow()
        self.pic = QPixmap(DEFAULT_NAME)
        self.pic = self.pic.scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio)
        self.label.setPixmap(self.pic)
        self.pushButton.setStyleSheet(f"background-color: {'#ff0000'}")
        self.pushButton.setEnabled(False)
        self.pushButton_3.setStyleSheet(f"background-color: {'#00ff00'}")
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setStyleSheet(f"background-color: {'#0000ff'}")
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.clicked.connect(self.bv)
        self.ColorButton.clicked.connect(self.changeColor)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionrotate_by_90.triggered.connect(self.flip90)
        self.actionrotate_by_180.triggered.connect(self.flip180)
        self.actionrotate_by_270.triggered.connect(self.flip270)
        self.actionFlip_Horizontal_2.triggered.connect(self.fliph)
        self.actionFlip_Vertical_2.triggered.connect(self.flipv)
        self.actionInvert_Colors.triggered.connect(self.invert)
        self.actionOpen.triggered.connect(self.open)
        self.actionNew.triggered.connect(self.newact)
        self.actionNew.setShortcut(QKeySequence("Ctrl+A"))
        self.actionSave_as.triggered.connect(self.saveimage)
        self.actionOpen.setShortcut(QKeySequence("Ctrl+S"))
        self.actionClear_Image.triggered.connect(self.clearim)
        self.actionSave_as.setShortcut(QKeySequence("Ctrl+D"))
        btn_group = QButtonGroup(self)
        btn_group.addButton(self.BrushButton)
        btn_group.addButton(self.LineButton)
        btn_group.addButton(self.CircleButton)
        btn_group.addButton(self.PenButton)
        btn_group.addButton(self.EraseButton)
        btn_group.addButton(self.CopyButton)
        btn_group.setExclusive(True)
        self.BrushButton.clicked.connect(self.setBrush)
        self.LineButton.clicked.connect(self.setLine)
        self.CircleButton.clicked.connect(self.setCircle)
        self.PenButton.clicked.connect(self.setPen)
        self.EraseButton.clicked.connect(self.setErase)
        self.CopyButton.clicked.connect(self.setCopy)
        self.objects = []
        self.instrument = ''
        self.lastPoint = QPoint()

    def bv(self):  # функция, выполняющая затемнение рабочего холста
        self.endend()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('shading', '{datetime.now()}')")
        image = Image.open(DEFAULT_NAME)
        img1 = image.copy()
        pixels = img1.load()
        pixels1 = image.load()
        rper = self.spinBox.value() / 100
        gper = self.spinBox_2.value() / 100
        bper = self.spinBox_3.value() / 100
        x, y = img1.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = int(r * rper), int(g * gper), int(b * bper)
        img1.save(DEFAULT_NAME)
        self.label.setPixmap(QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def show_about(self):  # функция, выполняющая затемнение рабочего холста
        self.endend()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('show_about', '{datetime.now()}')")
        self.aboutWindow.show()

    def flip90(self):  # функция, выполняющая разворот картинки на 90 градусов
        self.endend()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('flip90', '{datetime.now()}')")
        im = Image.open(DEFAULT_NAME).transpose(Image.ROTATE_90)
        im.save(DEFAULT_NAME)
        self.label.setPixmap(QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def flip180(self):  # функция, выполняющая разворот картинки на 180 градусов
        self.endend()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('flip180', '{datetime.now()}')")
        im = Image.open(DEFAULT_NAME).transpose(Image.ROTATE_180)
        im.save(DEFAULT_NAME)
        self.label.setPixmap(QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def flip270(self):  # функция, выполняющая разворот картинки на 270 градусов
        self.endend()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('flip270', '{datetime.now()}')")
        im = Image.open(DEFAULT_NAME).transpose(Image.ROTATE_270)
        im.save(DEFAULT_NAME)
        self.label.setPixmap(QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def fliph(self):  # функция, выполняющая поворот картинки по горизонтали
        self.endend()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('fliph', '{datetime.now()}')")
        im = Image.open(DEFAULT_NAME).transpose(Image.FLIP_TOP_BOTTOM)
        im.save(DEFAULT_NAME)
        self.label.setPixmap(QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def flipv(self):  # функция, выполняющая поворот картинки по вертикали
        self.endend()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('flipv', '{datetime.now()}')")
        im = Image.open(DEFAULT_NAME).transpose(Image.FLIP_LEFT_RIGHT)
        im.save(DEFAULT_NAME)
        self.label.setPixmap(QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def invert(self):  # функция, выполняющая инвертирование цветов на картинке
        self.endend()
        image = Image.open(DEFAULT_NAME)
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('invert', '{datetime.now()}')")
        img1 = image.copy()
        pixels = img1.load()
        x, y = img1.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 255 - r, 255 - g, 255 - b
        img1.save(DEFAULT_NAME)
        self.label.setPixmap(
            QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def clearim(self):  # функция, выполняющая очистку холста
        self.endend()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('clear', '{datetime.now()}')")
        newim = Image.open(DEFAULT_NAME)
        pixels = newim.load()
        x, y = newim.size
        for i in range(x):
            for j in range(y):
                pixels[i, j] = 255, 255, 255
        newim.save(DEFAULT_NAME)
        self.label.setPixmap(QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def open(self):  # функция, выполняющая открытие картинки из проводника
        self.endend()
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.png)')[0]
        if self.fname:
            im = Image.open(self.fname)
            query = QSqlQuery()
            query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('open', '{datetime.now()}')")
            image1 = im.copy()
            image1.save(DEFAULT_NAME)
            self.label.setPixmap(
                QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))

    def saveimage(self):  # функция, выполняющая сохранение картинки в проводнике
        self.endend()
        path, _ = QFileDialog.getSaveFileName(self, "Save file", self.fname, "PNG Image file (*.png)")

        if path:
            im = Image.open(DEFAULT_NAME)
            query = QSqlQuery()
            query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('saveimage', '{datetime.now()}')")
            image = im.copy()
            image.save(path)

    def newact(self):  # функция, выполняющая создание чистого холста
        self.fname = ''
        self.clearim()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('newact', '{datetime.now()}')")

    def paintEvent(self, event):  # обратотка события отрисовки
        painter = QPainter(self.label)
        self.label.setPixmap(QPixmap(DEFAULT_NAME).scaled(self.label.size(), aspectRatioMode=Qt.IgnoreAspectRatio))
        painter.begin(self.label.pixmap())
        for obj in self.objects:
            obj.draw(painter, self.color)
        painter.end()

    def mousePressEvent(self, event):  # обратотка события нажатия на кнопку мыши
        if self.instrument == 'brush':
            self.objects.append(BrushPoint(event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT,
                                           event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT))
            self.repaint()
        elif self.instrument == 'line':
            self.objects.append(Line(event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT, event.x() - WIDTH_INDENT,
                                     event.y() - HEIGHT_INDENT))
            self.repaint()
        elif self.instrument == 'circle':
            self.objects.append(Circle(event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT, event.x() - WIDTH_INDENT,
                                       event.y() - HEIGHT_INDENT))
            self.repaint()
        elif self.instrument == 'pen':
            self.objects.append(PenPoint(event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT, event.x() - WIDTH_INDENT,
                                         event.y() - HEIGHT_INDENT))
            self.repaint()
        elif self.instrument == 'erase':
            self.objects.append(ErasePoint(event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT,
                                           event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT))
            self.repaint()
        self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):  # обратотка события перемещения мыши
        if self.instrument == 'brush':
            self.objects.append(BrushPoint(self.lastPoint.x() - WIDTH_INDENT, self.lastPoint.y() - HEIGHT_INDENT,
                                           event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT))
            self.repaint()
        elif self.instrument == 'line':
            self.objects[-1].ex = event.x() - WIDTH_INDENT
            self.objects[-1].ey = event.y() - HEIGHT_INDENT
            self.repaint()
        elif self.instrument == 'circle':
            self.objects[-1].x = event.x() - WIDTH_INDENT
            self.objects[-1].y = event.y() - HEIGHT_INDENT
            self.repaint()
        elif self.instrument == 'pen':
            self.objects.append(PenPoint(self.lastPoint.x() - WIDTH_INDENT, self.lastPoint.y() - HEIGHT_INDENT,
                                         event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT))
            self.repaint()
        elif self.instrument == 'erase':
            self.objects.append(ErasePoint(self.lastPoint.x() - WIDTH_INDENT, self.lastPoint.y() - HEIGHT_INDENT,
                                           event.x() - WIDTH_INDENT, event.y() - HEIGHT_INDENT))
            self.repaint()
        self.lastPoint = event.pos()

    def setPen(self):  # изменение действия на отрисовку карандашом
        self.instrument = 'pen'
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('setPen', '{datetime.now()}')")

    def setBrush(self):  # изменение действия на отрисовку маркером
        self.instrument = 'brush'
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('setBrush', '{datetime.now()}')")

    def setLine(self):  # изменение действия на отрисовку линии
        self.instrument = 'line'
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('setLine', '{datetime.now()}')")

    def setCircle(self):  # изменение действия на отрисовку круга
        self.instrument = 'circle'
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('setCircle', '{datetime.now()}')")

    def setErase(self):  # изменение действия на стирание ластиком
        self.instrument = 'erase'
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('setErase', '{datetime.now()}')")

    def setCopy(self):
        self.instrument = 'copy'
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('setCopy', '{datetime.now()}')")

    def changeColor(self):  # изменение цвета отрисовки
        self.endend()
        self.color = QColorDialog.getColor()
        query = QSqlQuery()
        query.exec_(f"INSERT INTO Logs (action, datetime) VALUES ('changeColor', '{datetime.now()}')")

    def endend(self):  # сохранение отрисованных элементов на холсте перед функциями работы с картинками
        x = self.label.pixmap().toImage()
        x.save(DEFAULT_NAME)
        self.objects.clear()


def except_hook(cls, expection, traceback):  # отлавливание входящих ошибок
    sys.__excepthook__(cls, expection, traceback)


if __name__ == '__main__':
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("databases/log.db")  # подключение к базе данных
    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)
    else:
        print("Connect")
    createTableQuery = QSqlQuery( """
        CREATE TABLE Logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            action VARCHAR(50) NOT NULL,
            datetime DATETIME NOT NULL
        )
        """)
    QSqlQuery.exec_(createTableQuery)
    app = QApplication(sys.argv)
    wnd = PAINT()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
