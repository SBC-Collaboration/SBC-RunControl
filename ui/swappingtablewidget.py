from PySide6.QtWidgets import QTableWidget


# Overriding original table widget so that drag and drop will swap the two values, instead of erasing the value at destination
class SwappingTableWidget(QTableWidget):
    def dropEvent(self, dropEvent):
        item_src = self.selectedItems()[0]
        item_dest = self.itemAt(dropEvent.pos())
        src_value = item_src.text()
        item_src.setText(item_dest.text())
        item_dest.setText(src_value)