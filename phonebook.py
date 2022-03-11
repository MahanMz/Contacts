

from PyQt5 import uic
from PyQt5.QtWidgets import *

class Book(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("PhoneBook.ui", self)

        self.btnAdd.clicked.connect(self.openAddDialog)
        self.btnRemove.clicked.connect(self.deleteContact)
        
        self.setWindowTitle("Phone Book")
        self.show()

    def openAddDialog(self):
        """Open the Add Contact dialog."""
        dialog = Add(self)
        if dialog.exec() == QDialog.Accepted:
            self.addContact(dialog.data)
            
    def addContact(self, data):
        """Add a contact to the database."""
        rows = self.table.rowCount()
        self.table.insertRow(rows)
        
        for d in data:
            print(d)
            columns = data.index(d)
            value = QTableWidgetItem(str(d))
            self.table.setItem(rows, columns, value)
        self.widthc()
    def widthc(self):
        if self.table.columnWidth(0) < 150:
            self.table.setColumnWidth(0, 150)
            self.table.setColumnWidth(1, 150)
            self.table.setColumnWidth(2, 298)


    def deleteContact(self):
        """Delete the selected contact from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Delete Confim",
            "Do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        
        if messageBox == QMessageBox.Ok:
            self.table.removeRow(row)

class Add(QDialog):
    def __init__(self, parent= None):
        super().__init__()
        uic.loadUi("AddContact.ui", self)
        self.setWindowTitle("Add Contact")

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.fname, self.lname, self.phone):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()

app = QApplication([])
win = Book()
app.exec_()