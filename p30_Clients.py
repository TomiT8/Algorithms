"""Úkol 2.1: Klienti

Představte si, že máte obchod a implementujeme abstraktní třídu Zákazník a 3 třídy, které z ní dědí. Tyto 3 třídy reprezentují skupiny zákazníků, a to:

Ženy
Muži
Děti
Každá z těchto skupin by měla být oslovována jiným způsobem: ženy jako Paní, muži jako Pan a pro děti bez přívlastků.

"Nápověda"
Každá třída by měla mít vlastní reprezentaci řetězce __str(self)__.
"""

import abc
from collections import deque
import time


class Client(abc.ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class Woman(Client):
    def __str__(self) -> str:
        return f'Pani {self.first_name} {self.last_name}'


class Man(Client):
    def __str__(self) -> str:
        return f'Pán {self.first_name} {self.last_name}'


class Child(Client):
    def __str__(self) -> str:
        return  f'{self.first_name} {self.last_name}'


"""Úkol 2.2: Implementace fronty
Zatímco v případě zásobníku je poslední přidaná položka první, která zásobník opustí,
U fronty je to jinak: první přidaná položka jej také opustí jako první. Jedná se
o pravidlo známé jako First In, First Out - První dovnitř, První ven.

V tomto podúkolu implementujete třídu FifoList pomocí seznamu (list).
V tomto případě by přidání prvku mělo spočívat v použití metody seznamu append.
A odstraněn by měl být první prvek seznamu pomocí pop(0).
"""

class FifoList:
    def __init__(self):
        self.data = []

    def append(self, data):
        self.data.append(data)

    def pop(self):
        if self.data:
            return self.data.pop(0)
        return None


"""
Úkol 2.3: Pokladna
Implementujte třídu CashRegister, která bude simulovat operace v obchodě.
CashRegister by měla mít frontu a být schopna přidat a obsloužit nové zákazníky.
Použijte implementovanou Frontu z předešlého úkolu.
"""

class CashRegister:
    def __init__(self):
        self.queue = FifoList()

    def add_client(self, client: Client):
        self.queue.append(client)

    def process(self) -> Client:
        client = self.queue.pop()
        # print(f"Process client: {client}")
        return client


"""Úkol 2.4: Rychlejší pokladna
Pro implementaci fronty není použití seznamu optimální. Musíme odstranit položku ze začátku, a to je nákladná operace,
která vyžaduje kopírování všech položek seznamu. Odebraní prvku ve finále trvá úměrně délce seznamu.

Abychom operaci s frontou optimalizovali, vytvoříme novou třídu s využitím typu deque (obousměrná fronta),
který je k dispozici v modulu collections. deque má metody známé ze seznamu, tj. append a pop. Má také metody
popleft a appendleft. Chcete-li implementovat chování fronty, použijte metody append a popleft nebo appendleft a pop.
"""

class FasterCashRegister(CashRegister):

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def process(self):
        client = self.queue.popleft()
        # print(f"Process client: {client}")
        return client


if __name__ == '__main__':
    client1 = Woman("Anna", "Johnson")
    client2 = Man("John", "Smith")
    client3 = Child("Chris", "Novak")

    print(client1)
    print(client2)
    print(client3)

    cr = CashRegister()
    cr.add_client(client1)
    cr.add_client(client2)
    cr.add_client(client3)

    cr.process()
    cr.process()
    cr.process()


"""Úkol 2.5 Ověřte, že RychlaFronta je opravdu rychlejší
Porovnejte rychlost obou přístupů a ověřte, jestli je FasterCashRegister opravdu rychlejší než Pokladna.
Ideálně využijte modul timeit, která je vhodnější, ale můžete vyzkoušet také modul time.
"""

start = time.time()

cr = CashRegister()
ran = 400000
for i in range(ran):
    cr.add_client(client1)
for i in range(ran):
    cr.process()
print(f"CashRegister: {time.time() - start}")

start = time.time()

cr = FasterCashRegister()
for i in range(ran):
    cr.add_client(client1)
for i in range(ran):
    cr.process()
print(f"FasterCashRegister: {time.time() - start}")

print(f"Count client: {ran}")
