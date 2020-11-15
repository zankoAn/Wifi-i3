#!/bin/python

def pushButton_style_connect():
        return ("""
            QPushButton{font-family:SansSerif; color:#4ea65f; background-color:#15171a; border:0px; Text-align:left}
    	    QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 #1a1c1f, stop: 0 #1f2329); border-radius:7px}
            QPushButton::pressed{background-color:#15171a; border-radius:7px; border-style:inset}
        """)


def pushButton_style_other():
        return ("""
            QPushButton{font-family:SansSerif; color:#5aa1a1; background-color:#15171a; border:0px;Text-align:left}
    	    QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 #191c21, stop:0 #22272e); border-radius:7px}
            QPushButton::pressed{background-color:#15171a; border-radius:7px; border-style: inset}
        """)


def back_push_color(color):
        return ("""
                QPushButton{border-style:solid; border-radius:7px; color:#5aa1a1; background-color:#1a1c1e}
                QPushButton::hover{border:1px solid %s; border-radius:7px}
                QToolTip {color:#5aa1a1; background-color:#15171a; border: 0px}
                """%(color))


def scroll_style():
       return ("""
            QScrollBar:vertical {width:10px; background-color:#2b2f36; margin:0px 0px 0px 0px;  border-radius:3px}
            QScrollBar::handle {background:#191b1f; border-radius:5px}
            QScrollBar::add-line:vertical {height:0px; margin:0px 0px 0px 0px}
            QScrollBar::sub-line:vertical {height:0px}
        """)


def menu_style():
        return ("""
                QMenu {background-color:#1d1f24; color:#5aa1a1; font:12pt}
                QMenu::item {background-color:transparent}
                QMenu::item:selected {background-color:rgb(0, 85, 127); color:rgb(255, 255, 255)}
        """)


def back_push_0():
        return ("""
            QPushButton{font-size:15px; border-style:solid; border-radius:7px; color:#5aa1a1; background-color:#15171a}
    	    QPushButton::hover{background-color: #1b1d21}
            QPushButton::pressed{background-color:#15171a; border-radius:7px; border-style: inset}
        """)


def styleSheet_CC():
        return ("""
            QPushButton{font:hack 10; border-style: solid; border-radius:7px; color:#5aa1a1; background-color:#15171a; border:1px solid #303842}
    	    QPushButton::hover{background-color:#1a3333}
            QPushButton::pressed{background-color:#1a4a4a; border-radius:7px; border-style: inset}
        """)
        
