from PyQt5.QtGui import QPalette, QPixmap, QBrush
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import QSize, Qt


class QPokedex(QMainWindow):

    POKEDEX_IMG = "gui/images/pokedex.png"

    def __init__(self, width, height):
        super(QPokedex, self).__init__()

        # initialize the window
        self.set_size(width, height)
        self.set_window_title("Pokedex")
        self.set_background_image(self.POKEDEX_IMG)

        # initialize the start button
        self.start_button = QPushButton("START", self)
        self.start_button.setGeometry(84, 441, 130, 65)
        self.start_button.setStyleSheet("font: bold italic 12px;")
        self.start_button.setFlat(True)
        self.start_button.clicked.connect(self.load_model)

        # initialize the load button
        self.load_button = QPushButton("LOAD", self)
        self.load_button.setGeometry(448, 448, 114, 56)
        self.load_button.setStyleSheet("font: bold 12px;")
        self.load_button.setFlat(True)
        self.load_button.clicked.connect(self.load_image)

        # initialize the predict button
        self.predict_button = QPushButton("PREDICT", self)
        self.predict_button.setGeometry(574, 448, 114, 56)
        self.predict_button.setStyleSheet("font: bold 12px;")
        self.predict_button.setFlat(True)
        self.predict_button.clicked.connect(self.predict_image)

        # initialize name display
        self.name_label = QLabel("Name", self)
        self.name_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.name_label.setGeometry(465, 165, 210, 50)
        self.name_label.setStyleSheet("font: bold 12px;")

        # initialize width display
        self.width_label = QLabel("0.0(m)", self)
        self.width_label.setGeometry(475, 238, 60, 30)
        self.width_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.width_label.setStyleSheet("font: bold 12px;")

        # initialize height display
        self.height_label = QLabel("0.0(kgs)", self)
        self.height_label.setGeometry(568, 238, 80, 30)
        self.height_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.height_label.setStyleSheet("font: bold 12px;")

        # display image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(53, 155, 262, 165)
        self.image_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        default_screen = QPixmap("./gui/images/default.png")
        default_screen = default_screen.scaledToWidth(262)
        default_screen = default_screen.scaledToHeight(165)
        self.image_label.setPixmap(default_screen)

    def load_model(self):
        model_path = str(QFileDialog.getOpenFileName(caption="Select Model Path"))
        db_path = str(QFileDialog.getOpenFileName(caption="Select Database Path"))

        status = "Loading Model..."
        self.image_label.setText(status)
        # Load model
        print(model_path)

        status = "Loading Database..."
        self.image_label.setText(status)
        # Load database
        print(db_path)

        status = "Done! Pokedex is ready."
        self.image_label.setText(status)

    def load_image(self):
        image_path = str(QFileDialog.getOpenFileName(caption="Select Model Path")).split(',')[0][1:][1:-1]
        displayed_image = QPixmap(image_path)
        displayed_image = displayed_image.scaledToWidth(262)
        displayed_image = displayed_image.scaledToHeight(165)
        self.image_label.setPixmap(displayed_image)

    def predict_image(self, image):
        # Preprocess
        # Make prediction
        # Display results
        return

    def set_size(self, width, height):
        self.setMinimumSize(QSize(width, height))
        self.setMaximumSize(QSize(width, height))

    def set_background_image(self, path):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(path)))
        self.setPalette(palette)

    def set_window_title(self, title):
        self.setWindowTitle(title)

    def display_info(self, index):
        return

    def display_image(self, path):
        return
