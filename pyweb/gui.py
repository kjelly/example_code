#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os.path
from PySide import QtGui, QtCore, QtWebKit


class WebviewDemo(QtGui.QWidget):

    def __init__(self):
        super(WebviewDemo, self).__init__()

        self.initUI()
        self.initEvent()
        self.initJavascriptEnv()

        self.web.page().mainFrame().javaScriptWindowObjectCleared.connect(
                self.initJavascriptEnv)

        path = os.path.dirname(__file__)
        self.web.load(QtCore.QUrl('file:///%s/demo.html' % path))

    def initUI(self):

        self.web = QtWebKit.QWebView()

        self.code_input_label = QtGui.QLabel("Code input: ")
        self.code_input = QtGui.QLineEdit()
        self.output_window = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()

        grid.addWidget(self.web, 0, 0, 14, 10)
        grid.addWidget(self.code_input_label, 14, 0, 1, 1)
        grid.addWidget(self.code_input, 14, 1, 1, 9)
        grid.addWidget(self.output_window, 15, 0, 1, 10)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('WebviewDemo')
        self.show()

    def initEvent(self):
        self.code_input.returnPressed.connect(self.evalJavascript)

    @QtCore.Slot(result=str)
    def evalJavascript(self):
        ''' When user input javascript code in code_input and press enter,
        it will call the function.
        '''
        code = self.code_input.text()
        page = self.web.page()
        frame = page.currentFrame()
        # run javascript code and get result.
        result =frame.evaluateJavaScript(code)
        self.output_window.append(str(result) + '\n')

    def initJavascriptEnv(self):
        page = self.web.page()
        frame = page.mainFrame()
        # Add self object into javascript runtime.
        # So the "self" object  in javascript means the "self" instance in python.
        # Note: the "self"" objeect is maybe invalid after loading new url.
        # So check
        frame.addToJavaScriptWindowObject("self", self)

    # Any function which want to be called by javascript, it need to be wrapped by QtCore.Slot.
    # If You use C++ and Qt, you also need Q_INVOKABLE macro.
    @QtCore.Slot(result=str)
    def sayHello(self):
        print 'you call python function.'
        return 'hello'

    @QtCore.Slot(result=str)
    def submit(self):
        print 'sss'
        page = self.web.page()
        frame = page.currentFrame()
        user_input = frame.findFirstElement("#fullname").evaluateJavaScript("this.value")
        QtGui.QMessageBox.warning(self, "Qt Message Box", user_input)
        return ''




def main():
    app = QtGui.QApplication(sys.argv)
    widget =  WebviewDemo()
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()