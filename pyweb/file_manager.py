#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os
import os.path
import json
from PySide import QtGui, QtCore, QtWebKit


class FileManager(QtGui.QWidget):

    def __init__(self, path):
        super(FileManager, self).__init__()
        if not os.path.exists(path):
            raise Exception("invalid path")
        self.current_path = path

        self.initUI()
        self.initEvent()
        self.initJavascriptEnv()

        self.web.page().mainFrame().javaScriptWindowObjectCleared.connect(
                self.initJavascriptEnv)

        path = os.path.dirname(__file__)
        self.web.load(QtCore.QUrl('file:///%s/file_manager.html' % path))
        #self.web.load(QtCore.QUrl('http://yuilibrary.com/yui/docs/app/app-todo.html'))

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

    @QtCore.Slot(str, result=str)
    def cd(self, new_path):
        new_path =  os.path.abspath(new_path)
        if not os.path.isdir(new_path):
            raise Exception("invalid path")
        self.current_path = new_path if new_path[-1] == '/' else new_path + '/'
        return self.list_dir(self.current_path)

    @QtCore.Slot(str, result=str)
    def list_dir(self, path):
        entry = ['..']
        entry.extend(os.listdir(path))
        return json.dumps({'current_path': path, 'entrys': map(lambda s: {'entry': s}, entry)})

    @QtCore.Slot(result=str)
    def get_current_path(self):
        return self.current_path


def main():
    app = QtGui.QApplication(sys.argv)
    widget = FileManager(os.path.dirname(__file__))
    widget.show()
    print widget.cd(os.path.dirname(__file__))
    print widget.list_dir(os.path.dirname(__file__))

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()