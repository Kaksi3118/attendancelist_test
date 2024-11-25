from datetime import datetime
from attendance_data import AttendanceDataClass
from check_attendance import CheckAttendanceClass
from import_export import ImportExportClass
from managingList import managingListClass

class importingFunctions: #Dla szybkiego dostepu do wszystkich funkcji
    importExport = ImportExportClass()
    checkAttendance = CheckAttendanceClass()
    managingList = managingListClass()
    attendanceData = AttendanceDataClass()

use = importingFunctions() # deklaracja funkcji
managingListClass.students = []
use.students = []
filename = "students_Database.csv"
use.managingList.checkIfCreated(filename) # sprawdzenie czy istnieje plik
wantToEnd = False

while wantToEnd == False:
    managingListClass.students = use.managingList.importFromFile(filename)
    print("\n" * 100)
    decision = input("Zdecyduj co chcesz zrobic: "
                     "\n1 - Pokaż liste studentów"
                     "\n2 - edytuj liste studentów"
                     "\n3 - dodaj obecność"
                     "\n4 - edytuj obecności"
                     "\nreszta - zakończ\n")
    print("\n" * 100)
    if(decision == "1"):
      for student in managingListClass.students:
          print(student)
      _ = input("Press any key to continue...")
    elif(decision == "2"):
        wantToStop = False
        while (wantToStop == False):
            addOrDelete = input("chcesz dodac czy usunac studenta? \n1 - dodaj \n2 - usun \nenter - cofnij\n")
            if addOrDelete == "1":
                    name = input("Podaj imie: ")
                    surname = input("Podaj nazwisko: ")

                    isDuplicate = True
                    while (isDuplicate == True):
                        isDuplicate = False
                        isNumber = False
                        while isNumber == False:
                            idInput = input("Podaj unikalne id: ")  # string: imie,nazwisko,id,data,obecny
                            try:
                                int(idInput)
                                isNumber = True
                            except:
                                print("podano bledny typ danych, prosze podac liczbe calkowita dodatnia")
                                isNumber = False
                        for student in managingListClass.students:
                            dupeStudent = next((student for student in managingListClass.students if student["id:"] == idInput),None)
                            if dupeStudent:
                                isDuplicate = True
                                print(f"id: {idInput} juz istnieje")
                                break

                    isDateGood = False
                    while isDateGood == False:
                        isDateGood = True
                        date_text = input("Podaj date dolaczenia: (yyyy.mm.dd)")
                        try:
                            date = datetime.strptime(date_text, "%Y.%m.%d").date()
                        except ValueError:
                            isDateGood= False
                            print("Podano bledna wartosc!")

                    use.managingList.addStudent(name,surname,idInput,date)
                    use.managingList.saveToFile(filename)

            elif addOrDelete == "2":
                isNumber = False
                while isNumber == False:
                    idToDelete = input("Podaj id do usuniecia: ")
                    try:
                        int(idToDelete)
                        isNumber = True
                    except:
                        print("podano bledny typ danych, prosze podac liczbe calkowita dodatnia")
                        isNumber = False
                use.managingList.deleteStudent(idToDelete, filename)


            else:
                wantToStop = True

    elif (decision == "3"):
        use.checkAttendance.addAndSavePresence(filename)
        use.managingList.saveToFile(filename)
    elif (decision == '4'):
        isDateGood = False
        while isDateGood == False:
            isDateGood = True
            fileNameDate = input("Podaj date: YYYY.mm.dd ")
            try:
                date = datetime.strptime(fileNameDate, "%Y.%m.%d").date()
            except ValueError:
                isDateGood = False
                print("Podano bledna wartosc!")

        use.attendanceData.editPresence(f"Obecność_"+fileNameDate+".csv")
    else:
        wantToEnd = True
