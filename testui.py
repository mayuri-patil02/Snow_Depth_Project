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
        self.Pirrbtn.toggled.connect(lambda: self.btnstate(self.Pirrbtn))
        self.Ghrbtn.toggled.connect(lambda: self.btnstate(self.Ghrbtn))
        self.Kararbtn.toggled.connect(lambda: self.btnstate(self.Kararbtn))
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
        # self.pushButton_11.clicked.connect(self.file_Upload11)
        # self.pushButton_12.clicked.connect(self.file_Upload12)

    def btnstate(self, b):
        if b.isChecked():
            source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
            boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\merged_himalaya.shp')
            print(boundFile.head())
            

            # source_ds = ogr.Open(r"D:\Srinivas\Mayuri\SnowDepth\shpfile\Greater_Himalaya.shp")
            # boundFile = gpd.read_file(r"\Srinivas\Mayuri\SnowDepth\shpfile\Greater_Himalaya.shp")
            # print(boundFile)
            print(b.text(), "get clicked")
        if b.isChecked() == "Ghrbtn":
            print(b.text(), "get clicked")
        if b.isChecked() == "Kararbtn":
            print(b.text(), "get clicked")

    # QfileDialog used for browsing data take one push button and write function

    def file_Upload1(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)
        # filename = QFileDialog.getOpenFileNames(self, 'open file', 'D:\Srinivas\Mayuri\Feb2_2019')
        # self.lineEdit.setText(filename[0])
        # self.open_File()

    def file_Upload2(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)

    def file_Upload3(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)

    def file_Upload4(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)

    def file_Upload5(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)

    def file_Upload6(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)

    def file_Upload7(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)

    def file_Upload8(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)

    def file_Upload9(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)

    def file_Upload10(self):
        # print("button pressed")
        filename = QFileDialog.getOpenFileNames()
        path = filename[0]
        print(path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
