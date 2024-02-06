import os
from datetime import datetime
from tinkoff.invest import Client, RequestError, OrderDirection, OrderType, Quotation
import time

TOKEN = '' # Вписываете ваш API токен Тинькофф Инвестиции

FIGI = "TCS00A1039N1" # Тинькофф Bonds идентификатор
account_id = '' # Вписываете ваш Айди Аккаунта Тинькофф Инвестиции
quantity = 10 # Вписываете кол-во для расхода на покупку Тинькофф Bonds (по-умолчанию 100 руб объем покупки)

def get_account_id():
    with Client(TOKEN) as client:
        print(client.users.get_accounts())

def run_buy():
    try:
        # Токен с правами на чтение на соотв субсчете
        with Client(TOKEN) as client:

            # Рыночная, без указания цены (по лучшей доступной для объема)
            r = client.orders.post_order(
                 order_id=str(datetime.utcnow().timestamp()),
                 figi=FIGI,
                 quantity=quantity,
                 account_id=account_id,
                 direction=OrderDirection.ORDER_DIRECTION_BUY,
                 order_type=OrderType.ORDER_TYPE_MARKET
             )

            print(r)


    except RequestError as e:
        print(str(e))


def run_sell():
    try:
        # Токен с правами на чтение на соотв субсчете
        with Client(TOKEN) as client:

            # Рыночная, без указания цены (по лучшей доступной для объема)
            r = client.orders.post_order(
                 order_id=str(datetime.utcnow().timestamp()),
                 figi=FIGI,
                 quantity=quantity,
                 account_id=account_id,
                 direction=OrderDirection.ORDER_DIRECTION_SELL,
                 order_type=OrderType.ORDER_TYPE_MARKET
             )

            print(r)


    except RequestError as e:
        print(str(e))


if __name__ == "__main__":

    for i in range(5): # Здесь укажите кол-во покупок продаж для получения необходимого обьема
        run_buy()
        time.sleep(5)
        run_sell()
        time.sleep(5)
