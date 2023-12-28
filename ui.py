# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1180, 600)
        self.matting_tool = QtWidgets.QGroupBox(Dialog)
        self.matting_tool.setGeometry(QtCore.QRect(30, 10, 1111, 561))
        self.matting_tool.setObjectName("matting_tool")
        self.fg = QtWidgets.QGraphicsView(self.matting_tool)
        self.fg.setGeometry(QtCore.QRect(10, 40, 260, 192))
        self.fg.setObjectName("fg")
        self.seg = QtWidgets.QGraphicsView(self.matting_tool)
        self.seg.setGeometry(QtCore.QRect(280, 40, 260, 192))
        self.seg.setObjectName("seg")
        self.alpha = QtWidgets.QGraphicsView(self.matting_tool)
        self.alpha.setGeometry(QtCore.QRect(10, 320, 260, 192))
        self.alpha.setObjectName("alpha")
        self.bg = QtWidgets.QGraphicsView(self.matting_tool)
        self.bg.setGeometry(QtCore.QRect(280, 320, 260, 192))
        self.bg.setObjectName("bg")
        self.select_fg = QtWidgets.QPushButton(self.matting_tool)
        self.select_fg.setGeometry(QtCore.QRect(10, 240, 131, 30))
        self.select_fg.setObjectName("select_fg")
        self.gen_tri = QtWidgets.QPushButton(self.matting_tool)
        self.gen_tri.setGeometry(QtCore.QRect(680, 240, 125, 30))
        self.gen_tri.setMouseTracking(False)
        self.gen_tri.setObjectName("gen_tri")
        self.select_tri = QtWidgets.QPushButton(self.matting_tool)
        self.select_tri.setGeometry(QtCore.QRect(560, 240, 105, 30))
        self.select_tri.setMouseTracking(False)
        self.select_tri.setObjectName("select_tri")
        self.pre_alpha = QtWidgets.QPushButton(self.matting_tool)
        self.pre_alpha.setGeometry(QtCore.QRect(70, 520, 140, 30))
        self.pre_alpha.setMouseTracking(False)
        self.pre_alpha.setObjectName("pre_alpha")
        self.select_bg = QtWidgets.QPushButton(self.matting_tool)
        self.select_bg.setGeometry(QtCore.QRect(340, 520, 140, 30))
        self.select_bg.setMouseTracking(False)
        self.select_bg.setObjectName("select_bg")
        self.com = QtWidgets.QPushButton(self.matting_tool)
        self.com.setGeometry(QtCore.QRect(610, 520, 140, 30))
        self.com.setMouseTracking(False)
        self.com.setObjectName("com")
        self.com_res = QtWidgets.QGraphicsView(self.matting_tool)
        self.com_res.setGeometry(QtCore.QRect(550, 320, 260, 192))
        self.com_res.setObjectName("com_res")
        self.crop_fg = QtWidgets.QPushButton(self.matting_tool)
        self.crop_fg.setGeometry(QtCore.QRect(140, 240, 131, 28))
        self.crop_fg.setObjectName("crop_fg")
        self.spinBox_size = QtWidgets.QSpinBox(self.matting_tool)
        self.spinBox_size.setEnabled(True)
        self.spinBox_size.setGeometry(QtCore.QRect(1010, 50, 51, 30))
        self.spinBox_size.setAccessibleName("")
        self.spinBox_size.setAccessibleDescription("")
        self.spinBox_size.setSpecialValueText("")
        self.spinBox_size.setSuffix("")
        self.spinBox_size.setPrefix("")
        self.spinBox_size.setMinimum(10)
        self.spinBox_size.setMaximum(30)
        self.spinBox_size.setProperty("value", 20)
        self.spinBox_size.setObjectName("spinBox_size")
        self.spinBox_num_iters = QtWidgets.QSpinBox(self.matting_tool)
        self.spinBox_num_iters.setEnabled(True)
        self.spinBox_num_iters.setGeometry(QtCore.QRect(1000, 90, 51, 30))
        self.spinBox_num_iters.setAccessibleName("")
        self.spinBox_num_iters.setAccessibleDescription("")
        self.spinBox_num_iters.setSpecialValueText("")
        self.spinBox_num_iters.setSuffix("")
        self.spinBox_num_iters.setPrefix("")
        self.spinBox_num_iters.setMaximum(10)
        self.spinBox_num_iters.setObjectName("spinBox_num_iters")
        self.comboBox = QtWidgets.QComboBox(self.matting_tool)
        self.comboBox.setGeometry(QtCore.QRect(830, 90, 91, 30))
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.matting_tool)
        self.label.setGeometry(QtCore.QRect(930, 90, 81, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.matting_tool)
        self.label_2.setGeometry(QtCore.QRect(830, 50, 191, 30))
        self.label_2.setObjectName("label_2")
        self.tri = QtWidgets.QGraphicsView(self.matting_tool)
        self.tri.setGeometry(QtCore.QRect(550, 40, 260, 192))
        self.tri.setObjectName("tri")
        self.groupBox = QtWidgets.QGroupBox(self.matting_tool)
        self.groupBox.setGeometry(QtCore.QRect(850, 280, 221, 231))
        self.groupBox.setObjectName("groupBox")
        self.save_tri = QtWidgets.QPushButton(self.groupBox)
        self.save_tri.setGeometry(QtCore.QRect(20, 40, 151, 28))
        self.save_tri.setMouseTracking(False)
        self.save_tri.setObjectName("save_tri")
        self.save_alpha = QtWidgets.QPushButton(self.groupBox)
        self.save_alpha.setGeometry(QtCore.QRect(20, 80, 151, 28))
        self.save_alpha.setMouseTracking(False)
        self.save_alpha.setObjectName("save_alpha")
        self.save_com = QtWidgets.QPushButton(self.groupBox)
        self.save_com.setGeometry(QtCore.QRect(20, 120, 151, 28))
        self.save_com.setMouseTracking(False)
        self.save_com.setObjectName("save_com")
        self.save_com_pure = QtWidgets.QPushButton(self.groupBox)
        self.save_com_pure.setGeometry(QtCore.QRect(20, 160, 151, 61))
        self.save_com_pure.setMouseTracking(False)
        self.save_com_pure.setObjectName("save_com_pure")
        self.gen_seg = QtWidgets.QPushButton(self.matting_tool)
        self.gen_seg.setGeometry(QtCore.QRect(330, 240, 151, 30))
        self.gen_seg.setMouseTracking(False)
        self.gen_seg.setObjectName("gen_seg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.matting_tool.setTitle(_translate("Dialog", "Matting"))
        self.select_fg.setText(_translate("Dialog", "Select Foreground"))
        self.gen_tri.setText(_translate("Dialog", "Generate Trimap"))
        self.select_tri.setText(_translate("Dialog", "Select Trimap"))
        self.pre_alpha.setText(_translate("Dialog", "Predict Alpha Matte"))
        self.select_bg.setText(_translate("Dialog", "Select Background"))
        self.com.setText(_translate("Dialog", "Compose"))
        self.crop_fg.setText(_translate("Dialog", "Crop Foreground"))
        self.comboBox.setCurrentText(_translate("Dialog", "None"))
        self.comboBox.setItemText(0, _translate("Dialog", "None"))
        self.comboBox.setItemText(1, _translate("Dialog", "Dilation"))
        self.comboBox.setItemText(2, _translate("Dialog", "Erosion"))
        self.label.setText(_translate("Dialog", "Num Iters : "))
        self.label_2.setText(_translate("Dialog", "Unknown Region Thickness : "))
        self.groupBox.setTitle(_translate("Dialog", "Save Result"))
        self.save_tri.setText(_translate("Dialog", "Save Trimap"))
        self.save_alpha.setText(_translate("Dialog", "Save Alpha Matte"))
        self.save_com.setText(_translate("Dialog", "Save Compose Image"))
        self.save_com_pure.setText(_translate("Dialog", "Save Image with\n"
" Transparent Background"))
        self.gen_seg.setText(_translate("Dialog", "Generate Segement"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
