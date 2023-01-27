import os
import sys

import pyproj
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PySide2 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import *

import main
from main import *
from osgeo import ogr, gdal
import geopandas as gpd
from osgeo import gdal, ogr
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
import pygeos
# geopandas.options.use_pygeos = True
import rasterio

from shapely.geometry import Point
from rasterio import plot
import pandas as pd
import scipy.stats
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import scipy.stats as stats
import xarray as xr
import rioxarray as rio


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        try:
            super(MyQtApp, self).__init__()
            self.setupUi(self)
            self.showMaximized()
            self.setWindowTitle("Snow Depth Module")

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
            # self.pushButton_11.clicked.connect(self.file_Upload11)
            # self.pushButton_12.clicked.connect(self.file_Upload12)

            # function for clearing the text in lineedit
            self.clearbtn.clicked.connect(self.clearText)

            # Initialization of function to perform action on Submit button
            self.submitbtn.clicked.connect(self.submitFun)

        except Exception as e:
            print(f"An error occurred: {e}")

    # End of Init()
    def pirpanjalFun(self):
        if self.Pirrbtn.isChecked():
            try:
                source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\PirPanjal.shp')
                boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\PirPanjal.shp')
                print(boundFile)
                print('pirpanjal get clicked')
                bound_project = boundFile.to_crs({'init': 'EPSG:4326'})
                # bound_project = boundFile.to_crs({'EPSG:4326'})
                spacing = 0.005
                xmin, ymin, xmax, ymax = bound_project.total_bounds
                xcoords = [i for i in np.arange(xmin, xmax, spacing)]
                ycoords = [i for i in np.arange(ymin, ymax, spacing)]
                print(bound_project.crs)
                print(bound_project.total_bounds)
                # pointcoords = np.array(np.meshgrid(xcoords, ycoords)).T.reshape(-1,
                #                                                                 2)  # A 2D array like [[x1,y1], [x1,y2], ...
                # points = gpd.points_from_xy(x=pointcoords[:, 0], y=pointcoords[:, 1])
                # grid = gpd.GeoSeries(points, crs=bound_project.crs)
                # grid.name = 'geometry'
                # gridinside = gpd.sjoin(gpd.GeoDataFrame(grid), bound_project[['geometry']], how="inner")
                # import matplotlib.pyplot as plt
                # fig, ax = plt.subplots(figsize=(15, 15))
                # bound_project.plot(ax=ax, alpha=0.7, color="pink", edgecolor='red', linewidth=1)
                # # grid.plot(ax=ax, markersize=150, color="blue")
                # df = pd.DataFrame()
                # df['LONGITUDE'] = gridinside['geometry'].x
                # df['LATITUDE'] = gridinside['geometry'].y
                # coord_list = [(x, y) for x, y in zip(gridinside['geometry'].x, gridinside['geometry'].y)]
                # gridinside.plot(ax=ax, markersize=10, color="yellow")
                # # print(gridinside.plot)

            except Exception as e:
                QMessageBox.warning(self, "Error", "An error occurred while trying to open the shapefile: {}".format(e))

    def greaterhFun(self):
        if self.Ghrbtn.isChecked():
            try:
                source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\GreaterHimalaya.shp')
                boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\GreaterHimalaya.shp')
                print(boundFile)
                print('greater himalaya get clicked')

            except Exception as e:
                QMessageBox.warning(self, "Error", "An error occurred while trying to open the shapefile: {}".format(e))

    def karakoramFun(self):
        if self.Kararbtn.isChecked():
            try:
                source_ds = ogr.Open(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Karakoram.shp')
                boundFile = gpd.read_file(r'D:\Srinivas\Mayuri\SnowDepth\shpfile\Karakoram.shp')
                print(boundFile)
                print('korakoram get clicked')

            except Exception as e:
                QMessageBox.warning(self, "Error", "An error occurred while trying to open the shapefile: {}".format(e))

    # QfileDialog used for browsing data take one push button and write function

    def file_Upload1(self):
        try:
            filename1 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_1.setText(str(filename1[0]))
            print(filename1)
            if self.lineEdit_1.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload2(self):
        try:
            filename2 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_2.setText(str(filename2[0]))
            print(filename2)
            if self.lineEdit_2.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload3(self):
        try:
            filename3 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_3.setText(str(filename3[0]))
            print(filename3)
            if self.lineEdit_3.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload4(self):
        try:
            filename4 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_4.setText(str(filename4[0]))
            print(filename4)
            if self.lineEdit_4.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload5(self):
        try:
            filename5 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_5.setText(str(filename5[0]))
            print(filename5)
            if self.lineEdit_5.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload6(self):
        try:
            filename6 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_6.setText(str(filename6[0]))
            print(filename6)
            if self.lineEdit_6.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload7(self):
        try:
            filename7 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_7.setText(str(filename7[0]))
            print(filename7)
            if self.lineEdit_7.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload8(self):
        try:
            filename8 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_8.setText(str(filename8[0]))
            print(filename8)
            if self.lineEdit_8.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")
            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload9(self):
        try:
            filename9 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_9.setText(str(filename9[0]))
            print(filename9)
            if self.lineEdit_9.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def file_Upload10(self):
        try:
            filename10 = QFileDialog.getOpenFileName(self, 'Open File', '', 'Tif File (*.tif)')
            self.lineEdit_10.setText(str(filename10[0]))
            print(filename10)
            if self.lineEdit_10.text():
                QMessageBox.information(self, "Information", "File Uploaded Successfully..")

            else:
                QMessageBox.warning(self, "Warning", "Please Select a File to Upload!")

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    # function clearText and clear radio button selection on clear button
    def clearText(self):
        try:
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

        except Exception as e:
            QMessageBox.warning(self, 'Error', 'An error occurred: {}'.format(e))

    # Function for submit Button  code to check all files are selected or not
    def submitFun(self):
        try:
            line_edits = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5,
                          self.lineEdit_6, self.lineEdit_7, self.lineEdit_8, self.lineEdit_9, self.lineEdit_10]

            # Check if all line edit widgets have text entered
            if all(line_edit.text() for line_edit in line_edits):

                # Check if only one radio button is selected
                selected_count = sum([self.Pirrbtn.isChecked(), self.Ghrbtn.isChecked(), self.Kararbtn.isChecked()])
                if selected_count == 1:
                    QMessageBox.information(self, "Information", "Process towards output...")
                else:
                    QMessageBox.warning(self, "Warning", "Please select Only One Input Out of Three")

            else:

                QMessageBox.warning(self, "Warning", "Please Upload all Input Files")

        except Exception as e:

            QMessageBox.warning(self, 'Error', str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    sys.exit(app.exec_())
