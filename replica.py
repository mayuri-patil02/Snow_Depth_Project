from PyQt5 import QtWidgets
import sys


class Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.line_edits = []
        self.submit_button = QtWidgets.QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.on_submit)
        # add line edits and submit button to layout
        layout = QtWidgets.QVBoxLayout(self)
        for i in range(3):
            line_edit = QtWidgets.QLineEdit(self)
            self.line_edits.append(line_edit)
            layout.addWidget(line_edit)
        layout.addWidget(self.submit_button)

    def on_submit(self):
        for line_edit in self.line_edits:
            if line_edit.text() == '':
                print(f'LineEdit {line_edit.objectName()} is empty')
                return
        print('All LineEdits have valid input')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = Form()
    qt_app.show()
    app.exec_()
