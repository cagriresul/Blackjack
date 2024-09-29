import random
import clear
from email.policy import default
from random import randint

def deal_card():
    kartlar = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    kart = random.choice(kartlar)
    return kart


def skor(kartlar):
    if sum(kartlar) == 21 and len(kartlar) == 2:
        return 0

    if 11 in kartlar and sum(kartlar) > 21 :
        kartlar.remove(11)
        kartlar.append(1)
    return sum(kartlar)


def karşılaştırma(kullanıcı_skor , pc_skor):

    if kullanıcı_skor >21 and pc_skor > 21 :
        return "Kaybettiniz"

    if kullanıcı_skor == pc_skor :
        return "Beraberlik"

    elif pc_skor == 0 :
        return "Kaybettiniz"

    elif kullanıcı_skor == 0 :
        return "Kazandınız"
    elif kullanıcı_skor> 21 :
        return "Kaybettiniz"
    elif pc_skor > 21 :
        return "Kazandınız"

    elif kullanıcı_skor > pc_skor :
        return "Kazandınız"

    else :
        return "Kaybettiniz"


def oyun():
    kullanıcı_kartları = []
    pc_kartları = []
    oyun_bitti_mi = False

    for _ in range(2):
        kullanıcı_kartları.append(deal_card())
        pc_kartları.append(deal_card())

    while not oyun_bitti_mi:
        kullanıcı_skoru = skor(kullanıcı_kartları)
        pc_skoru = skor(pc_kartları)

        print(f"Senin kartlarım : {kullanıcı_kartları} , skorunuz : {kullanıcı_skoru}")
        print(f"Pc kartları : {pc_kartları} , pc skoru : {pc_skoru}")

        if kullanıcı_skoru == 0 or pc_skoru == 0 or kullanıcı_skoru > 21 :
            oyun_bitti_mi = True

        else :

            Kullanıcıya_sor = input("Eğer başka kart istiyorsanız 'y' istemiyorsannız 'n' yazın : ")
            if Kullanıcıya_sor == "evet" :
                kullanıcı_kartları.append(deal_card())
            else:
                oyun_bitti_mi = True



    while pc_kartları != 0 and pc_skoru < 17:
        pc_kartları.append(deal_card())
        pc_skoru = skor(pc_kartları)

    print(f"Senin son elin {kullanıcı_kartları} ve skorun {kullanıcı_skoru}")

    print(f"Pc son el, {pc_kartları} ve skoru {pc_skoru}")

    print(karşılaştırma(kullanıcı_skoru, pc_skoru))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    oyun()

