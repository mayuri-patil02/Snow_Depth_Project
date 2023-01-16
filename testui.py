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
        self.selected = None
        self.line_edits = []
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Snow Depth Module")
        msg = QMessageBox()
        # PySide2.QtWidgets.QLineEdit.setValidator(arg__1)

        # Initialization of function for radio button state
        self.Pirrbtn.clicked.connect(self.pirpanjalFun)
        self.Ghrbtn.clicked.connect(self.greaterhFun)
        self.Kararbtn.clicked.connect(self.karakoramFun)

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

        # function for clearing the text in lineedit

        # self.lineedit.clicked.connect(self.lineedit.clear)
        self.clearbtn.clicked.connect(self.clearText)
        # self.pushButton_11.clicked.connect(self.file_Upload11)
        # self.pushButton_12.clicked.connect(self.file_Upload12)

        # Initialization of function to perform action on Submit button
        self.submitbtn.clicked.connect(self.submitFun)
        # self.selected_option = QtWidgets.QLabel("", self)
        # self.selected_option.move(10, 170)
        # # files = ["file1.tif", "file2.tif", "file3.tif"]
        # for i in range(11):
        #     line_edit = QtWidgets.QLineEdit(self)
        #     self.line_edits.append(line_edit)

    def pirpanjalFun(self):
        if self.Pirrbtn.isChecked():
            source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\PirPanjal.shp')
            boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\PirPanjal.shp')
            print(boundFile)
            print('pirpanjal get clicked')
            # self.selected_option.clear()

    def greaterhFun(self):
        if self.Ghrbtn.isChecked():
            source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\GreaterHimalaya.shp')
            boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\GreaterHimalaya.shp')
            print(boundFile)

            # source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Greater_Himalaya.shp')
            # boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Greater_Himalaya.shp')
            # print(boundFile)
            print('greater himalaya get clicked')
            # self.selected_option.clear()

    def karakoramFun(self):
        if self.Kararbtn.isChecked():
            source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Karakoram.shp')
            boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Karakoram.shp')
            print(boundFile)
            print('korakoram get clicked')
            # self.selected_option.clear()

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
        # do something if the line edit is empty.

        # filename = QFileDialog.getOpenFileNames(self, 'Image Files (*.tif)')

        # self.lineEdit_1.setText(str(filename[0]))
        # print(filename[0])

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

    # function clearText for clear button
    def clearText(self):
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
        self.Pirrbtn.setChecked(False)
        # print(self.Pirrbtn.text())
        self.Ghrbtn.setChecked(False)
        self.Kararbtn.setChecked(False)


    # Function for submit Button  code to check all files are selected or not
    def submitFun(self,selected):
        # code to check all whether one radio button out of three is selected or not on submit
        self.selected = ""
        if self.Pirrbtn.isChecked():
            selected = "PirPanjal"
            # self.selected_option.clear()
        elif self.Ghrbtn.isChecked():
            selected = "GreaterHimalaya"
            # self.selected_option.clear()
        elif self.Kararbtn.isChecked():
            selected = "Karakoram"
            # self.selected_option.clear()

        if selected:
            pass
            # self.selected_option.setText('input selcted')
            # self.selected_option.clear()
            # print(selected, 'is clicked')
            # # Show the selected option
            # msg = QMessageBox()
            # msg.setIcon(QMessageBox.Information)
            # # msg.setText(self.selected, "is Selected")
            # msg.setText('input is selected')
            # msg.setWindowTitle("Info")
            # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # retval = msg.exec_()

        else:
            pass
            # self.selected_option.setText("Please select an option")
            # self.selected_option.clear()
            # msg = QMessageBox()
            # msg.setIcon(QMessageBox.Information)
            # # msg.setText('Please Select valid input')
            # msg.setWindowTitle("Warning")
            # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # retval = msg.exec_()
        # # Show the message if no option is selected

        #
        # # code to check all files are uploaded and one among three radio button selected or not
        if self.lineEdit_1.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text() and self.lineEdit_5.text() and self.lineEdit_6.text() and self.lineEdit_7.text() and self.lineEdit_8.text() and self.lineEdit_9.text() and self.lineEdit_10.text() and selected:
            print('process to output')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("you are ready to process output")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please select input and upload all files related to input")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    sys.exit(app.exec_())
