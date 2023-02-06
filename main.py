# Creating a program for make decisions for me

from random import choice

books = ['É assim que começa', 'É assim que acaba',
         'O homem mais rico da Babilônia', 'Todas as suas (in)prefeições']

movies = ['M3GAN', 'Gato de Botas - O Último Pedido',
          'Avatar: O Caminho da Água', 'Alerta Máximo', 'A Man Called Otto']

theme = input('Hello\nFor which theme do you want suggestions?\n\n')

if theme == 'books':
    suggestion = choice(books)

    print('\nMy book suggestion for todday is {} 📚'.format(suggestion))
elif theme == 'movies':
    suggestion = choice(movies)

    print('\nMy movie suggestion for todday is {} 🎬'.format(suggestion))
else:
    print('Theme not found !-!')
