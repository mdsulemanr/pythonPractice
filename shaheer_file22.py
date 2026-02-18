def stu(students):

    for name, storage in students.items():
        if storage["age"] == 9:
            if storage["Gender"] == "boy":
                if storage["Section"] == "Green":
                    if "Strawberry" in storage["favourite"]:
                        if storage["angry"] == False:
                            if storage["favourite_subject"] == "Math":
                                return stu(students)

students = {
        "Shaheer": {
            "age": 9,
            "Gender": "boy",
            "Class": 3,
            "Section": "Green",
            "favourite": ["Cherry", "Strawberry", "Pineapple"],
            "angry": False,
            "favourite_subject": "Math"
        },
        "Arisha": {
            "age": 12,
            "Gender": "girl",
            "Class": 6,
            "Section": "Red",
            "favourite": ["Apple", "Banana"],
            "angry": True,
            "favourite_subject": "Computer"
        },
        "Mustafa": {
            "age": 11,
            "Gender": "boy",
            "Class": 5,
            "Section": None,
            "favourite": ["Guava", "Pineapple"],
            "angry": True,
            "favourite_subject": "Urdu"
        },
        "Hazik": {
            "age": 13,
            "Gender": "boy",
            "Class": 7,
            "Section": None,
            "favourite": ["Apple", "Guava"],
            "angry": False,
            "favourite_subject": "English"
        },
        "Zaryab": {
            "age": 12,
            "Gender": "boy",
            "Class": 6,
            "Section": None,
            "favourite": ["Apple", "Pineapple"],
            "angry": True,
            "favourite_subject": "Science"
        },
        "Ahmad": {
            "age": 5,
            "Gender": "boy",
            "Class": None,
            "Section": None,
            "favourite": ["Apple", "Orange"],
            "angry": True,
            "favourite_subject": None
        },
        "Haris": {
            "age": 9,
            "Gender": "boy",
            "Class": 3,
            "Section": "Orange",
            "favourite": ["Apple", "Banana", "Pineapple"],
            "angry": False,
            "favourite_subject": "Computer"
    }
}

name = stu(students)

print(name)