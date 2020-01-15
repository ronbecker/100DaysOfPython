#!/usr/bin/env python
import os
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("CleanJaro - A Manjaro Maintenance Utility")
    textLabel.move(64,32)

    button1 = QPushButton(widget)
    button1.setText("Update Mirrors")
    button1.move(64,64)
    button1.clicked.connect(button1_clicked)

    button2 = QPushButton(widget)
    button2.setText("System Upgrade")
    button2.move(64,96)
    button2.clicked.connect(button2_clicked)

    button3 = QPushButton(widget)
    button3.setText("Remove Orphan Packages")
    button3.move(64,128)
    button3.clicked.connect(button3_clicked)

    button4 = QPushButton(widget)
    button4.setText("Purge Cache Not Accessed in 30 Days")
    button4.move(64,160)
    button4.clicked.connect(button4_clicked)

    button5 = QPushButton(widget)
    button5.setText("Clean Up pacman Cache")
    button5.move(64,192)
    button5.clicked.connect(button5_clicked)

    button6 = QPushButton(widget)
    button6.setText("Exit")
    button6.move(64,224)
    button6.clicked.connect(button6_clicked)

    widget.setGeometry(50,50,640,300)
    widget.setWindowTitle("CleanJaro GUI")
    widget.show()
    sys.exit(app.exec_())

def button1_clicked():
       subprocess.call(["sudo", "pacman", "-Sy"])
def button2_clicked():
       subprocess.call(["sudo", "pacman", "-Syyu", "--noconfirm"])
def button3_clicked():
       os.system("sudo pacman -Rs $(pacman -Qdtq)")
def button4_clicked():
       os.system("sudo find ~/.cache/ -type f -atime +30 -delete")
def button5_clicked():
       subprocess.call(["sudo", "pacman", "-Scc", "--noconfirm"])
def button6_clicked():
       sys.exit()

if os.geteuid() != 0:
        exit("\nYou need to have root privileges to run this.\nPlease try again, this time using 'sudo'. Exiting.\n")

if __name__ == '__main__':
    window()
