from ATM import ATM
from card import BankCard




my_card = BankCard(2202202325142507, '1234', new=False)
print(my_card)

bankomat = ATM(1)
print(bankomat)

bankomat.insert(my_card)
bankomat.replenish_balance()