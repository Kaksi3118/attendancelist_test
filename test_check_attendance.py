import os
import pytest

from check_attendance import CheckAttendanceClass


def test_add_attendance():
    # Given:
    attendance = CheckAttendanceClass()
    want = {
        "name:": "Jan",
        "surname:": "Kowalski",
        "id:": "1",
        "attendance:": "Yes"
    }

    # When:
    attendance.addAttendance("Jan", "Kowalski", "1", "Yes")
    got = attendance.attendance_list[0]

    # Then:
    assert got == want


def test_save_attendance(tmp_path):
    # Given:
    attendance = CheckAttendanceClass()
    attendance.addAttendance("Anna", "Nowak", "2", "No")
    test_file = tmp_path / "attendance.csv"
    want = True
    # When:
    attendance.saveAttendance(test_file)
    got = test_file.exists()

    # Then:
    assert got == want
