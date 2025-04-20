#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QMessageBox, QButtonGroup
from random import shuffle
#создание элементов интерфейса
app = QApplication([]) #приложение (конструктор)
main_win = QWidget() #окно (конструктор)

main_win.setWindowTitle('Memory Card')  #надпись на шапке экрана
main_win.resize(700, 500) #размер окна
main_win.move(900,70) #сдвиг окна

RadioGroupBox = QGroupBox('Варианты')
question = QLabel('')
rbtn_1 = QRadioButton('') #не
rbtn_2 = QRadioButton('')#да
rbtn_3 = QRadioButton('')#не
rbtn_4 = QRadioButton('')#не
button = QPushButton('Ответить')

main_win.cur_question = -1
main_win.score = 0
main_win.total = 0
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3    
q = Question('Какое море омывает берега Сочи?', 'Чёрное', 'Балтийское', 'Каспийское', 'Баренцево')
# questions_list.append(q)
questions_list = []

q1 = Question('Сколько цветов в радуге?', 'Семь', 'Шесть', 'Восемь', 'Девять')
questions_list.append(q1)
q2 = Question('Как зовут главного героя романа Война и мир?', 'Пьер Безухов', 'Андрей Болконский', 'Николай Ростов', 'Иван Карамазов')
questions_list.append(q2)
q3 = Question('Как называется столица Австралии?', 'Канбера', 'Сидней', 'Мельбурн', 'Брисбен')
questions_list.append(q3)
q4 = Question('Кто написал роман Преступление и наказание?', 'Фёдор Достоевские', 'Лев Толстой', 'Антон Чехов', 'Иван Тургенев')
questions_list.append(q4)
q5 = Question('Какая планета находится ближе всего к Солнцу?', 'Меркурий', 'Венера', 'Земля', 'Марс')
questions_list.append(q5)
q6 = Question('Сколько хромосом у человека?', '46', '44', '48', '42')
questions_list.append(q6)
q7 = Question('Какой химический элемент обозначается символом О?', 'Кислород', 'Углерод', 'Водород', 'Натрий')
questions_list.append(q7)
q8 = Question('Какой цвет получится при смешении синего и жёлтого?', 'Зелёный', 'Красный', 'Оранжевый', 'Фиолетовый')
questions_list.append(q8)
q9 = Question('Какое животное является символом 2024 года по восточному календарю?', 'Дракон', 'Крыса', 'Тигр', 'Обезьяна')
questions_list.append(q9)
q10 = Question('Как называется столица Японии?', 'Токио', 'Осака', 'Киото', 'Нагоя')
questions_list.append(q10)
q11 = Question('Кто написал сказку Аленький цветочек', 'Сергей Аксаков', 'Александр Пушкин', 'Николай Гоголь', 'Лев Толстой')
questions_list.append(q11)
q12 = Question('Сколько сторон у треугольника?', 'Три', 'Четыре', 'Пять', 'Две')
questions_list.append(q12)
q13 = Question('Какой газ преобладает в атмосфере Земли?', 'Азот', 'Кислород', 'Углекислый газ', 'Водород')
questions_list.append(q13)
q14 = Question('Кто автор произведения Гарри Поттер?', 'Джоана Роулинг', 'Стивен Кинг', 'Джордж Мартин', 'Толкин')
questions_list.append(q14)
q15 = Question('Как называется самая длинная река в мире?', 'Амазонка', 'Нил', 'Миссисипи', 'Янцзы')
questions_list.append(q15)
q16 = Question('Как называется наука о звёздах и космосе?', 'Астрономия', 'Биология', 'Геология', 'Химия')
questions_list.append(q16)
q17 = Question('Сколько сантиметров в одном метре?', '100', '10', '1000', '50')
questions_list.append(q17)
q18 = Question('Какая страна считается родиной пиццы?', 'Италия', 'Франция', 'Испания', 'Греция')
questions_list.append(q18)
q19 = Question('Какой океан самый большой на планете?', 'Тихий', 'Атлантический', 'Индийский', 'Северный Ледовитый')
questions_list.append(q19)

def show_result():
    RadioGroupBox.hide() #временное скрытие окна
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show() #временное скрытие окна
    AnsGroupBox.hide()
    button.setText('Ответить')    
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(rbtn_1)
    RadioGroup.addButton(rbtn_2)
    RadioGroup.addButton(rbtn_3)
    RadioGroup.addButton(rbtn_4)
    RadioGroup.setExclusive(False)   #снять ограничения
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if 'Ответить' == button.text():
        show_result()
    else:
        show_question() 

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q : Question):
    shuffle(answers)   #перемешать ответы 
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    itog.setText(q.right_answer)
    show_question()

def show_correct(res):    
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score+=1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')

def next_question():
    main_win.total+=1 
    reyting = main_win.score/main_win.total * 100  
    print('Статистка')  
    print('-Всего вопросов:',main_win.total)
    print('-Правильных ответов:', main_win.score)
    print('-Рейтинг:',reyting)    
    main_win.cur_question += 1 #переход к слд вопросу
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0 #обнулить список вопросов    
    q = questions_list[main_win.cur_question] #взять вопрос из списка
    ask(q)

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
itog = QLabel('Правильный ответ')
AnsGroupBox.hide()

layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
AnsGroupBox.setLayout(layout_res)

line1 = QHBoxLayout()
line1.addWidget(question, alignment=(Qt.AlignCenter))
line2 = QHBoxLayout()
line2.addWidget(RadioGroupBox) #alignment= (Qt.AlignHCenter | Qt.AlignVCenter)
line2.addWidget(AnsGroupBox)
line3 = QHBoxLayout()
line3.addStretch(1)
line3.addWidget(button, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
line3.addStretch(1)

glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)



ask(q)
button.clicked.connect(click_ok)


main_win.setLayout(glav)
main_win.show() #сделать окно открытым
app.exec_() #оставлять окно открытым 