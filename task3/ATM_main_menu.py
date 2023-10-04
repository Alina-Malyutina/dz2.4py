from ATM import ATM
from card import BankCard
import messages
import time

all_atm = []
all_cards = []
current_atm: ATM
current_card: BankCard

def start():
    while True:
        current_atm.main_menu(line_1=current_atm.bank, line_2=current_atm.address, line_4=f'1. {messages.INSERT_CARD}',
                              line_5=f'2. {messages.EXIT}')
        select_option = int(input(messages.SELECT_OPTION))
        match select_option:
            case 1:

                current_card = select_card()
                current_atm.main_menu(line_1=current_atm.bank, line_2=current_atm.address,
                                      line_4=f'1. {messages.ENTER_PIN}')
                while True:

                    pin_ok = current_atm.insert(current_card)
                    if pin_ok == messages.OPERATION_OK:
                        while True:
                            current_atm.main_menu(line_1=current_atm.bank, line_2=current_atm.address,
                                                  line_4=f'1. {messages.REPLENISH_BALANCE}', line_5=f'2. {messages.TAKE_CASH}',
                                                  line_6=f'3. {messages.CHECK_BALANCE}', line_7=f'4. {messages.EJECT_CARD}')
                            select_option = int(input(messages.SELECT_OPTION))
                            match select_option:
                                case 1:
                                    replenish_ok = current_atm.replenish_balance()
                                    current_atm.main_menu(line_1=current_atm.bank, line_2=current_atm.address,
                                                          line_4=f'{replenish_ok}')
                                    current_atm.card.save_card()
                                    time.sleep(3)
                                case 2:
                                    take_cash = current_atm.take_cash()
                                    current_atm.main_menu(line_1=current_atm.bank, line_2=current_atm.address,
                                                          line_4=f'{take_cash}')
                                    current_atm.card.save_card()
                            
                                    time.sleep(3)
                                case 3:
                                    current_atm.main_menu(line_1=current_atm.bank, line_2=current_atm.address,
                                                          line_4='Ваш баланс:',
                                                          line_5=f'{current_atm.check_balance()}')
                                    current_atm.card.save_card()
                                    time.sleep(3)
                                case 4:
                                    current_atm.card.save_card()
                                    return
                    else:
                        current_atm.main_menu(line_1=current_atm.bank, line_2=current_atm.address,
                                              line_4=f'{messages.WRONG_PIN}')
            case 2:
                return


def select_card() -> BankCard:
    [print(f'{i}. {card} \n') for i, card in enumerate(all_cards, 1)]
    choice = int(input(messages.SELECT_CARD))
    return all_cards[choice - 1]

def select_atm():
    global current_atm
    [print(f'{i}. {atm} \n') for i, atm in enumerate(all_atm, 1)]
    choice = int(input(messages.SELECT_ATM))
    current_atm = all_atm[choice - 1]


def read_atm_list():
    with open('task3\ATM_list.txt', 'r', encoding='UTF-8') as file:
        atm_list = file.readlines()
    for cur_atm in atm_list:
        atm = cur_atm.strip().split(':')
        all_atm.append(ATM(int(atm[0]), atm[1], atm[2], float(atm[3])))


def read_card_list():
    with open('task3\cards.txt', 'r', encoding='UTF-8') as file:
        card_list = file.readlines()
    for cur_card in card_list:
        card = cur_card.strip().split(':')
        all_cards.append(BankCard(card[0], card[1], card[2], float(card[3])))