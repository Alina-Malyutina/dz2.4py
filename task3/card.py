import random


class BankCard:
    def __init__(self, card_number: str = '', pin: str = '', owner: str = '', balance: float = 0):
        self.number = card_number
        self.owner = owner
        self.balance = balance
        self.__pin = pin


    def increase(self, amount: float):
        self.balance += amount
        return True

    def decrease(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return True

    def check_pin(self, pin: str):
        if self.__pin == pin:
            return True

    def save_card(self):
        with open('task3\cards.txt', 'r', encoding='UTF-8') as file:
            card_list = file.readlines()
        for i, card in enumerate(card_list):
            if self.number in card:
                card_list.pop(i)
                card_list.append(f'{self.number}:{self.__pin}:{self.owner}:{self.balance}')
        with open('task3\cards.txt', 'w', encoding='UTF-8') as file:
            file.write('\n'.join([card.strip() for card in card_list]))


    def __str__(self):
        return f'Карта {self.number}\nНа имя: {self.owner}\nPin: ****'