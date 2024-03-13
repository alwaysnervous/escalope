import sys

from prototype.main import File, FileSystemInterface

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication

file_system = FileSystemInterface(File('Задачник по олимпиадному программированию.pdf',
                                       {'Олимпиады', 'Программирование', 'Книги'}),
                                  File('Чистый код.fb2',
                                       {'Программирование', 'Книги'}),
                                  File('Доклад «Менеджер паролей».docx',
                                       {'Доклады', 'Проекты', 'МИРЭА', 'Менеджер паролей'}),
                                  File('Презентация «Менеджер паролей».pptx',
                                       {'Презентации', 'Проекты', 'МИРЭА', 'Менеджер паролей'}),
                                  File('Python для начинающих.pdf',
                                       {'Программирование', 'Python', 'Книги'}),
                                  File('Базы данных.fb2',
                                       {'Программирование', 'Базы данных', 'Книги'}),
                                  File('Доклад «Искусственный интеллект».docx',
                                       {'Доклады', 'Проекты', 'Искусственный интеллект'}),
                                  File('Презентация «Блокчейн технологии».pptx',
                                       {'Презентации', 'Проекты', 'Блокчейн'})
                                  )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.model = None
        loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.model = QStandardItemModel()

        self.get_linked_tags()

        self.listView.setModel(self.model)

        self.listView.doubleClicked.connect(self.handle_double_click)

        self.backwardButton.clicked.connect(self.backward_click)

    def handle_double_click(self, index):
        selected_item = self.model.itemFromIndex(index)
        item_text = selected_item.text()
        file_system.add_current_tag(item_text)

        self.model.clear()
        self.get_linked_tags()

    def get_linked_tags(self):
        folders, files = file_system.get_linked_tags
        for folder_name in folders:
            item = QStandardItem(folder_name)
            item.setIcon(QIcon('data/img/folder.png'))
            self.model.appendRow(item)
        for file_name in files:
            item = QStandardItem(file_name)
            item.setIcon(QIcon('data/img/extensions/file.png'))
            self.model.appendRow(item)

        self.label.setText('/'.join(file_system.current_tags))

    def backward_click(self):
        file_system.backward_step()
        self.model.clear()
        self.get_linked_tags()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
