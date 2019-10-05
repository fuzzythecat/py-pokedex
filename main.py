import sys
from PyQt5.QtWidgets import QApplication
from pokedex import QPokedex


def main():
    app = QApplication(sys.argv)

    window = QPokedex(745, 540)

    window.show()
    return app.exec_()


if __name__ == "__main__":
    main()
