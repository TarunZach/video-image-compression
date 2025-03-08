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
import vid_compressor


class CompressionApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.setWindowTitle("Video & Image Compressor")
        self.setGeometry(100, 100, 800, 600)

        # UI Elements
        self.label = QLabel("Select a file to compress", self)
        self.select_button = QPushButton("Choose File", self)
        self.compress_button = QPushButton("Compress", self)
        self.slider = QSlider(Qt.Horizontal)
        self.progress_bar = QProgressBar(self)

        # Slider
        self.slider.setMinimum(10)
        self.slider.setMaximum(90)
        self.slider.setValue(50)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_button)
        layout.addWidget(QLabel("Compression Percentage:"))
        layout.addWidget(self.slider)
        layout.addWidget(self.compress_button)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

        # Signals
        self.select_button.clicked.connect(self.select_file)
        self.compress_button.clicked.connect(self.compress_file)

        self.selected_file = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "Images (*.png *.jpg *.jpeg);;Videos (*.mp4 *.avi *.mkv)",
        )

        if file_path:
            self.selected_file = file_path
            self.label.setText(f"Selected: {os.path.basename(file_path)}")

    def compress_file(self):
        if not self.select_file:
            self.label.setText("No file selected!")
            return

        compression_level = self.slider.value()
        file_extension = os.path.splitext(self.selected.file)[1].lower()

        if file_extension in [".png", ".jpg", ".jpeg"]:
            output_file = img_compressor.compress_image(
                self.selected_file, compression_level
            )

        elif file_extension in [".mp4", ".avi", ".mkv"]:
            output_file = vid_compressor.compress_video(
                self.selected_file, compression_level
            )
        else:
            self.label.setText("Unsupported file format!")
            return

        self.label.setText(f"Compression Complete: {os.path.basename(output_file)}")
        self.progress_bar.setValue(100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CompressionApp()
    window.show()
    sys.exit(app.exec_())
