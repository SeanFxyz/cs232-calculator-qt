import sys, re
from enum import Enum
from PySide2.QtCore import Qt, QCoreApplication, QFile, QObject
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QVBoxLayout, QHBoxLayout

class Op(Enum):
    NONE = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

class Calculator(QObject):
    def __init__(self, ui_file, parent=None):
        super().__init__()

        #load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.accText = self.window.findChild(QLineEdit, 'accumulatorText')
        self.storedText = self.window.findChild(QLabel, 'storedText')

        (self.window.findChild(QPushButton, 'zeroButton')
                .clicked.connect(self.on_zeroButton_clicked))
        (self.window.findChild(QPushButton, 'oneButton')
                .clicked.connect(self.on_oneButton_clicked))
        (self.window.findChild(QPushButton, 'twoButton')
                .clicked.connect(self.on_twoButton_clicked))
        (self.window.findChild(QPushButton, 'threeButton')
                .clicked.connect(self.on_threeButton_clicked))
        (self.window.findChild(QPushButton, 'fourButton')
                .clicked.connect(self.on_fourButton_clicked))
        (self.window.findChild(QPushButton, 'fiveButton')
                .clicked.connect(self.on_fiveButton_clicked))
        (self.window.findChild(QPushButton, 'sixButton')
                .clicked.connect(self.on_sixButton_clicked))
        (self.window.findChild(QPushButton, 'sevenButton')
                .clicked.connect(self.on_sevenButton_clicked))
        (self.window.findChild(QPushButton, 'eightButton')
                .clicked.connect(self.on_eightButton_clicked))
        (self.window.findChild(QPushButton, 'nineButton')
                .clicked.connect(self.on_nineButton_clicked))
        (self.window.findChild(QPushButton, 'addButton')
                .clicked.connect(self.on_addButton_clicked))
        (self.window.findChild(QPushButton, 'subtractButton')
                .clicked.connect(self.on_subtractButton_clicked))
        (self.window.findChild(QPushButton, 'multiplyButton')
                .clicked.connect(self.on_multiplyButton_clicked))
        (self.window.findChild(QPushButton, 'divideButton')
                .clicked.connect(self.on_divideButton_clicked))
        (self.window.findChild(QPushButton, 'equalsButton')
                .clicked.connect(self.on_equalsButton_clicked))
        (self.window.findChild(QPushButton, 'clearButton')
                .clicked.connect(self.on_clearButton_clicked))


        self.accumulator = 0
        self.stored_value = 0
        self.last_op = Op.NONE
        self.new_value = True
        self.update()

    def on_zeroButton_clicked(self):
        self.accumulate(0)
    def on_oneButton_clicked(self):
        self.accumulate(1)
    def on_twoButton_clicked(self):
        self.accumulate(2)
    def on_threeButton_clicked(self):
        self.accumulate(3)
    def on_fourButton_clicked(self):
        self.accumulate(4)
    def on_fiveButton_clicked(self):
        self.accumulate(5)
    def on_sixButton_clicked(self):
        self.accumulate(6)
    def on_sevenButton_clicked(self):
        self.accumulate(7)
    def on_eightButton_clicked(self):
        self.accumulate(8)
    def on_nineButton_clicked(self):
        self.accumulate(9)
    def on_addButton_clicked(self):
        self.on_equalsButton_clicked()
        self.last_op = Op.ADD
    def on_subtractButton_clicked(self):
        self.on_equalsButton_clicked()
        self.last_op = Op.SUBTRACT
    def on_multiplyButton_clicked(self):
        self.on_equalsButton_clicked()
        self.last_op = Op.MULTIPLY
    def on_divideButton_clicked(self):
        self.on_equalsButton_clicked()
        self.last_op = Op.DIVIDE
    def on_equalsButton_clicked(self):
        if self.last_op == Op.ADD:
            self.accumulator += self.stored_value
        elif self.last_op == Op.SUBTRACT:
            self.accumulator -= self.stored_value
        elif self.last_op == Op.MULTIPLY:
            self.accumulator *= self.stored_value
        elif self.last_op == Op.DIVIDE:
            self.accumulator /= self.stored_value
        self.update()
        self.new_value = True
        self.last_op = Op.NONE

    def on_clearButton_clicked(self):
        if self.new_value:
            self.stored_value = 0
            self.last_op = Op.NONE
            self.new_value == False
        else:
            self.accumulator = 0
            self.new_value == True
        self.update()

    def accumulate(self, n):
        if self.new_value:
            self.stored_value = self.accumulator
            self.accumulator = 0
            self.new_value = False
        else:
            self.new_value = True
        self.accumulator = self.accumulator * 10 + n
        self.update()

    def op_char(self, op):
        if op == Op.NONE:
            return ''
        if op == Op.ADD:
            return '+'
        if op == Op.SUBTRACT:
            return '-'
        if op == Op.MULTIPLY:
            return '*'
        if op == Op.DIVIDE:
            return '/'

    def update(self):
        self.accText.setText(str(self.accumulator))
        self.storedText.setText(str(self.stored_value) + ' ' + self.op_char(self.last_op))

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    calculator = Calculator('calculator.ui')
    calculator.window.show()
    sys.exit(app.exec_())
