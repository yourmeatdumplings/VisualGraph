from PySide6.QtWidgets import QWidget, QBoxLayout

class VisualGraphEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = None

        self.setup_editor()

    def setup_editor(self):
        self.setGeometry(400,400,1280,720)

        self.setWindowTitle("Visual Graph")

        self.layout = QBoxLayout(QBoxLayout.LeftToRight, self)

        self.layout.setContentsMargins(0,0,0,0)

        self.show()