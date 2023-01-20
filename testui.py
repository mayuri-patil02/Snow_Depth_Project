import os
import sys

import PySide2
import importlib_metadata
import lineedit as lineedit

from importlib_metadata import *

import self as self
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PySide2 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import *

import main
from main import *
from osgeo import ogr, gdal
import geopandas as gpd


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        # self.selected = None
        # self.line_edits = []
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Snow Depth Module")

        # Initialization of function for radio button state
        self.Pirrbtn.clicked.connect(self.pirpanjalFun)
        self.Ghrbtn.clicked.connect(self.greaterhFun)
        self.Kararbtn.clicked.connect(self.karakoramFun)

        # self.Pirrbtn.toggled.connect(lambda: self.select_radio(self.Pirrbtn))
        # self.Ghrbtn.toggled.connect(lambda: self.select_radio(self.Ghrbtn))
        # self.Kararbtn.toggled.connect(lambda :self.select_radio(self.Kararbtn))

        # Initialization of function for Upload Button
        self.upload_1.clicked.connect(self.file_Upload1)
        self.upload_2.clicked.connect(self.file_Upload2)
        self.upload_3.clicked.connect(self.file_Upload3)
        self.upload_4.clicked.connect(self.file_Upload4)
        self.upload_5.clicked.connect(self.file_Upload5)
        self.upload_6.clicked.connect(self.file_Upload6)
        self.upload_7.clicked.connect(self.file_Upload7)
        self.upload_8.clicked.connect(self.file_Upload8)
        self.upload_9.clicked.connect(self.file_Upload9)
        self.upload_10.clicked.connect(self.file_Upload10)
        # self.pushButton_11.clicked.connect(self.file_Upload11)
        # self.pushButton_12.clicked.connect(self.file_Upload12)

        # function for clearing the text in lineedit
        self.clearbtn.clicked.connect(self.clearText)

        # Initialization of function to perform action on Submit button
        self.submitbtn.clicked.connect(self.submitFun)

    # End of Init()
    def pirpanjalFun(self):

        # self.clearbtn.setEnabled(True)
        if self.Pirrbtn.isChecked():
            # source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\PirPanjal.shp')
            # boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\PirPanjal.shp')
            # print(boundFile)
            print('pirpanjal get clicked')
            # self.Ghrbtn.setChecked(False)
            # self.Kararbtn.setChecked(False)

    def greaterhFun(self):
        # self.clearbtn.setEnabled(True)
        if self.Ghrbtn.isChecked():
            # source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\GreaterHimalaya.shp')
            # boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\GreaterHimalaya.shp')
            # print(boundFile)
            print('greater himalaya get clicked')
            # self.Kararbtn.setChecked(False)
            # self.Pirrbtn.setChecked(False)

    def karakoramFun(self):
        # self.clearbtn.setEnabled(True)
        if self.Kararbtn.isChecked():
            # source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Karakoram.shp')
            # boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Karakoram.shp')
            # print(boundFile)
            print('korakoram get clicked')
            # self.Pirrbtn.setChecked(False)
            # self.Ghrbtn.setChecked(False)

    # QfileDialog used for browsing data take one push button and write function

    def file_Upload1(self):
        filename1 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_1.setText(str(filename1[0]))
        print(filename1)
        if self.lineEdit_1.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload2(self):
        # print("button pressed")
        filename2 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_2.setText(str(filename2[0]))
        print(filename2)
        if self.lineEdit_2.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload3(self):
        # print("button pressed")
        filename3 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_3.setText(str(filename3[0]))
        print(filename3)
        if self.lineEdit_3.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload4(self):
        # print("button pressed")
        filename4 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_4.setText(str(filename4[0]))
        print(filename4)
        if self.lineEdit_4.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload5(self):
        # print("button pressed")
        filename5 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_5.setText(str(filename5[0]))
        print(filename5)
        if self.lineEdit_5.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload6(self):
        # print("button pressed")
        filename6 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_6.setText(str(filename6[0]))
        print(filename6)
        if self.lineEdit_6.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload7(self):
        # print("button pressed")
        filename7 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_7.setText(str(filename7[0]))
        print(filename7)
        if self.lineEdit_7.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload8(self):
        # print("button pressed")
        filename8 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_8.setText(str(filename8[0]))
        print(filename8)
        if self.lineEdit_8.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload9(self):
        # print("button pressed")
        filename9 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_9.setText(str(filename9[0]))
        print(filename9)
        if self.lineEdit_9.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    def file_Upload10(self):
        # print("button pressed")
        filename10 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_10.setText(str(filename10[0]))
        print(filename10)
        if self.lineEdit_10.text():
            # print('file uploaded')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Uploaded Successfully")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Select file to Upload")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

    # function clearText and clear radio button selection on clear button
    def clearText(self):
        self.Pirrbtn.setAutoExclusive(False)
        self.Ghrbtn.setAutoExclusive(False)
        self.Kararbtn.setAutoExclusive(False)

        self.Pirrbtn.setChecked(False)
        self.Ghrbtn.setChecked(False)
        self.Kararbtn.setChecked(False)

        self.Pirrbtn.setAutoExclusive(True)
        self.Ghrbtn.setAutoExclusive(True)
        self.Kararbtn.setAutoExclusive(True)

        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()

    # Function for submit Button  code to check all files are selected or not
    def submitFun(self):
        line_edits = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5,
                      self.lineEdit_6, self.lineEdit_7, self.lineEdit_8, self.lineEdit_9, self.lineEdit_10]

        # Check if all line edit widgets have text entered
        if all(line_edit.text() for line_edit in line_edits):

            # Check if only one radio button is selected
            selected_count = sum([self.Pirrbtn.isChecked(), self.Ghrbtn.isChecked(), self.Kararbtn.isChecked()])
            if selected_count == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("you are ready to process output")
                msg.setWindowTitle("Success")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please select Only One Input Out of Three ")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please Upload all Input Files")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    sys.exit(app.exec_())
