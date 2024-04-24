from PySide6 import QtWidgets


# Overriding original table widget so that drag and drop will swap the two values, instead of erasing the value at
# destination
class SwappingTableWidget(QtWidgets.QTableWidget):
    def dropEvent(self, dropEvent):
        item_src = self.selectedItems()[0]
        item_dest = self.itemAt(dropEvent.pos())
        src_value = item_src.text()
        item_src.setText(item_dest.text())
        item_dest.setText(src_value)


class NoWheelSpinBox(QtWidgets.QSpinBox):
    def wheelEvent(self, event):
        event.ignore()


class NoWheelDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    def wheelEvent(self, event):
        event.ignore()


class NoWheelComboBox(QtWidgets.QComboBox):
    def wheelEvent(self, event):
        event.ignore()
