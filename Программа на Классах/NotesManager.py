import csv
from datetime import datetime

class Note:
    def __init__(self, id=None, title='', body=''):
        self.id = id
        self.title = title
        self.body = body
        self.date = datetime.now()

    def __str__(self):
        return f'ID: {self.id}, Title: {self.title}, Body: {self.body}, Date: {self.date}'

class NotesManager:
    def __init__(self, csvfile='notes.csv'):
        self.csvfile = csvfile
        self.delimiter = ';'

    def add_note(self, title, body):
        note = Note(hash(title + body + str(datetime.now())), title, body)
        try:
            with open(self.csvfile, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=self.delimiter)
                writer.writerow([note.id, note.title, note.body, note.date])
        except:
            print("Ошибка при добавлении заметки.")

    def delete_note(self, note_id):
        try:
            notes = list(csv.reader(open(self.csvfile), delimiter=self.delimiter))
            notes = [note for note in notes if note[0] != note_id]
            writer = csv.writer(open(self.csvfile, 'w', newline=''), delimiter=self.delimiter)
            writer.writerows(notes)
        except:
            print("Ошибка при удалении заметки.")

    def update_note(self, note_id, new_title='', new_body=''):
        notes = list(csv.reader(open(self.csvfile), delimiter=self.delimiter))
        for note in notes:
            if note[0] == note_id:
                if new_title != '': note[1] = new_title
                if new_body != '': note[2] = new_body
        writer = csv.writer(open(self.csvfile, 'w', newline=''), delimiter=self.delimiter)
        writer.writerows(notes)

    def read_notes(self, date=''):
        try:
            with open(self.csvfile, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=self.delimiter)
                for row in reader:
                    if date == '' or datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S").date() == datetime.strptime(date, "%Y-%m-%d").date():
                        print(', '.join(row))
        except:
            print("Ошибка при чтении заметок.")

manager = NotesManager()

while(True):
    command = input('Введите команду (add, delete, update, read, exit): ')
    if command == 'add':
        title = input('Введите заголовок заметки: ')
        body = input('Введите тело заметки: ')
        manager.add_note(title, body)
    elif command == 'delete':
        id = input('Введите id заметки: ')
        manager.delete_note(id)
    elif command == 'update':
        id = input('Введите id заметки: ')
        new_title = input('Введите новый заголовок (если нужно оставить старый, то просто нажмите Enter): ')
        new_body = input('Введите новое тело заметки (если нужно оставить старое, то просто нажмите Enter): ')
        manager.update_note(id, new_title, new_body)
    elif command == 'read':
        date = input('Введите дату (YYYY-MM-DD) или нажмите Enter для просмотра всех заметок: ')
        manager.read_notes(date)
    elif command == 'exit':
        break
    else:
        print('Неизвестная команда.')