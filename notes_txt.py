#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QPushButton,QLabel,QListWidget,QLineEdit,QTextEdit,QInputDialog,QHBoxLayout,QVBoxLayout,QFormLayout)
import json
notes = {
'Добро пожаловать!':
        {
            "текст" : "введите заметку:",
            "теги" : ["добро","инструкция"]
        }
}

with open('f.json','w') as file:
    json.dump(notes, file)

app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
list_notes = QListWidget()#Сосдаём список заметок
list_notes_label = QLabel('Список заметок')#Надпись для списка заметок
button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')
field_tag = QLineEdit('')
field_text = QLineEdit('') #Поле для ввода текста
field_tag.setPlaceholderText('Введите тег...')#Подсказка в поле ввода тега
field_text = QTextEdit() #Многострочное текстовое поле для заметок
field_text.setPlaceholderText('Введите заметку...')
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу') #Кнопка
list_tags = QListWidget() #Список для отображения тегов
list_tags_label = QLabel()#Метка для списка тегов

layout_notes = QHBoxLayout()#Главный комплектовщик (главная коробочка)
col_1 = QVBoxLayout()#Вертикальная компоновка для первой колонки
col_1.addWidget(field_text) #Добавляем текстовое поле в первую колонку
layout_notes.addLayout(col_1)
notes_win.setLayout(layout_notes)

col_2 = QVBoxLayout() #2 столбец справа
col_2.addWidget(list_notes_label) 
col_2.addWidget(list_notes)


row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
col_2.addLayout(row_3)
col_2.addLayout(row_2)
col_2.addLayout(row_4)
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text() #Выбор заметки
        notes[key]['текст'] = field_text.toPlainText()
        with open ("f.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка не найдена!')

def show_note():
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[name]['теги'])
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != "":
        notes[note_name] = {'текст' : '', 'теги' : []}
        list_notes.addItem(note_name)
        list_tags.addItem(notes[note_name]['текст'])
        print(notes)
def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open ("f.json", "w") as file:
            json.dump(notes, file,sort_keys=True, ensure_ascii=False)
        print(notes)
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open ("f.json", "w") as file:
            json.dump(notes, file,sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для добавления не выбрана')
def del_tag(): 
    if list_notes.selectedItems()[0].text():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["теги"])
        with open ("f.json", "w") as file:
            json.dump(notes, file,sort_keys=True, ensure_ascii=False)
        print(notes)

def search_tag():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text() == 'Искать заметки по тегу' and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        button_tag_search.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text() == 'Сбрость поиск':
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText('Искать заметки по тегу')
        print(button_tag_search.text())
    else:
        pass

button_note_create.clicked.connect(add_note)  
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)
button_tag_search.clicked.connect(search_tag)
button_tag_add.clicked.connect(add_tag)
button_note_del.clicked.connect(del_note)
button_tag_del.clicked.connect(del_tag)

layout_notes.addLayout(col_2)
notes_win.setLayout(layout_notes)
# with open("f.json", "r") as file:
#     notes = json.load(file)
#     list_notes.addItems(notes)
notes_win.show()
app.exec_()