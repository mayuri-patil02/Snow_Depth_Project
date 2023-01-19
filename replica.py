from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button Example")
        self.resize(300, 100)

        # Create radio buttons
        self.radio_button_1 = QtWidgets.QRadioButton("Option 1", self)
        self.radio_button_2 = QtWidgets.QRadioButton("Option 2", self)
        self.radio_button_3 = QtWidgets.QRadioButton("Option 3", self)

        # Add radio buttons to a button group
        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)
        self.button_group.addButton(self.radio_button_3)

        # Create a layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.radio_button_1)
        layout.addWidget(self.radio_button_2)
        layout.addWidget(self.radio_button_3)

        self.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
