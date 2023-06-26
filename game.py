from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QGridLayout
import sys

class TicTacToe(QMainWindow):
    def __init__(self):
        super(TicTacToe, self).__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(200, 200, 350, 350)
        self.button_list = []
        self.player = "X"
        self.initUI()

    def initUI(self):
        central_widget = QtWidgets.QWidget()
        layout = QGridLayout()
        for i in range(3):
            button_row = []
            for j in range(3):
                button = QtWidgets.QPushButton()
                button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                button.clicked.connect(lambda _, button=button: self.click_handler(button))
                layout.addWidget(button, i, j)
                layout.setRowStretch(i, 1)
                layout.setColumnStretch(j, 1)
                button_row.append(button)
            self.button_list.append(button_row)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def check_win(self):
        # Check rows for win
        for row in self.button_list:
            if row[0].text() == row[1].text() == row[2].text() != "":
                return True
        # Check columns for win
        for i in range(3):
            if self.button_list[0][i].text() == self.button_list[1][i].text() == self.button_list[2][i].text() != "":
                return True
        # Check diagonals for win
        if self.button_list[0][0].text() == self.button_list[1][1].text() == self.button_list[2][2].text() != "":
            return True
        if self.button_list[0][2].text() == self.button_list[1][1].text() == self.button_list[2][0].text() != "":
            return True
        return False

    def click_handler(self, button):
        if button.text() == "":
            button.setText(self.player)
            if self.check_win():
                QMessageBox.information(self, "Game Over", "Player {} wins!".format(self.player))
                if QMessageBox.question(self, "Game Over", "Do you want to play again?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    self.reset_game()
                else:
                    sys.exit()
            elif all(button.text() != "" for row in self.button_list for button in row):
                QMessageBox.information(self, "Game Over", "It's a tie!")
                if QMessageBox.question(self, "Game Over", "Do you want to play again?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    self.reset_game()
                else:
                    sys.exit()
            else:
                self.player = "O" if self.player == "X" else "X"

    def reset_game(self):
        self.player = "X"
        for row in self.button_list:
            for button in row:
                button.setText("")

def window():
    app = QApplication(sys.argv)
    win = TicTacToe()
    win.show()
    sys.exit(app.exec_())

window()
