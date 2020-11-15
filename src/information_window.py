#!/bin/python3

from PyQt5 import QtCore,  QtWidgets
from os import popen
import src.style_sheet as style_sheet

class Info:
    def Information_Window(self, Dialog, Bssid):
        Dialog.setWindowTitle("Information")
        Dialog.setObjectName("Information")
        Dialog.setStyleSheet("background-color:#15171a")
        Dialog.setFixedSize(230,230)
        Dialog.setGeometry(930,80,190,300)
    
        Bssid = Bssid.replace(':', '\\\:')
        Get_Info = popen(f"nmcli -t -f IN-USE,SSID,SECURITY,SIGNAL,BARS,FREQ,BSSID \
                dev wifi |  grep -Po '.*{Bssid}' ").read().replace("\\","").strip().split(":", 6)
        
        Get_Info[0] = "Connected" if Get_Info[0] == "yes" or Get_Info[0] == '*'  else  "Disconnected"
        Get_Info[1] = "Anonymous" if not Get_Info[1]  else Get_Info[1]

        Info = ''.join([ k+v for k,v in dict(zip('STATUS:\t|\nSSID:\t|\nSECURITY:\t|\
SIGNAL:\t|\nBARS:\t|\nFREQ:\t|\nBSSID:\t'.split('|'), Get_Info)).items()])
        
        self.Lable = QtWidgets.QLabel(Dialog)
        self.Lable.setObjectName("Label")
        self.Lable.setStyleSheet('color:#5aa1a1;font-size:15px;font:vazir')
        self.Lable.setGeometry(QtCore.QRect(10, 10, 250, 160))
        self.Lable.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.Lable.setText(Info)

        self.Ok = QtWidgets.QPushButton(Dialog)
        self.Ok.setObjectName("Ok")
        self.Ok.setText("OK")
        self.Ok.setStyleSheet(style_sheet.styleSheet_CC())
        self.Ok.setGeometry(QtCore.QRect(79, 185, 70, 33))
        self.Ok.clicked.connect(lambda : self.Close_Window(Dialog))
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def Close_Window(self,Dialog):
        """
            This function is used to close the desired window
        """
        Dialog.close()
