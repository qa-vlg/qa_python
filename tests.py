from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_default_value_of_books_genre_true(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_default_value_of_favorites_true(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_default_value_of_genre_true(self):
        collector = BooksCollector()
        expected_list = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert expected_list == collector.genre

    def test_default_value_of_genre_age_rating_true(self):
        collector = BooksCollector()
        expected_list = ['Ужасы', 'Детективы']
        assert expected_list == collector.genre_age_rating

    # verify that added book doesn't have a genre
    def test_add_new_book_and_it_should_have_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Life of a bug')
        assert collector.get_books_genre()['Life of a bug'] == ''

    # add book then a genre, verify all the genre options
    @pytest.mark.parametrize(
        'name, genre', 
        [
            ['Life of a bug', 'Фантастика'],
            ['Crazy Python', 'Ужасы'],
            ['Poirot', 'Детективы'],
            ['Snow White', 'Мультфильмы'],
            ['Good Omens', 'Комедии']
        ]
    )
    def test_set_book_genre_verify_all_genres_accepted(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre()[name] == genre

    # add a book then a genre and verify proper genre returned
    @pytest.mark.parametrize('name, genre', [['Life of a bug', 'Фантастика']])
    def test_get_book_genre_returned_correct_one(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # add a book then a genre and verify proper list of  genre items returned
    @pytest.mark.parametrize('name, genre', [['Life of a bug', 'Фантастика']])
    def test_get_books_with_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre)[0] == name

    # verifying returned dict has proper book/genre
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Life of a bug')
        collector.set_book_genre('Life of a bug', 'Фантастика')
        expected = {'Life of a bug': 'Фантастика'}
        assert collector.get_books_genre() == expected

    # verifying that books_for_children doesn't have any items from genre_age_rating
    def test_get_books_for_children_only_books_for_kids_added(self):
        collector = BooksCollector()
        collector.add_new_book('Crazy Python')
        collector.add_new_book('Snow White')
        collector.add_new_book('Good Omens')
        collector.set_book_genre('Crazy Python', 'Ужасы')
        collector.set_book_genre('Snow White', 'Мультфильмы')
        collector.set_book_genre('Good Omens', 'Комедии')
        expected = ['Snow White', 'Good Omens']
        assert collector.get_books_for_children() == expected

    # verifying a book can be added to favorites
    @pytest.mark.parametrize('name', ['Crazy Python'])
    def test_add_book_in_favorites_book_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        expected = [name]
        assert collector.get_list_of_favorites_books() == expected

    # verifying that added to favorites book can be deleted
    @pytest.mark.parametrize('name', ['Crazy Python'])
    def test_delete_book_from_favorites_book_is_deleted(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        expected = []
        assert collector.get_list_of_favorites_books() == expected

    # adding list of books to favorites and verifying that all of 'em been added
    def test_get_list_of_favorites_books_all_books_added(self):
        collector = BooksCollector()
        expected = ['Crazy Python', 'Snow White', 'Good Omens']
        for item in expected:
            collector.add_new_book(item)
            collector.add_book_in_favorites(item)
        assert collector.get_list_of_favorites_books() == expected
