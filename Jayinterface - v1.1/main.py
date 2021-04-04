# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets,uic
from jayui_main import Ui_MainWindow

from astar import whole_astar
from binary import whole_binarysearch
from insertion import insertionsort
# from linear import whole_linear
from bubble import  whole_bubble
from merge import whole_merge
from quick import whole_quick

import sys
import platform
# from PySide2 import  QtGui, QtWidgets
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
# from PySide2.QtWidgets import *
from ui_functions import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
            super(MainWindow,self).__init__()
            uic.loadUi('JayAlgorithmsVisualisationTool-master/JayAlgorithmsVisualisationTool-master/Jayinterface - v1.1/jayui.ui',self)

    ############################################


    ##################################################
            #------a star
            def astar():
                whole_astar()
            self.A_star.clicked.connect(astar)
            #--------
            # ------binary search
            def binary():
                whole_binarysearch()
            self.binary_search.clicked.connect(binary)
            # --------
            # ------insertion sort
            def insert_sort():
                insertionsort()
            self.insertion_sort.clicked.connect(insert_sort)
            # --------
            # MOVE WINDOW
            def moveWindow(event):
                # RESTORE BEFORE MOVE
                if UIFunctions.returnStatus() == 1:
                    UIFunctions.maximize_restore(self)

                # IF LEFT CLICK MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            # self.ui.title_bar.mouseMoveEvent = moveWindow
            self.A_star.setToolTip(
                "Important Instruction *****: Selct and two boxes in the grid and press space bar to get the path....!!A* pronounced as A star is a computer algorithm that is widely used in pathfinding and graph traversal. The algorithm efficiently plots a walkable path between multiple nodes, or points, on the graph.On a map with many obstacles, pathfinding from points AA to BB can be difficult. A robot, for instance, without getting much other direction, will continue until it encounters an obstacle, as in the path-finding example to the left below.However, the A* algorithm introduces a heuristic into a regular graph-searching algorithm, essentially planning ahead at each step so a more optimal decision is made.")
            self.merge_sort.setToolTip(
                "Merge sort is a sorting technique based on divide and conquer technique. With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms.Merge sort first divides the array into equal halves and then combines them in a sorted manner.")
            self.insertion_sort.setToolTip(
                "In an insertion sort, the first element in the array is considered as sorted, even if it is an unsorted array. In an insertion sort, each element in the array is checked with the previous elements, resulting in a growing sorted output list. With each iteration, the sorting algorithm removes one element at a time and finds the appropriate location within the sorted array and inserts it there. The iteration continues until the whole list is sorted.")
            self.bubble_sort.setToolTip(
                "Bubble sort is a sorting algorithm that works by repeatedly stepping through lists that need to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order. This passing procedure is repeated until no swaps are required, indicating that the list is sorted. Bubble sort gets its name because smaller elements bubble toward the top of the list.Bubble sort is also referred to as sinking sort or comparison sort.")
            self.quick_sort.setToolTip(
                "Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.")
            self.binary_search.setToolTip(
                "search algorithm works on the principle of divide and conquer. For this algorithm to work properly, the data collection should be in the sorted form.Binary search looks for a particular item by comparing the middle most item of the collection. If a match occurs, then the index of item is returned. If the middle item is greater than the item, then the item is searched in the sub-array to the left of the middle item. Otherwise, the item is searched for in the sub-array to the right of the middle item. This process continues on the sub-array as well until the size of the subarray reduces to zero.")

            ##################################################
            # # --------
            # ------bubble sort
            def buble():
                whole_bubble()

            self.bubble_sort.clicked.connect(buble)
            # --------
            # ------merge sort
            def merge():
                    whole_merge()

            self.merge_sort.clicked.connect(merge)
            # --------
            # ------quick sort
            def quick():
                whole_quick()

            self.quick_sort.clicked.connect(quick)
            # --------




            self.show()

    #
    # #------------------
    #
    # # MOVE WINDOW
    # def moveWindow(event):
    #     # RESTORE BEFORE MOVE
    #     if UIFunctions.returnStatus() == 1:
    #         UIFunctions.maximize_restore(self)
    #
    #     # IF LEFT CLICK MOVE WINDOW
    #     if event.buttons() == Qt.LeftButton:
    #         self.move(self.pos() + event.globalPos() - self.dragPos)
    #         self.dragPos = event.globalPos()
    #         event.accept()
    #
    #     # SET TITLE BAR
    #     self.ui.title_bar.mouseMoveEvent = moveWindow
    #
    #     ## ==> SET UI DEFINITIONS
    #     UIFunctions.uiDefinitions(self)
    #
    #     ## SHOW ==> MAIN WINDOW
    #     ########################################################################
    #     self.show()
    #
    # ## APP EVENTS
    # ########################################################################
    # def mousePressEvent(self, event):
    #     self.dragPos = event.globalPos()
    #
    #
    # #------------

app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
sys.exit(app.exec_())
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec_())


