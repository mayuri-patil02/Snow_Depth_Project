import sys

from PyQt5.QtWidgets import QFileDialog
from PySide2 import QtWidgets

import main
from main import *
from osgeo import ogr, gdal
import geopandas as gpd


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Snow Depth Module")
        # Initialization of function for radio button state

        self.Pirrbtn.clicked.connect(self.pirpanjalFun)
        self.Ghrbtn.clicked.connect(self.greaterhFun)
        self.Kararbtn.clicked.connect(self.karakoramFun)



        # self.Pirrbtn.toggled.connect(lambda: self.btnstate(Pirrbtn))
        # self.Ghrbtn.toggled.connect(lambda: self.btnstate(self.Ghrbtn))
        # self.Kararbtn.toggled.connect(lambda: self.btnstate(self.Kararbtn))
        # Initialization of function for pushButton
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
        # self.clear.clicked.connect(self.clearText)
        # self.pushButton_11.clicked.connect(self.file_Upload11)
        # self.pushButton_12.clicked.connect(self.file_Upload12)

    def pirpanjalFun(self):
        if self.Pirrbtn.isChecked():
            source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
            boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
            print(boundFile)
            print('pirpanjal get clicked')

    def greaterhFun(self):
        if self.Ghrbtn.isChecked():
            source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
            boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
            print(boundFile)

            # source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Greater_Himalaya.shp')
            # boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Greater_Himalaya.shp')
            # print(boundFile)
            # print('greater himalaya get clicked')

    def karakoramFun(self):
        if self.Kararbtn.isChecked():
            source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
            boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
            print(boundFile)
            print('korakoram get clicked')

    # def btnstate(self, b):

    # if b.isChecked():
    #     source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
    #     boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
    #     print(boundFile.head())
    #
    #     # source_ds = ogr.Open(r"D:\Srinivas\Mayuri\SnowDepth\shpfile\Greater_Himalaya.shp")
    #     # boundFile = gpd.read_file(r"\Srinivas\Mayuri\SnowDepth\shpfile\Greater_Himalaya.shp")
    #     # print(boundFile)
    #     print(b.text(), "get clicked")
    # if b.isChecked():
    #     print(b.text(), "get clicked")
    # if b.isChecked():
    #     print(b.text(), "get clicked")

    # QfileDialog used for browsing data take one push button and write function

    def file_Upload1(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_1.setText(str(filename[0]))
        print(filename)
        # filename = QFileDialog.getOpenFileNames(self, 'Image Files (*.tif)')



        # self.lineEdit_1.setText(str(filename[0]))
        # print(filename[0])

    def file_Upload2(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_2.setText(str(filename[0]))
        print(filename)

    def file_Upload3(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_3.setText(str(filename[0]))
        print(filename)

    def file_Upload4(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_4.setText(str(filename[0]))
        print(filename)
    def file_Upload5(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_5.setText(str(filename[0]))
        print(filename)

    def file_Upload6(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_6.setText(str(filename[0]))
        print(filename)

    def file_Upload7(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_7.setText(str(filename[0]))
        print(filename)
    def file_Upload8(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_8.setText(str(filename[0]))
        print(filename)

    def file_Upload9(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_9.setText(str(filename[0]))
        print(filename)

    def file_Upload10(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
        self.lineEdit_10.setText(str(filename[0]))
        print(filename)

    #funcion clearText for clear button
    # def clearText(self):
    #     if

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
