#### IMPORTS ####
import event_manager as EM


#### PART 1 ####
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    all_lines = createAllCorrectLinesFromFile(orig_file_path)
    output_file = open(filtered_file_path, 'w')
    for line in all_lines:
        output_file.write(line)
    output_file.close()


def checkLineCorrect(line: str):
    devised_line = line.split(',')
    if len(devised_line) != 5:
        return False

    id_num = (devised_line[0]).replace(' ', '')
    name = ''.join((devised_line[1]).split())
    age = int(devised_line[2].replace(' ', ''))
    birth_year = int(devised_line[3].replace(' ', ''))
    semester = int(devised_line[4].replace(' ', ''))

    id_correct = (len(id_num) == 8 and id_num[0] != 0)
    name_correct = (name.isalpha())
    age_correct = (120 >= age >= 16)
    birth_year_correct = (age + birth_year == 2020)
    semester_correct = (semester >= 1)

    return id_correct and name_correct and age_correct and \
           birth_year_correct and semester_correct


def createAllCorrectLinesFromFile(orig_file_path: str):
    input_file = open(orig_file_path, 'r')
    all_lines = []

    for new_line in input_file:
        if checkLineCorrect(new_line):
            new_line = correctLine(new_line)
            for i, existing_line in enumerate(all_lines):
                if existing_line[0:8] == new_line[0:8]:
                    del all_lines[i]
            all_lines.append(new_line)

    return all_lines


def correctLine(line: str):
    devised_line = line.split(',')

    id_num = (devised_line[0]).replace(' ', '')
    name = ' '.join((devised_line[1]).split())
    age = devised_line[2].replace(' ', '')
    birth_year = devised_line[3].replace(' ', '')
    semester = devised_line[4].replace(' ', '')

    new_line = [id_num, name, age, birth_year, semester]
    new_line = ', '.join(new_line)
    return new_line


def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if k < 1:
        return -1

    all_lines = createAllCorrectLinesFromFile(in_file_path)
    if len(all_lines) < k:
        k = len(all_lines)

    all_lines.sort(key=getId)
    all_lines.sort(key=getAge)

    output_file = open(out_file_path, 'w')
    for i, line in enumerate(all_lines):
        if i < k:
            output_file.write(line)
    output_file.close()

    return k


def getId(line: str):
    split_line = line.split(', ')
    line_id = int(split_line[0])
    return line_id


def getAge(line: str):
    split_line = line.split(', ')
    line_age = int(split_line[2])
    return line_age


def correctAgeAvg(in_file_path: str, semester: int) -> float:
    if semester < 1:
        return -1

    age_sum = 0
    amount_of_students = 0
    all_lines = createAllCorrectLinesFromFile(in_file_path)

    for line in all_lines:
        split_line = line.split(', ')
        student_semester = int(split_line[-1][0:-1])
        if student_semester == semester:
            amount_of_students = amount_of_students + 1
            age_sum = age_sum + int(split_line[2])

    if amount_of_students == 0:
        average = 0
    else:
        average = age_sum / amount_of_students

    return average


#### PART 2 ####
def printEventsList(events: list,
                    file_path: str):  # em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    pass
    # TODO


def testPrintEventsList(file_path: str):
    events_lists = [{"name": "New Year's Eve", "id": 1, "date": EM.dateCreate(30, 12, 2020)}, \
                    {"name": "annual Rock & Metal party", "id": 2, "date": EM.dateCreate(21, 4, 2021)}, \
                    {"name": "Improv", "id": 3, "date": EM.dateCreate(13, 3, 2021)}, \
                    {"name": "Student Festival", "id": 4, "date": EM.dateCreate(13, 5, 2021)}, ]
    em = printEventsList(events_lists, file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)
