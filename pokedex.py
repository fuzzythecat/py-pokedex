import json
import cv2

import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PyQt5.QtGui import QPalette, QPixmap, QBrush
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import QSize, Qt

import config

class QPokedex(QMainWindow):
    def __init__(self, width, height):
        super(QPokedex, self).__init__()

        # initialize the window
        self.set_size(width, height)
        self.set_window_title("Pokedex")
        self.set_background_image(config.pokedex_img_path)

        # initialize the start button
        self.classify_button = QPushButton("ClASSIFY", self)
        self.classify_button.setGeometry(84, 441, 130, 65)
        self.classify_button.setStyleSheet("font: bold italic 12px;")
        self.classify_button.setFlat(True)

        # initialize the load button
        self.load_image_button = QPushButton("LOAD IMAGE", self)
        self.load_image_button.setGeometry(448, 448, 114, 56)
        self.load_image_button.setStyleSheet("font: bold 12px;")
        self.load_image_button.setFlat(True)

        # initialize the predict button
        #self.classify_button = QPushButton("PREDICT", self)
        #self.classify_button.setGeometry(574, 448, 114, 56)
        #self.classify_button.setStyleSheet("font: bold 12px;")
        #self.classify_button.setFlat(True)

        # initialize name display
        self.name_label = QLabel("Name", self)
        self.name_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.name_label.setGeometry(465, 165, 210, 50)
        self.name_label.setStyleSheet("font: bold 12px;")

        # initialize height display
        self.height_label = QLabel("0.0(m)", self)
        self.height_label.setGeometry(475, 238, 60, 30)
        self.height_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.height_label.setStyleSheet("font: bold 12px;")

        # initialize weight display
        self.weight_label = QLabel("0.0(kgs)", self)
        self.weight_label.setGeometry(568, 238, 80, 30)
        self.weight_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.weight_label.setStyleSheet("font: bold 12px;")

        # display image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(53, 155, 262, 165)
        self.image_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        default_screen = QPixmap(config.default_img_path)
        default_screen = default_screen.scaledToWidth(262)
        default_screen = default_screen.scaledToHeight(165)
        self.image_label.setPixmap(default_screen)

        # connect activities
        self.classify_button.clicked.connect(self.on_button_classify)
        self.load_image_button.clicked.connect(self.on_button_load)
        
        self.model = load_model(config.model_path)
        self.labels = config.labels
        self.db = json.loads(open(config.db_path).read())

    def on_button_classify(self):
        # load pretrained pokedex model
        image = cv2.imread(self.image_path)

        # preprocess image
        image = cv2.resize(image, (96, 96))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        proba = self.model.predict(image)[0]

        # update display info
        name = self.labels[np.argmax(proba)]
        info = self.db[name]
        self.name_label.setText(name)
        self.weight_label.setText(info["weight"])
        self.height_label.setText(info["height"])

    def on_button_load(self):
        image_path = str(QFileDialog.getOpenFileName(caption="Select Model Path")).split(',')[0][1:][1:-1]
        displayed_image = QPixmap(image_path)
        displayed_image = displayed_image.scaledToWidth(262)
        displayed_image = displayed_image.scaledToHeight(165)
        self.image_label.setPixmap(displayed_image)
        self.image_path = image_path

    def set_size(self, width, height):
        self.setMinimumSize(QSize(width, height))
        self.setMaximumSize(QSize(width, height))

    def set_background_image(self, path):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(path)))
        self.setPalette(palette)

    def set_window_title(self, title):
        self.setWindowTitle(title)