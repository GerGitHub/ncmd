# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(346, 208)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isPhone = QtWidgets.QRadioButton(self.groupBox)
        self.isPhone.setChecked(True)
        self.isPhone.setObjectName("isPhone")
        self.horizontalLayout.addWidget(self.isPhone)
        self.isEmail = QtWidgets.QRadioButton(self.groupBox)
        self.isEmail.setObjectName("isEmail")
        self.horizontalLayout.addWidget(self.isEmail)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.actEdit = QtWidgets.QLineEdit(Dialog)
        self.actEdit.setObjectName("actEdit")
        self.horizontalLayout_2.addWidget(self.actEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pwdEdit = QtWidgets.QLineEdit(Dialog)
        self.pwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdEdit.setClearButtonEnabled(False)
        self.pwdEdit.setObjectName("pwdEdit")
        self.horizontalLayout_3.addWidget(self.pwdEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.skipBtn = QtWidgets.QPushButton(Dialog)
        self.skipBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.skipBtn.setObjectName("skipBtn")
        self.horizontalLayout_4.addWidget(self.skipBtn)
        self.loginBtn = QtWidgets.QPushButton(Dialog)
        self.loginBtn.setEnabled(False)
        self.loginBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout_4.addWidget(self.loginBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.groupBox.setTitle(_translate("Dialog", "登录方式"))
        self.isPhone.setText(_translate("Dialog", "手机号"))
        self.isEmail.setText(_translate("Dialog", "邮箱"))
        self.label.setText(_translate("Dialog", "账号"))
        self.actEdit.setText(_translate("Dialog", "17051050346"))
        self.actEdit.setPlaceholderText(_translate("Dialog", "手机号/邮箱"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.pwdEdit.setText(_translate("Dialog", "54385462YZFbmh"))
        self.pwdEdit.setPlaceholderText(_translate("Dialog", "密码"))
        self.skipBtn.setText(_translate("Dialog", "跳过"))
        self.loginBtn.setText(_translate("Dialog", "登录"))
