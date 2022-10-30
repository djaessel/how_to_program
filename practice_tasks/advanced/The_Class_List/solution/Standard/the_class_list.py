#!/usr/bin/python


classes = [
  "TGIE",
  "TGMTE",
  "TGJ1/1",
  "TGJ1/2",
  "TGJ2/1",
  "TGJ2/2",
  "TGJ3/1",
  "TGJ3/2",
]


print("------------------------")
print("---- The Class List ----")
print("------------------------")
print("-- Erstelle die Liste --")
print("------------------------")


def student_input():
    students = []

    next_student = True
    while next_student:
        vorname = input('Vorname: ')
        nachname = input('Nachname: ')
        alter = input('Alter: ')
        firma = input('Firma (optional): ')
        coding_language = input('Lieblingsprogrammiersprache (optional): ')
        
        falsche_eingabe = True
        while falsche_eingabe:
            klasse = input('Klasse: ')
            if klasse in classes:
                falsche_eingabe = False
            else:
                print("Falsche Klasse!")
                print("Verfügbare Klassen:")
                for c in classes:
                    print(c)
                print()
        
        students.append((vorname, nachname, alter, firma, coding_language, klasse))
        
        weiter = input('Naechster Schueler? [J/n]: ')
        if weiter != '' and weiter.lower() != 'j':#
            next_student = False

    return students
        

def change_block(array, x, y):
    xx = array[x]
    array[x] = array[y]
    array[y] = xx
    return array


def sort_students(students):
    student_order = []
    for i in range(len(students)):
        student_order.append((i, classes.index(students[i][5])))

    for i in range(len(student_order)):
        for j in range(i):
            if student_order[j][1] > student_order[i][1]:
                change_block(student_order, i, j)

    new_students = []
    for i in range(len(student_order)):
        new_students.append(students[student_order[i][0]])

    return new_students


def print_students(students):
    print("--------------")
    print("-- Schueler --")
    print("--------------")
    print("Nachname", "Firma", "Klasse")
    for student in students:
        print(student[1], student[3], student[5])


schueler = student_input()
schueler = sort_students(schueler)
print_students(schueler)

