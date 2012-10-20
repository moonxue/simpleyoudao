# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ydwin import Ui_winMain
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QIcon, QSystemTrayIcon, QAction, QMenu
from threading import Thread
from os import popen,system
from time import sleep
import requests
import json
import sys


class Windows(QtGui.QMainWindow):
			
	def mousePressEvent(self,event):
		#鼠标点击事件
		if event.button() == QtCore.Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			event.accept()
	def mouseMoveEvent(self,event):
		#鼠标移动事件
		if event.buttons() ==QtCore.Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()
			
	
		
class StartQT4(Windows):
	
	def keyPressEvent(self, event):
		k = event.key() 
		if k == QtCore.Qt.Key_Escape:
			sys.exit()
		elif k == QtCore.Qt.Key_Enter-1:
			self.ui.btnSend.clicked.emit(True)
			
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_winMain()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.btnSend, QtCore.SIGNAL("clicked()"), self.SendQuery)
		self.setMouseTracking(True)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint| Qt.Popup | Qt.Tool)
		
		# 创建托盘
		self.icon = QIcon("img.png")
		self.trayIcon = QSystemTrayIcon(self)
		self.trayIcon.setIcon(self.icon)
		self.trayIcon.setToolTip(u"simple有道")
		self.trayIcon.show()
		# 托盘气泡消息
		self.trayIcon.showMessage(u"simple有道", u"simple有道已经启动，随时待命！")
		# 托盘菜单
		self.action = QAction(u"退出simple有道", self, triggered = sys.exit) # 触发点击后调用sys.exit()命令，即退出
		self.menu = QMenu(self)
		self.menu.addAction(self.action)
		self.trayIcon.setContextMenu(self.menu)
		self.move(1100,50)
		#开启监听线程
		system("xclip -f /dev/null")           #清空剪切板
		listener = Thread(target=listenMouse, args=(self.ui,))
		listener.setDaemon(True)
		listener.start()
        
	def SendQuery(self):
		querystring = "http://fanyi.youdao.com/openapi.do?keyfrom=hustbg&key=1205943053&type=data&doctype=json&version=1.1&q="+unicode(self.ui.txtSend.text())
		response = json.loads(requests.get(querystring).text)
		try:
			result = u"   音标:"+response["basic"].get("phonetic","")+u"\n   翻译:"+u','.join(response["translation"])+u"\n   解释:\n   "+'\n   '.join(response["basic"]["explains"][0:2])
			self.ui.labresult.setText(result)
		except:
			self.ui.labresult.setText(u"没有查到相关记录")
			
			
def listenMouse(ui):
	history=""
	while(True):
		pipe = popen("xclip -o")
		st = pipe.readline()
		try:
			st = st.decode('utf8')
		except:
			try:
				st =st.decode('gbk')
			except:
				try:
					st=unicode(st)
				except:
					st=history
		pipe.readlines()    #清空管道剩余部分
		pipe.close()
		if st != history:
			ui.txtSend.setText(st)
			ui.btnSend.clicked.emit(True)
		history = st
		sleep(2)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
	
