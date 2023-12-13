# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import time
from threading import Thread
import mythread
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

import mythread
from comm import sendUdp


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 296)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(220, 30, 121, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 110, 121, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 200, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.btn3_click)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 200, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.btn4_click)  # 将停止按钮的点击事件连接到 btn4_click 函数
        # self.pushButton_4.clicked.connect(self.stop_threads)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.thread01 = Thread(target=mythread.target01, args="参数1", name="线程1")
        # self.thread01 = Thread(target=mythread.target01)
        # self.thread02 = Thread(target=mythread.target02)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "接包率"))
        self.pushButton_2.setText(_translate("Dialog", "误码率"))
        self.pushButton_3.setText(_translate("Dialog", "开始"))
        self.pushButton_4.setText(_translate("Dialog", "停止"))

    def btn3_click(self):
        try:

            self.thread01.start()  # 启动线程
            ui.textEdit.setPlainText(mythread.count_str)
            ui.textEdit_2.setPlainText(mythread.ber_str)
            self.timer_start() # 启动时间间隔

        except RuntimeError as e:
            print("----------------------发生了异常------------")
            popup = MyPopupWindow()
            popup.exec_()

    def btn4_click(self):
        ui.textEdit.clear()
        ui.textEdit_2.clear()
        print("cancel")

    # 启动定时器 时间间隔秒
    def timer_start(self):
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.updataData)
        self.timer.start(50)  # 50ms 更新一次

    # 更新数据
    def updataData(self):
        # ui.textEdit.setPlainText(str(111))
        # ui.textEdit_2.setPlainText(str(222))
        ui.textEdit.setPlainText(mythread.count_str)
        print("接受次数：", mythread.count_str)
        ui.textEdit_2.setPlainText(mythread.ber_str)

    #杀死线程
    def btn4_click(self):  # 新增的停止按钮点击事件处理函数
        self.timer.stop()  # 停止定时器
        mythread.stop_flag = True  # 设置停止标志为True
        self.thread01.join()  # 等待线程1结束
        # self.thread02.join()  # 等待线程2结束
        print("Threads stopped")
        sys.exit(0)  # 通过sys.exit()来退出程序
        MainWindow.close()  # 手动关闭主窗口
    def stop_threads(self):
        mythread.stop_flag = True  # 设置停止标志为True
        self.thread01.join()  # 等待线程1结束
        # self.thread02.join()  # 等待线程2结束
class MyPopupWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("弹出窗口")
        self.setGeometry(100, 100, 300, 200)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel("请勿重复点击")
        layout.addWidget(label)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
