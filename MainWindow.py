from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox, QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPixmap


import main
import os

class EmailWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Email a friend who's interested in space(hopefully?)!")
        self.label1 = QLabel("Type your recipients separated with a comma in the recipients area or enter a single email address")
        self.label2 = QLabel("Eg - friend1@gmail.com,friend2@gmail.com,...")
        self.label3 = QLabel("Type in your subject as a continuous line in the subject area")
        self.label4 = QLabel("Finally add in your message and hit send")

        self.recipient_area = QLineEdit("Recipients - ")
        self.subject_area = QLineEdit("Subject - ")
        self.message_area = QLineEdit("Message - ")

        self.send = QPushButton("Send")
        self.send.clicked.connect(self.send_clicked)

        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.recipient_area)
        layout.addWidget(self.subject_area)
        layout.addWidget(self.message_area)
        layout.addWidget(self.send)

        self.setLayout(layout)

    def send_clicked(self):
        recipients = (self.recipient_area.text())
        subject = (self.subject_area.text())
        message = (self.message_area.text())

        if ',' in recipients:
            recipient_list = recipients.split(',')
            for i in recipient_list:
                main.sendEmail(i, subject, message)
        else:
            main.sendEmail(recipients, subject, message)
        



class RoverWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Rover options available")
        self.label1 = QLabel("Type your choice in the main window under the button")
        self.label2 = QLabel("For more info on the rovers, visit")
        self.label3 = QLabel("https://api.nasa.gov/")

        self.rovers = QComboBox()
        self.rovers.addItems(['Curiosity', 'Opportunity', 'Spirit'])

        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.rovers)
        
        self.setLayout(layout)

class CameraWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Camera options for each rover")
        self.label1 = QLabel("Type your choice in the main window under the button")
        self.label2 = QLabel("For more info on the abbreviations, visit")
        self.label3 = QLabel("https://api.nasa.gov/")
        
        self.cameraCuriosity = QComboBox()
        self.cameraCuriosity.addItems(['CURIOSITY', 'fhaz', 'rhaz', 'mast', 'chemcam', 'mahli', 'mardi', 'navcam'])
        

        self.cameraOpportunity = QComboBox()
        self.cameraOpportunity.addItems(['OPPORTUNITY', 'fhaz', 'rhaz', 'navcam', 'pancam', 'minites'])

        self.cameraSpirit= QComboBox()
        self.cameraSpirit.addItems(['SPIRIT', 'navcam', 'pancam', 'minites'])

        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.cameraCuriosity)
        layout.addWidget(self.cameraOpportunity)
        layout.addWidget(self.cameraSpirit)

        self.setLayout(layout)

class SolWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Sol can range from 0 to 1000")
        self.label1 = QLabel("Type your choice in the main window under the button")
        self.label2 = QLabel("For more info on the martian dates, visit")
        self.label3 = QLabel("https://api.nasa.gov/")
        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        self.setLayout(layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 689)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)

        #for opening the other windows
        self.w = None
        self.w1 = None
        self.w2 = None
        self.w3 = None

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(310, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Title.setFrameShape(QtWidgets.QFrame.Box)
        self.Title.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Title.setTextFormat(QtCore.Qt.RichText)
        self.Title.setObjectName("Title")

        self.Image_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Image_Frame.setEnabled(False)
        self.Image_Frame.setGeometry(QtCore.QRect(350, 80, 561, 481))
        self.Image_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Image_Frame.setObjectName("Image_Frame")

        global image_label
        image_label = QtWidgets.QLabel(self.centralwidget)
        image_label.setGeometry(QtCore.QRect(350, 80, 561, 481))
        image = QtGui.QPixmap('../FreeMarsPics/rover_500.jpg')
        image_label.setPixmap(image)

        self.Email_button = QtWidgets.QPushButton(self.centralwidget)
        self.Email_button.setGeometry(QtCore.QRect(180, 560, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Email_button.setFont(font)
        self.Email_button.setObjectName("Email_button")
        self.Email_button.clicked.connect(self.sendEmail_Clicked)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 311, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.Rover_selection = QtWidgets.QPushButton(self.frame)
        self.Rover_selection.setGeometry(QtCore.QRect(0, 0, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Rover_selection.setFont(font)
        self.Rover_selection.setObjectName("Rover_selection")
        self.Rover_selection.clicked.connect(self.roverSelection_Clicked)

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 80, 311, 81))
        self.lineEdit.setObjectName("lineEdit")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 250, 311, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")


        self.Sol_selection = QtWidgets.QPushButton(self.frame_2)
        self.Sol_selection.setGeometry(QtCore.QRect(0, 0, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Sol_selection.setFont(font)
        self.Sol_selection.setObjectName("Sol_selection")
        self.Sol_selection.clicked.connect(self.solSelection_Clicked)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 70, 311, 81))
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 410, 311, 141))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.Camera_selection = QtWidgets.QPushButton(self.frame_3)
        self.Camera_selection.setGeometry(QtCore.QRect(0, 0, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Camera_selection.setFont(font)
        self.Camera_selection.setObjectName("Camera_selection")
        self.Camera_selection.clicked.connect(self.cameraSelection_Clicked)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 60, 311, 81))
        self.lineEdit_3.setObjectName("lineEdit_3")


        self.Get_image_button = QtWidgets.QPushButton(self.centralwidget)
        self.Get_image_button.setGeometry(QtCore.QRect(20, 560, 141, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Get_image_button.setFont(font)
        self.Get_image_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Get_image_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Get_image_button.setObjectName("Get_image_button")
        self.Get_image_button.clicked.connect(self.getImages_Clicked)


        self.previous_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_button.setGeometry(QtCore.QRect(350, 570, 171, 81))
        self.previous_button.setObjectName("previous_button")
        self.previous_button.clicked.connect(self.goPrev)

        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(710, 570, 201, 81))
        self.next_button.setObjectName("next_button")
        self.next_button.clicked.connect(self.goNext)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def roverSelection_Clicked(self):
        print("LMAO")
        if self.w is None:
            self.w = RoverWindow()
        self.w.show()

    def cameraSelection_Clicked(self):
        print("LMAO")
        if self.w1 is None:
            self.w1 = CameraWindow()
        self.w1.show()

    def solSelection_Clicked(self):
        print("LMAO")
        if self.w2 is None:
            self.w2 = SolWindow()
        self.w2.show()

    def getImages_Clicked(self):
        rover_name=(self.lineEdit.text()).lower()
        camera_name=(self.lineEdit_3.text()).lower()
        sol_date = (self.lineEdit_2.text()).lower()
        
        main.getImage(rover_name, camera_name, sol_date)

    global counter
    counter = 1
    def goNext(self):
        global counter
        count_files = 0
        for path in os.listdir('../FreeMarsPics/MarsPics'):
            # check if current path is a file
            if os.path.isfile(os.path.join('../FreeMarsPics/MarsPics', path)):
                count_files += 1

        if 0<counter<=count_files:
            image = QtGui.QPixmap('../FreeMarsPics/MarsPics/image'+str(counter))
            image_label.setPixmap(image)
            counter+=1
            print(counter)
        else:
            counter = 1

    def goPrev(self):
        global counter
        count_files = 0
        for path in os.listdir('../FreeMarsPics/MarsPics'):
            # check if current path is a file
            if os.path.isfile(os.path.join('../FreeMarsPics/MarsPics', path)):
                count_files += 1
        
        if 0<counter<=count_files:
            image = QtGui.QPixmap('../FreeMarsPics/MarsPics/image'+str(counter))
            image_label.setPixmap(image)
            counter-=1
            print(counter)
        else:
            counter = 1

    def sendEmail_Clicked(self):
        print("LMAO")
        if self.w3 is None:
            self.w3 = EmailWindow()
        self.w3.show()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "The Martian Chronicles"))
        self.Email_button.setText(_translate("MainWindow", "Send Email"))
        self.Rover_selection.setText(_translate("MainWindow", "Rover"))
        self.Sol_selection.setText(_translate("MainWindow", "Sol"))
        self.Camera_selection.setText(_translate("MainWindow", "Camera"))
        self.Get_image_button.setText(_translate("MainWindow", "Get Images"))
        self.previous_button.setText(_translate("MainWindow", "Previous"))
        self.next_button.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
