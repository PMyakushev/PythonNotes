import csv
from datetime import datetime

# Структура заметки: [идентификатор, заголовок, тело заметки, дата_время]
def add_note(title, body):
    try:
        with open('../notes.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([hash(title + body + str(datetime.now())), title, body, datetime.now()])
    except:
        print("Ошибка при добавлении заметки.")

def delete_note(note_id):
    try:
        notes = list(csv.reader(open("../notes.csv"), delimiter=';'))
        notes = [note for note in notes if note[0] != note_id]
        writer = csv.writer(open('../notes.csv', 'w', newline=''), delimiter=';')
        writer.writerows(notes)
    except:
        print("Ошибка при удалении заметки.")

def update_note(note_id, new_title = '', new_body = ''):
    notes = list(csv.reader(open("../notes.csv"), delimiter=';'))
    for note in notes:
        if note[0] == note_id:
            if new_title != '': note[1] = new_title
            if new_body != '': note[2] = new_body
    writer = csv.writer(open('../notes.csv', 'w', newline=''), delimiter=';')
    writer.writerows(notes)

def read_notes(date = ''):
    try:
        with open('../notes.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if date == '' or datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S").date() == datetime.strptime(date, "%Y-%m-%d").date():
                    print(', '.join(row))
    except:
        print("Ошибка при чтении заметок.")

while(True):
    command = input('Введите команду (add, delete, update, read, exit): ')
    if command == 'add':
        title = input('Введите заголовок заметки: ')
        body = input('Введите тело заметки: ')
        add_note(title, body)
    elif command == 'delete':
        id = input('Введите id заметки: ')
        delete_note(id)
    elif command == 'update':
        id = input('Введите id заметки: ')
        new_title = input('Введите новый заголовок (если нужно оставить старый, то просто нажмите Enter): ')
        new_body = input('Введите новое тело заметки (если нужно оставить старое, то просто нажмите Enter): ')
        update_note(id, new_title, new_body)
    elif command == 'read':
        date = input('Введите дату (YYYY-MM-DD) или нажмите Enter для просмотра всех заметок: ')
        read_notes(date)
    elif command == 'exit':
        break
    else:
        print('Неизвестная команда.')