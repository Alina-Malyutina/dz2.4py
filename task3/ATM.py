from card import BankCard
import messages

class ATM:
    def __init__(self, index: int, bank: str, address: str, balance: float):
        self.index = index
        self.bank = bank
        self.address = address
        self._balance = balance
        self.card: BankCard = None

    def main_menu(self, line_1: str = '', line_2: str = '', line_3: str = '',
                  line_4: str = '', line_5: str = '', line_6: str = '',
                  line_7: str = '', line_8: str = '', line_9: str = ''):
        print('\n' * 20)
        print('╔' + '═' * 31 + '╗')
        print(f'║{line_1:^31}║')
        print(f'║{line_2:^31}║')
        print(f'║{line_3:^31}║')
        print(f'║{line_4:^31}║')
        print(f'║{line_5:^31}║')
        print(f'║{line_6:^31}║')
        print(f'║{line_7:^31}║')
        print(f'║{line_8:^31}║')
        print(f'║{line_9:^31}║')
        print('╚' + '═' * 31 + '╝')

    def insert(self, card: BankCard):
        pin = input(messages.ENTER_PIN)
        if card.check_pin(pin):
            self.card = card
            return messages.OPERATION_OK
        else:
            return messages.WRONG_PIN

    def take_cash(self):
        if self.card:
            self.luxury_tax()
            amount = float(input(messages.CASH_AMOUNT))
            tax = amount * 0.15
            if tax < 30:
                amount += 30
            elif tax > 600:
                amount += 600
            else:
                amount += tax
            if amount < self._balance:
                if self.card.decrease(amount):
                    self._balance -= amount
                    return messages.OPERATION_OK
            else:
                return messages.NOT_ENOUGH_BALANCE
        else:
            return messages.INSERT_CARD


    def replenish_balance(self):
        if self.card:
            self.luxury_tax()
            amount = float(input(messages.CASH_AMOUNT))
            if self.card.increase(amount):
                self._balance += amount
                return messages.OPERATION_OK
        else:
            return messages.INSERT_CARD

    def check_balance(self):
        self.luxury_tax()
        return self.card.balance

    def luxury_tax(self):
        if self.card.balance > 5000000:
            self.card.balance -= self.card.balance / 10

    def __str__(self):
        return f'Банкомат: {self.bank} #{self.index}\nАдрес: {self.address}'