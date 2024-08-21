"""
Napište kód simulující zásobník knih. Třída by měla umožňovat přidávání a odebírání knih
ze zásobníku, procházet tituly v zásobníku a zobrazit poslední pozici v zásobníku.
Nezapomeňte použít magické metody.
A implementujte třídu ZasobnikKnih s níže uvedenými metodami:

pro sčítání zásobníků
porovnávání zásobníků podle počtu knih
reprezentovat zásobník jako řetězec
vrátit počet knih v zásobníku

výstup:

['Cheetahs', 'Elephants', 'Cats']
Cats
['Cheetahs', 'Elephants']
['Cheetahs', 'Elephants', 'Horses']
True
False
Stack: My Stack of Books with category of books: Natural
stack_name: My Stack of Books
category: Natural
books: ['Cheetahs', 'Elephants', 'Horses']
3
"""

from typing import List


class BooksStack:

    def __init__(self, stack_name: str, stack_category: str):
        self.stack_name = stack_name
        self.stack_category = stack_category
        self.stack = []

    def __str__(self):
        return f"Stack: {self.stack_name} with category of books: {self.stack_category}"

    def add_new_book(self, title: str):
        return self.stack.append(title)

    def get_book(self):
        return self.stack.pop()

    def all_books(self) -> List[str]:
        return self.stack

    def __add__(self, second_stack):
        new_stack = BooksStack(stack_name=self.stack_name, stack_category=self.stack_category)
        new_stack.stack = self.stack + second_stack.stack
        return new_stack

    def __gt__(self, second_stack):
        return len(self.stack) > len(second_stack)

    def __lt__(self, second_stack):
        return len(self.stack) < len(second_stack)

    def __ge__(self, second_stack: object) -> object:
        return len(self.stack) >= len(second_stack)

    def __le__(self, second_stack):
        return len(self.stack) <= len(second_stack)

    def __repr__(self):
        return f"stack_name: {self.stack_name}\ncategory: {self.stack_category}\nbooks: {self.stack}"

    def __len__(self):
        return len(self.stack)


my_books = BooksStack("My Stack of Books", "Natural")

my_books.add_new_book("Cheetahs")
my_books.add_new_book("Elephants")
my_books.add_new_book("Cats")

print(my_books.all_books())
print(my_books.get_book())
print(my_books.all_books())

her_books = BooksStack("Her Stack of Books", "Natural")
her_books.add_new_book("Horses")

my_books = my_books + her_books
print(my_books.all_books())

print(my_books > her_books)
print(my_books <= her_books)

print(my_books)
print(repr(my_books))

print(len(my_books))
