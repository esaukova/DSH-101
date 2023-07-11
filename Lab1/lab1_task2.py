# TODO Найдите количество книг, которое можно разместить на дискете
disk_space = 1.44 #Мегабайта
number_of_pages = 100
number_of_lines_on_page = 50
number_of_symbols_in_line = 25
symbol_space = 4 #байта

BYTES_IN_MEGABYTE = 1024 ** 2 #байт
one_book = number_of_pages * number_of_lines_on_page * number_of_symbols_in_line
one_book_space = one_book * symbol_space
number_of_books_on_disk = round((disk_space * BYTES_IN_MEGABYTE) / one_book_space)

print("Количество книг, помещающихся на дискету:", number_of_books_on_disk)
