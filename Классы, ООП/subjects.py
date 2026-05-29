class subject:
    _objects = []
    #атрибуты класса:
    total_subjects = 0
    numer = 1
    def __init__(self, Name, Type, Semester):
        self.Name = Name
        self.Type = Type
        self.Semester = Semester
        self.num=subject.numer
        subject.total_subjects+=1
        subject._objects.append(self)
        subject.numer+=1
    @classmethod
    def getobjects(cls):
        return cls._objects
    def __repr__(self):
        return f"[{self.num}] {self.Name} ({self.Type} {self.Semester} сем.)"
while True:
    print("Список всех предметов:", subject.getobjects())
    print("Всего предметов:", subject.total_subjects)
    act = input("Выберите действие путем ввода с клавиатуры:\n1 - Создать предмет\n2 - Удалить предмет\n0 - Выход\n")
    if act == "1":
        name = input("Введите название предмета: ")
        typesub = input("Введите тип предмета: ")
        semester = input("Введите семестр предмета: ")
        if semester == "1" or semester == "2":
            sub = subject(name, typesub, semester)
            print(f"Предмет {name} был успешно добавлен!")
        else:
            print("Семестр должен быть числом от 1 до 2")
    elif act=="2":
        if not subject.getobjects():
            print("Список предметов пуст")
            continue
        try:
            numertodelete = int(input("Введите номер удаляемого предмета\n"))
            subjecttoremove = None
            for sub in subject.getobjects():
                if sub.num==numertodelete:
                    subjecttoremove = sub
                    break
            if subjecttoremove:
                subject._objects.remove(subjecttoremove)
                subject.total_subjects-=1
                print(f"Предмет {subjecttoremove.Name} был удален")
            else:
                print("Предмет с таким номером не найден")
        except ValueError:
            print("Ошибка: нужно ввести число")
    elif act=="0":
        break
