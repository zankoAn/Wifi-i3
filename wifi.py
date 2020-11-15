#!/bin/pytohn3.8

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QTimer, QMetaObject
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenu , QFileDialog, QDialog,
        QVBoxLayout, QPushButton, QGroupBox, QFormLayout, QLabel, QScrollArea, QAction)

from os import system, popen , getcwd

from subprocess import run, PIPE, Popen

from src.connect_window import GetPass
from src.information_window import Info
import src.style_sheet as style_sheet


class WIFI_(QMainWindow):
    def setupUi(self, Dialog):
        app.processEvents()
     
        Dialog.setWindowTitle("i3 Wi-Fi_M ")
        Dialog.setObjectName("i3 Wi-Fi_M")
        Dialog.setStyleSheet("background-color:#15171a")
        Dialog.setGeometry(1120, 30, 190, 300)
        
        self.groupBox = QGroupBox()
        self.formLayout = QFormLayout()
        self.Dialog = Dialog
        self.current_path = getcwd()
        
        self.refresh = QPushButton(Dialog)
        self.refresh.setGeometry(QRect(15, 7, 17, 17))
        self.refresh.setObjectName("Refresh")
        self.refresh.setIcon(QtGui.QIcon(f"{self.current_path}/icons/refresh_green-64.png"))
        self.refresh.setStyleSheet(style_sheet.back_push_color("#162e2e"))
        self.refresh.clicked.connect(self.handler)
        self.refresh.setToolTip('Refresh')
        
        self.exit = QPushButton(Dialog)
        self.exit.setGeometry(QRect(158, 7, 17, 17))
        self.exit.setObjectName("Exit")
        self.exit.setIcon(QtGui.QIcon(f"{self.current_path}/icons/multiply-64.png"))
        self.exit.setStyleSheet(style_sheet.back_push_color("#4f0c3e"))
        self.exit.clicked.connect(lambda x : self.close_window(Dialog))
        self.exit.setToolTip('Exit')
     
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setStyleSheet("border-top: 1px solid #2b2f36;border-radius:8px")
        self.scrollArea.setGeometry(QRect(7, 33, 176, 257))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.verticalScrollBar().setStyleSheet(style_sheet.scroll_style())
        self.scrollArea.setWidget(self.groupBox)
        
        self.title_0 = QLabel(Dialog)
        self.title_0.setGeometry(QRect(45, 8, 100, 15))
        self.title_0.setObjectName("title_0")
        self.title_0.setStyleSheet(' color:#5aa1a1; subcontrol-position: top center;font:11pt')
        self.title_0.setText("Available WiFi")
     
        Dialog.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.handler)
        self.timer.start(10)
        QMetaObject.connectSlotsByName(Dialog) 
     
     
    def handler(self):
        """
            This function is for handling the crashing Wi-Fi scan
        """
        app.processEvents()
     
        wifi =  Popen("nmcli -t -f  active,ssid,signal,bssid dev wifi | sort -r ",\
                shell=True, stderr=PIPE, stdout=PIPE\
                )  # Split ssid  signal and bssid of out put somthing like that ['status', 'ssid', 'bssid' ]
        
        if wifi.communicate()[1]:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            msgBox.setText(wifi.communicate()[1].decode())
                
            msgBox.setStyleSheet("background-color:#15171a;color:#5aa1a1")
            msgBox.setWindowTitle("NetworkManager Error")
            msgBox.setFont(QtGui.QFont('vazir',12))
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.setGeometry(840,170,0,0)
            returnValue = msgBox.exec_()
                
            if returnValue == QtWidgets.QMessageBox.Ok:
                sys.exit()
                
        else: 
            self.wifi_  = [x for x in wifi.communicate()[0].decode().split('\n') if x]
     
        self.timer.stop()
        self.scan()
     
     
    def scan(self):
        """
            Create a dynamic PushButton for  avaliable Wi-Fi
        """
        app.processEvents()
        
        wifi_list = [ x.replace("\\","").strip().split(":", 3) for x in self.wifi_ ]
        layout = self.formLayout.layout()
        if layout.count() is not None:   # Remove duplicate PushButton after each refresh            
            for i in reversed(range(layout.count())):                
                layout.itemAt(i).widget().deleteLater()
        
        for IW in range(len(wifi_list)):   # Create a dynamic PushButton
            self.IW = QPushButton(Dialog)
            self.IW.setFont(QtGui.QFont('SansSerif', 10))
            self.IW.setObjectName(wifi_list[IW][3])
            self.IW.setFixedSize(166, 24)
            self.IW.mouseDoubleClickEvent
            
            if not wifi_list[IW][1]:
                wifi_list[IW][1] = "Hidden"
            
            if wifi_list[IW][0] == 'yes':
                self.IW.setStyleSheet(style_sheet.pushButton_style_connect())
            else:
                self.IW.setStyleSheet(style_sheet.pushButton_style_other())
            
            self.IW.setText('       '.join(wifi_list[IW][1:3]))
            self.IW.setContextMenuPolicy(Qt.CustomContextMenu)
            self.IW.customContextMenuRequested.connect(self.right_click)
            self.IW.clicked.connect(self.click_btn)
            self.formLayout.addRow(self.IW)
        
        self.groupBox.setLayout(self.formLayout)
     
        
    def click_btn(self,event):
        """
            Handle events after single click PushButtons
        """
        app.processEvents()
            
        self.Wifi_Info = self.sender()
        if ( active_bssid := popen("nmcli -t -f  active,ssid,bssid dev wifi | sort -r|grep yes ").read().replace("\\", "").strip().split(":", 2)):
            active_bssid = active_bssid[2] if len(active_bssid) > 1 else ""
            
        if self.Wifi_Info.objectName() != active_bssid:
            self.close_window(self.Dialog)
            if popen(f" nmcli c | grep '{self.Wifi_Info.text().split()[0]}'").read():
                command_0 = "nmcli c up `nmcli c | grep '^%s.*' | awk '{print $2}'`"%(self.Wifi_Info.text().split()[0])
                status = run(command_0, stderr=PIPE, stdout=PIPE, shell=True)
                stdout = status.stdout.decode()
                stderr = status.stderr.decode()
                
                if  'successfully' not in stdout and 'successfully' not in stderr:
                    command_1 = "nmcli c delete `nmcli c | grep '^%s.*' | awk '{print $2}'`"%(self.Wifi_Info.text().split()[0])
                    run(command_1, shell=True, stdout=PIPE, stderr=PIPE)
                    self.connect_window()
                    command_2 = f"notify-send -u low '{status.stderr.decode()}'"                    
                    run(command_2, shell=True)
                    
                else:
                    command_3 = f"notify-send -u low '{status.stdout.decode()}'"
                    run(command_3, shell=True)
                    self.close_window(self.Dialog)
            else:
                self.connect_window()


    def right_click(self, event):
        """
            Handle events after right click PushButtons
        """
        app.processEvents()
        
        if Qt.RightButton:
            self.Wifi_Info = self.sender()
            
            menu = QMenu(self)
            if ( x := popen("nmcli -t -f  active,ssid,bssid dev wifi | sort -r|grep yes ").read().replace("\\", "").strip().split(":",2)):
                x = x[2] if len(x) > 1 else ""
            
            if self.Wifi_Info.objectName() == x: 
                menu.addAction(QAction(QtGui.QIcon(f"{self.current_path}/icons/desconnect-64.png"), 'Desconnect', self))
                
            else:
                menu.addAction(QAction(QtGui.QIcon(f"{self.current_path}/icons/connect-64.png"), 'Connect', self))
            
            menu.addAction(QAction(QtGui.QIcon(f"{self.current_path}/icons/info-64.png"), 'Info', self))
            menu.setStyleSheet(style_sheet.menu_style())
            geometry_menu = self.Wifi_Info.geometry()
            self.setGeometry(geometry_menu.x()+1000, geometry_menu.y()+90, 100, 100)
            action = menu.exec_(self.mapToGlobal(event))
            
            try:
                if action.text() == 'Connect':
                    self.close_window(self.Dialog)
                    self.connect_window()
                if action.text() == 'Desconnect':
                    self.desconnect_wifi()
                if  action.text() == 'Info':
                    self.info_win()
            except AttributeError:
                pass

 
    def connect_window(self):
        """
            This function to open the connect window
        """
        Dialog = QDialog()
        Ui = GetPass()
        Ui.get_password(Dialog, self.Wifi_Info.text().split()[0], self.Wifi_Info.objectName())
        Dialog.exec_()


    def desconnect_wifi(self):
        """
            This function to open the desconnect window
        """
        app.processEvents()
        
        Connec_Uuid = popen("nmcli -f STATE,CON-UUID device status | grep -Po '^connected\K\W.*' ").read()
        Out = run(f'nmcli c dow uuid {Connec_Uuid}', stdout = PIPE, stderr = PIPE, shell=True)
        if ( out := Out.stdout.decode() ) or ( out := Out.stderr.decode() ):
            run(f"notify-send -u critical '{out}'", shell=True)
        self.close_window(self.Dialog)


    def info_win(self):
        """
            This function to open the information available Wi-Fi window
        """
        app.processEvents()
        
        Dialog = QDialog()
        Ui = Info()
        Ui.Information_Window(Dialog, self.Wifi_Info.objectName())
        Dialog.exec()


    def close_window(self,Dialog):
        """
            This function is used to close the desired window
        """
        Dialog.close()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    Ui = WIFI_()
    Ui.setupUi(Dialog)    
    Dialog.show()
    sys.exit(app.exec_())
