import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout

from src.editor.vg_editor import VisualGraphEditor

if __name__ == '__main__':
    app = QApplication([])
    container = QVBoxLayout()
    v_layout = VisualGraphEditor()
    v_layout.show()
    sys.exit(app.exec())