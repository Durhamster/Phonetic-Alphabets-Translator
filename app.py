import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QComboBox,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QPlainTextEdit,
)
from alphabets import (
    nato_alphabet,
    raf_1921,
    uk_navy_1917,
    us_army_1916,
    us_army_1943,
    us_navy_1913,
    us_navy_1938,
    us_navy_WWII
)

def spelling(alphabet, self):
    word_phrase = []
    if alphabet == "NATO":
        alphabet = nato_alphabet
    elif alphabet == "RAF 1921":
        alphabet = raf_1921
    elif alphabet == "UK Navy 1917":
        alphabet = uk_navy_1917
    elif alphabet == "US Army 1916":
        alphabet = us_army_1916
    elif alphabet == "US Army 1943":
        alphabet = us_army_1943
    elif alphabet == "US Navy 1913":
        alphabet = us_navy_1913
    elif alphabet == "US Navy 1938":
        alphabet = us_navy_1938
    elif alphabet == "US Navy WWII":
        alphabet = us_navy_WWII


    for letter in self.line.text():
        letter = letter.lower()

        if letter not in alphabet:
            word_phrase.append(letter)
        else:
            word_phrase.append(alphabet[letter])

    # Convert list into single string
    final_spelling = " ".join(word_phrase)
    self.spelling_output.clear()
    self.spelling_output.insertPlainText(final_spelling)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(520, 360))
        self.setWindowIcon(QtGui.QIcon("assets/Globe_icon.svg"))
        self.setWindowTitle("Historical Alphabet Speller")

        # Dropdown line
        self.alphabet_label = QLabel(self)
        self.alphabet_label.setText("Select an alphabet:")
        self.alphabet_label.move(10, 10)

        # Dropdown box
        self.dropDown = QComboBox(self)
        self.dropDown.move(130, 10)
        self.dropDown.addItem("NATO")
        self.dropDown.addItem("RAF 1921")
        self.dropDown.addItem("UK Navy 1917")
        self.dropDown.addItem("US Army 1916")
        self.dropDown.addItem("US Army 1943")
        self.dropDown.addItem("US Navy 1913")
        self.dropDown.addItem("US Navy 1938")
        self.dropDown.addItem("US Navy WWII")

        # Word/Phrase line
        self.nameLabel = QLabel(self)
        self.nameLabel.setText("Enter a word or phrase:")
        self.nameLabel.move(10, 60)
        self.nameLabel.adjustSize()

        # Word/Phrase Input
        self.line = QLineEdit(self)
        self.line.move(130, 50)
        self.line.resize(200, 32)

        # Submit Button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.clickMethod)
        self.submit_button.adjustSize()
        self.submit_button.move(130, 100)

        # Spelling Output line
        self.spelling_line = QLabel(self)
        self.spelling_line.setText("Copy spelling:")
        self.spelling_line.move(50, 150)

        # Spelling Output
        self.spelling_output = QPlainTextEdit(self)
        self.spelling_output.move(130, 150)
        self.spelling_output.adjustSize()

    def clickMethod(self):
        alphabet = self.dropDown.currentText()
        spelling(alphabet, self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
