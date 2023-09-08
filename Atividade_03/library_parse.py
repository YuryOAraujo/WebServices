import json

LIBRARY_INFO = '''{


    "informacao": {

        "nome": "Biblioteca Municipal de Barbacena",

        "telefones": ["32 3333-3333", "32 9 9999-9999"]

    },

    "livros": {

        "romance": [

            {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "copias": 10, "emprestados": 5},

            {"titulo": "Quincas Borba", "autor": "Machado de Assis", "copias": 3, "emprestados": 3},

            {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "copias": 3, "emprestados": 0}

        ],

        "tecnologia": [

            {"titulo": "Java: como programar", "autor": "Deitel", "copias": 5, "emprestados": 4},

            {"titulo": "JavaScript: O Guia Definitivo", "autor": "David Flanagan", "copias": 5, "emprestados": 1},

            {"titulo": "C: como programar", "autor": "Deitel", "copias": 1, "emprestados": 1}

        ],

        "autoajuda": [

            {"titulo": "O Segredo", "autor": "Rhonda Byrne", "copias": 2, "emprestados": 0},

            {"titulo": "O Milagre da Manhã", "autor": "Hal Elrod", "copias": 5, "emprestados": 5},

            {"titulo": "Como Fazer Amigos e Influenciar Pessoas", "autor": "Dale Carnegie", "copias": 15, "emprestados": 8}

        ]

    }

}'''


def parse_dict(LIBRARY_INFO):
    return json.loads(LIBRARY_INFO)

def get_name(library_json):
    print('1) Qual o nome da biblioteca?')
    print(f"\t{library_json['informacao']['nome']}")

def get_phone_count(library_json):
    print('2) Quantos telefones a biblioteca possui?')
    print(f"\t{len(library_json['informacao']['telefones'])}")

def get_self_help_books_count(library_json):
    total = 0
    print('3) Quantos livros existem na categoria autoajuda?')    
    for book in library_json['livros']['autoajuda']:
        total += book['copias'] + book['emprestados']
    print(f"\t{total}")

def get_different_books_count(library_json):
    different_books = []
    print('4) Quantos livros diferentes a biblioteca possui?')
    for category in library_json['livros']:
        for book in library_json['livros'][category]:
            if book not in different_books:
                different_books.append(book)
    print(f"\t{len(different_books)}")

def get_books_count(library_json):
    total = 0
    print('5) Quantos livros totais a biblioteca possui?')
    for category in library_json['livros']:
        for book in library_json['livros'][category]:
            total += book['copias'] + book['emprestados']
    print(f"\t{total}")

def get_borrowed_romance_books_count(library_json):
    total = 0
    print('6) Quantos livros da categoria romance estão emprestados?')    
    for book in library_json['livros']['romance']:
        total += book['emprestados']
    print(f"\t{total}")

def get_borrowed_books_from_author(library_json):
    author = {}
    print('7) Qual o autor possui mais livros emprestados?')
    for category in library_json['livros']:
        for book in library_json['livros'][category]:
            if author: 
                if book['emprestados'] > author['emprestados']:
                    author = book
            else:
                author = book
    print(f"\t{author['autor']}")

def get_max_count_copies(library_json):
    most_copies = {}
    print('8) Qual o nome do livro com mais cópias?')
    for category in library_json['livros']:
        for book in library_json['livros'][category]:
            if most_copies: 
                if book['copias'] > most_copies['copias']:
                    most_copies = book
            else:
                most_copies = book
    print(f"\t{most_copies['titulo']}")
    
def get_author_book_names(library_json):
    book_list = {}
    print('9) O nome de cada autor e o nome de cada um dos seus livros.')
    for category in library_json['livros']:
        for book in library_json['livros'][category]:
            autor = book['autor']
            titulo = book['titulo']
            if autor in book_list:
                book_list[autor].append(titulo)
            else:
                book_list[autor] = [titulo]
    for author, books in book_list.items():
        print(f"\t{author}")
        for book in books:
            print(f"\t - {book}")
    
def get_category_with_most_books(library_json):
    category_count = 0
    print('10) Qual a categoria possui mais livros?')
    for category in library_json['livros']:
        book_count = 0
        for book in library_json['livros'][category]:
            book_count += book['copias'] + book['emprestados']
        if book_count > category_count:
            category_count = book_count
            categoryName = category
    print(f"\t{category}")
    
def get_book_with_bigger_title(library_json):
    title_size = 0
    print('11) Qual o livro com o maior título?')
    for category in library_json['livros']:
        for book in library_json['livros'][category]:
            if len(book['titulo']) > title_size:
                title_size = len(book['titulo'])
                book_title = book['titulo']

    print(f"\t{book_title}")
            
def get_shortest_author_name(library_json):
    shortest_author_name = None
    shortest_author_name_size = float('inf')

    print('12) Qual o autor com o menor nome?')
    for category in library_json['livros']:
        for book in library_json['livros'][category]:
            author_name = book['autor']
            author_name_size = len(author_name)

            if author_name_size < shortest_author_name_size:
                shortest_author_name = author_name
                shortest_author_name_size = author_name_size

    print(f"\t{shortest_author_name}")


def display_stats():
    library_json = parse_dict(LIBRARY_INFO)
    get_name(library_json)
    get_phone_count(library_json)
    get_self_help_books_count(library_json)
    get_different_books_count(library_json)
    get_books_count(library_json)
    get_borrowed_romance_books_count(library_json)
    get_borrowed_books_from_author(library_json)
    get_max_count_copies(library_json)
    get_author_book_names(library_json)
    get_category_with_most_books(library_json)
    get_book_with_bigger_title(library_json)
    get_shortest_author_name(library_json)

display_stats()
