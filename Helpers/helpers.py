import math
import os
import stat
from os.path import join
from os.path import isfile

from Helpers.constantes import const

class utils:
    def calc_eh(persona):
        persona.eh = persona.profession.eh + persona.get_fisico()
        return persona.eh

    def get_level(xp):
        for i in range(len(const.EVOLUTION_TABLE)):
            if xp <= const.EVOLUTION_TABLE[i]:
                return i + 1

    def get_xp_next(level):
        return const.EVOLUTION_TABLE[level - 1] + 1

    def convert_to_coins(money):
            gold = money / 100
            money = money % 100
            silver = money / 10
            copper = money % 10

            return (copper, silver, gold)

    def convert_to_coins_single(money):
            if (money % 100) == 0:
                coin = const.GOLD
            elif (money % 10) == 0:
                coin = const.SILVER
            else:
                coin = const.COPPER

            return (money / (10 ** coin), coin)

    def buy(price, coins):
        '''Argumentos: price = preco em moedas de cobre;
                       coins = dinheiro disponivel em [cobre, prata, ouro];
           Retorna:    (True se compra foi efetuada,troco)
        '''

        price_v, kind = convert_to_coins_single(price)

        if coins[kind] >= price_v:
            coins[kind] -= price_v
            deal = True

        else:
            deal = False

            conv = [0, 0, 0]
            for i in range(const.COINS):
                conv[i] = coins[i] * (10 ** i)

            price -= conv[kind]
            conv[kind] = 0

            for i in range(const.COINS):
                if conv[i] >= price:
                    conv[i] -= price
                    price = 0
                    deal = True
                else:
                    price -= conv[i]
                    conv[i] = 0

            if deal:
               coins[const.GOLD] = conv[const.GOLD] / 100
               tmp = conv[const.GOLD] % 100
               coins[const.SILVER] = tmp / 10
               coins[const.COPPER] = tmp % 10

        return (deal, coins)

    def get_image_pixbuf(path, image_file):
        image_file = join(path, image_file)
        if not image_file or not isfile(image_file):
            return None
        
        #return gtk.gdk.pixbuf_new_from_file(image_file)



