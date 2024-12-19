import pytest

from managingList import managingListClass


def test_add_student():
    # Given:
    manager = managingListClass()
    want = {
        "name:": "Anna",
        "surname:": "Nowak",
        "id:": "2",
        "date:": "2023-11-25"
    }

    # When:
    manager.addStudent("Anna", "Nowak", "2", "2023-11-25")
    got = manager.students[0]

    # Then:
    assert got == want
#TODO: Testing if code is good maybe

def test_delete_student(tmp_path):
    # Given:
    test_file = tmp_path / "students.csv"
    manager = managingListClass()
    manager.addStudent("Anna", "Nowak", "2", "2023-11-25")
    manager.saveToFile(test_file)
    want = 1  # Liczba wierszy w pliku po usunięciu (nagłówek)

    # When:
    manager.deleteStudent("2", test_file)
    with open(test_file, "r", encoding="utf-8") as file:
        got = len(file.readlines())

    # Then:
    assert got == want
