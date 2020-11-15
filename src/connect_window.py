#!/bin/python3.8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import sys
from os import system, popen
from subprocess import run, PIPE

import src.style_sheet as style_sheet


class GetPass(object):
    def get_password(self, Dialog, ssid, bssid):
        """
            This function is for the default password label style
        """
        Dialog.setFixedSize(260, 220)
        Dialog.setGeometry(1080, 30, 190, 300)
        Dialog.setObjectName("i3 Wi-Fi_M")
        Dialog.setWindowTitle("Authentication Wi-Fi")
        Dialog.setStyleSheet("background-color:#15171a; border:0px; padding:0px;   margin: 0px 0px 0px 0px")

        self.ssid = ssid.split()[0].strip()
        self.bssid = bssid
        self.Dialog = Dialog

        self.title = QtWidgets.QLabel(Dialog)
        self.title.setText("Authentication Wi-Fi")
        self.title.setObjectName("Title")
        self.title.setStyleSheet('color:#5aa1a1;font-size:15px;font:vazir')
        self.title.setGeometry(QtCore.QRect(15, 13, 220, 19))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.get_ssid()

        self.password = QtWidgets.QLabel(Dialog)
        self.password.setObjectName("Password")
        self.password.setStyleSheet('color:#5aa1a1;font-size:15px;font:vazir')
        self.password.setGeometry(QtCore.QRect(15, 100, 80, 19))

        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(15, 125, 230, 27))
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setClearButtonEnabled(True)        
        self.pass_lineEdit.setPlaceholderText('password')
        self.pass_lineEdit.setObjectName("Pass_LineEdit")
        self.pass_lineEdit.setStyleSheet('color:#5aa1a1;qproperty-frame: false')
        self.pass_lineEdit.mousePressEvent =  self.pass_disable
        
        self.line_pass = QtWidgets.QFrame(Dialog)
        self.line_pass.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_pass.setStyleSheet('background-color:#374a4a')
        self.line_pass.setGeometry(QtCore.QRect(15,150, 230,2))
        self.line_pass.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_pass.setObjectName("Line_Pass")
        
        self.cansel = QtWidgets.QPushButton(Dialog)
        self.cansel.setGeometry(QtCore.QRect(90, 170, 70, 33))
        self.cansel.setObjectName("Cansel")
        self.cansel.setText("Cansel")
        self.cansel.setStyleSheet(style_sheet.styleSheet_CC())
        self.cansel.clicked.connect(lambda : self.close_window(Dialog))
        self.cansel.setShortcut("Ctrl+d")
        self.cansel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    
        self.connect = QtWidgets.QPushButton(Dialog)
        self.connect.setGeometry(QtCore.QRect(180,170, 70, 33))
        self.connect.setObjectName("Connect")
        self.connect.setText("Connect")
        self.connect.setStyleSheet(style_sheet.styleSheet_CC())
        self.connect.clicked.connect(self.connect_wifi)
        self.connect.setShortcut("Return")
        self.connect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))        
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def get_ssid(self):    
        """
            This function is for the default ssid label style
        """
        self.ssid_label = QtWidgets.QLabel(self.Dialog)
        self.ssid_label.setGeometry(QtCore.QRect(15, 50, 80, 19))
        self.ssid_label.setStyleSheet('color:#5aa1a1;font-size:15px;font:vazir')
        self.ssid_label.setObjectName("Username")
        self.ssid_label.setText("Username")
        
        self.ssid_lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.ssid_lineEdit.setGeometry(QtCore.QRect(15, 66, 230, 27))        
        self.ssid_lineEdit.setStyleSheet('color:#5aa1a1')
        self.ssid_lineEdit.setObjectName("Ssid_lineEdit")
        self.ssid_lineEdit.mousePressEvent = self.ssid_label_disable
        self.ssid_lineEdit.setClearButtonEnabled(True)
        
        self.line_ssid = QtWidgets.QFrame(self.Dialog)
        self.line_ssid.setObjectName("Line_Username")
        self.line_ssid.setStyleSheet('background-color:#5aa1a1')
        self.line_ssid.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_ssid.setGeometry(QtCore.QRect(15, 91, 230, 2))
        self.line_ssid.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        
        if self.ssid != 'Hidden':
            self.ssid_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ssid_lineEdit.setClearButtonEnabled(False)
            self.ssid_lineEdit.setReadOnly(True)
            self.ssid_lineEdit.setEnabled(False)
            self.ssid_lineEdit.setText(self.ssid)
            self.disable_get_ssid()


    def disable_get_ssid(self):
        """
            This function to diable of useranme label
        """
        self.ssid_label.setStyleSheet('color:#374a4a;font-size:15px;font:vazir')
        self.line_ssid.setStyleSheet('background-color:#374a4a')
        self.ssid_lineEdit.setStyleSheet('color:#374a4a')


    def pass_disable(self,*event):
        """
            This function to diable style of password label
        """
        self.password.setStyleSheet('color:#5aa1a1;font-size:15px;font:vazir')
        self.password.setText("Password")
        self.line_pass.setStyleSheet('background-color:#5aa1a1')
        self.pass_lineEdit.setStyleSheet('color:#5aa1a1')
        
        self.pass_lineEdit.setPlaceholderText('')
        self.disable_get_ssid()
        
        if self.ssid != 'Hidden':
            self.disable_get_ssid()
                
        if  self.ssid_lineEdit.text() :
            self.ssid_label.setText("Username")
        else:
            self.ssid_lineEdit.setPlaceholderText('ssid_label')
            self.ssid_label.setText("")


    def ssid_label_disable(self, *event):
        """
            This function to diable style of ssid_label label
        """
        self.ssid_label.setStyleSheet('color:#5aa1a1;font-size:15px;font:vazir')
        self.ssid_label.setText("Username")
        self.line_ssid.setStyleSheet('background-color:#5aa1a1')
        self.ssid_lineEdit.setStyleSheet('color:#5aa1a1')
        self.ssid_lineEdit.setPlaceholderText('')
        
        self.password.setStyleSheet('color:#374a4a;font-size:15px;font:vazir')
        self.line_pass.setStyleSheet('background-color:#374a4a')
        self.pass_lineEdit.setStyleSheet('color:#374a4a')
        
        if  self.pass_lineEdit.text() :
            self.password.setText("Password")
        else:
            self.pass_lineEdit.setPlaceholderText('Password')
            self.password.setText('')


    def connect_wifi(self):
        """
           This function to connect wifi and handle erorr by notify(etc...).
	"""
        QApplication.processEvents()
        ssid = self.bssid if self.ssid == "Hiddden" else self.ssid_lineEdit.text()
        active_WI = popen("ip addr show | grep 'wlp*' |  awk '/inet.*brd/{print $NF}'").read().strip()
        command_0 = "nmcli c delete `nmcli c | grep '^%s.*' | awk '{print $2}'`"%(ssid)
        command_1 = f"nmcli d wifi con {ssid} password {self.pass_lineEdit.text()}"
        command_1_0 = f"nmcli c add type wifi con-name {ssid} ifname {active_WI} ssid {ssid}"
        command_1_1 = f"nmcli c modify {ssid} wifi-sec.key-mgmt wpa-psk wifi-sec.psk {self.pass_lineEdit.text()}"
        command_1_2 = f"nmcli c up {ssid}"

        if not ssid or not self.pass_lineEdit.text():
            run(f"notify-send -u low 'Please Enter The ssid_label(SSID) OR  Pass'", shell=True)

            if not ssid :
                self.ssid_lineEdit.setStyleSheet("color:#ad4040")
                self.ssid_label.setStyleSheet("color:#ad4040")
                self.line_ssid.setStyleSheet("background-color:#ad4040")

            if not self.pass_lineEdit.text():
                self.pass_lineEdit.setStyleSheet("color:#ad4040")
                self.password.setStyleSheet("color:#ad4040")
                self.line_pass.setStyleSheet("background-color:#ad4040")

        else:
            self.Dialog.hide()
            if  self.ssid == "Hidden":
                run(command_1_0, shell=True,stdout = PIPE, stderr = PIPE)
                run(command_1_1, shell=True,stdout = PIPE, stderr = PIPE)
                status = run(command_1_2, shell=True,stdout = PIPE, stderr = PIPE)
            else:
                status = run(command_1, stderr = PIPE, stdout = PIPE, shell=True)
            stdout = status.stdout.decode()
            stderr = status.stderr.decode()
            
            run(f"notify-send -u low '{stdout}'", shell=True)
            if "successfully" not in stdout and 'successfully' not in stderr:
                stderr = stderr[:stderr.find("\n")]
                run(command_0, shell = True, stdout = PIPE, stderr = PIPE)
                self.pass_lineEdit.setText("")
                
                if 'Error: No network with SSID' in stderr:
                    self.ssid_lineEdit.setEnabled(True)
                    self.ssid_lineEdit.setReadOnly(False)
                    self.pass_disable()
                    self.ssid_label_disable()
                self.Dialog.setGeometry(1080, 30, 190, 300)
                self.Dialog.show()
            else:
                self.close_window(self.Dialog)


    def close_window(self,Dialog):
        """
            This function is used to close the desired window
        """
        Dialog.close()
