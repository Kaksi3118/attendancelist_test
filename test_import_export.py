import pytest

from import_export import ImportExportClass


def test_import_students(tmp_path):
    # Given
    test_file = tmp_path / "students.csv"
    with open(test_file, "w", encoding="utf-8") as file:
        file.write("name:,surname:,id:,attendance:\n")
        file.write("Jan,Kowalski,1,Yes\n")
    importer = ImportExportClass()

    # When:
    got = importer.import_students(test_file)
    want = [{"name:": "Jan", "surname:": "Kowalski",
             "id:": "1", "attendance:": "Yes"}]

    # Then:
    assert got == want


def test_export_attendance(tmp_path):
    # Given:
    test_file = tmp_path / "exported.csv"
    exporter = ImportExportClass()

    # Tymczasowe przypisanie danych do students
    exporter.students = [
        {"Name": "Jan Kowalski", "Present": "Yes"}
    ]

    # Wywołujemy metodę export_attendance
    exporter.export_attendance(str(test_file))

    want = [
        "Name,Present\n",
        "Jan Kowalski,Yes\n"
    ]

    # When:
    with open(test_file, "r", encoding="utf-8") as file:
        got = file.readlines()

    # Then:
    assert want == got
