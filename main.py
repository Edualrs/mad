# Creating a program for make decisions for me

from random import choice

with open('books.txt') as bookList: # Create a list from the given file
    books_newline = bookList.readlines()
    books = []
    for i in books_newline:
        books.append(i.strip()) # Stripping the \n from the end of each list item
            
with open('movies.txt', encoding='utf-8') as movieList: # Create a list from the given file
    movies_newline = movieList.readlines()
    movies = []
    for i in movies_newline:
        movies.append(i.strip()) # Stripping the \n from the end of each list item  

theme = input('Hello\nFor which theme do you want suggestions?\n')

if theme == 'books':
    suggestion = choice(books) # Choose an item from the book list

    print('\nMy book suggestion for todday is {} 📚'.format(suggestion))
elif theme == 'movies':
    suggestion = choice(movies) # Choose an item from the movie list

    print('\nMy movie suggestion for todday is {} 🎬'.format(suggestion))
else:
    print('Theme not found !-!')
