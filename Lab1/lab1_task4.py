users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
total_users_count = len(users)
unique_users_count = len(set(users))

statistics_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0

}

statistics_["Общее количество"] = total_users_count
statistics_["Уникальные посещения"] = unique_users_count

print(statistics_)



# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
