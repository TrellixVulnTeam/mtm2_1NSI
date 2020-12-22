#### IMPORTS ####
# import event_manager as EM


#### PART 1 ####
# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    input_file = open(orig_file_path, 'r')
    output_file = open(filtered_file_path, 'w')
    all_lines = []

    for new_line in input_file:
        if checkLineCorrect(new_line):
            new_line = correctLine(new_line)
            for i, existing_line in enumerate(all_lines):
                if existing_line[0:8] == new_line[0:8]:
                    del all_lines[i]
            all_lines.append(new_line)

    for line in all_lines:
        output_file.write(line)

    input_file.close()
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


def correctLine(line: str):
    devised_line = line.split(',')

    id_num = (devised_line[0]).replace(' ', '')
    name = ' '.join((devised_line[1]).split())
    age = devised_line[2].replace(' ', '')
    birth_year = devised_line[3].replace(' ', '')
    semester = devised_line[4].replace(' ', '')

    new_line = [id_num, name, age, birth_year, semester]
    return ', '.join(new_line)

    # Writes the names of the K youngest students which subscribed
    # to the event correctly.
    #   in_file_path: The path to the unfiltered subscription file
    #   out_file_path: file path of the output file


def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if k < 1:
        return -1

    fileCorrect(in_file_path, out_file_path)
    output_file = open(out_file_path, 'r')
    lines_in_order = []

    for line in output_file:
        print(line)

    return 1
    pass
    # TODO

    # Calculates the avg age for a given semester
    #   in_file_path: The path to the unfiltered subscription file
    #   retuns the avg, else error codes defined.
    # def correctAgeAvg(in_file_path: str, semester: int) -> float:
    #    pass
    # TODO

    #### PART 2 ####
    # Use SWIG :)
    # print the events in the list "events" using the functions from hw1
    #   events: list of dictionaries
    #   file_path: file path of the output file
    # def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    #    pass
    # TODO

    # def testPrintEventsList(file_path :str):
    #     events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
    #                     {"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
    #                                  {"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
    #                                      {"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
    #     em = printEventsList(events_lists,file_path)
    #     for event in events_lists:
    #         EM.dateDestroy(event["date"])
    #     EM.destroyEventManager(em)

    #### Main ####
    # feel free to add more tests and change that section.
    # sys.argv - list of the arguments passed to the python script
    # def main():
    #     i = 1
    #     open('C:\Users\adi.amuzig\Desktop\Google Drive\טכניון\תואר שני\קורסים\השלמות\מתמ\HW\hw2\code\tests\input', 'r')
    #
    #     fileCorrect('tests\input', 'tests\my_out1')
    #
    # if __name__ == "__main__":
    #     main()
    import sys
    # if len(sys.argv)>1:
    # testPrintEventsList(sys.argv[1])
