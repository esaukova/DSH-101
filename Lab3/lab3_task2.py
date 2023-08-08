# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, delimiter=','):
    participants1 = set(str1.split(delimiter))
    participants2 = set(str2.split(delimiter))

    common_participants = list(participants1.intersection(participants2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
