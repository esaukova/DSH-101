# TODO  Напишите функцию count_letters


def count_letters(text):
    text_lower = text.lower()  # Приводим символ к нижнему регистру
    letter_count = {}

    for char in text_lower:
        if char.isalpha():
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1

    return letter_count


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
    frequency_dict = {}
    for letter, count in letter_count.items():
        frequency_dict[letter] = round(count / total_letters, 2)
    return frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
# Пример использования

def count_and_calculate(text):
    letter_count = count_letters(text)
    frequency_dict = calculate_frequency(letter_count)
    for letter, frequency in frequency_dict.items():
        print(f"{letter}: {frequency:.2f}")

count_and_calculate(main_str)

# TODO Распечатайте в столбик букву и её частоту в тексте
