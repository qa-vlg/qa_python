## Список реализованных тестов:

№ | Тест | Описание
--- | --- | ---
001 | test_default_value_of_books_genre_true | тестируем `__init__` словарь books_genre
002 | test_default_value_of_favorites_true | тестируем `__init__` список favorites
003 | test_default_value_of_genre_true | тестируем `__init__` список genre
004 | test_default_value_of_genre_age_rating_true | тестируем `__init__` список genre_age_rat
005 | test_add_new_book_and_it_should_have_no_genre| у добавленной книги нет жанра
006 | test_set_book_genre_verify_all_genres_accepted | проверяем все доступные жанры
007 | test_get_book_genre_returned_correct_one | проверяем что возвращается верный жанр
008 | test_get_books_with_specific_genre | поиск книги по жанру
009 | test_get_books_genre | проверяем словарь {книга: жанр}
010 | test_get_books_for_children_only_books_for_kids_added | книги с возрастным рейтингом отсутствуют в списке книг для детей
011 | test_add_book_in_favorites_book_added | добавление книги в избранное
012 | test_delete_book_from_favorites_book_is_deleted | удаление книги из избранного
013 | test_get_list_of_favorites_books_all_books_added | добавляем несколько книг в избранное