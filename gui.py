import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QFileDialog,
    QVBoxLayout,
    QSlider,
    QProgressBar,
)
from PyQt5.QtCore import Qt
import os
# import image_compressor
# import video_compressor


class CompressionApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.setWindowTitle("Video & Image Compressor")
