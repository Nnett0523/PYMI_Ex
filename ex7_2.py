#!/usr/bin/env python3
import random
'''
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

'''


class Fighter():
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def __str__(self):
        return self.name + str(self.HP)

    # Add more if needed


class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def __str__(self):
        return self.name + str(self.damage)
    
def solve(player1, player2):
    '''Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)'''
    result = ('', 0)

    shortGun = Weapon('Short Gun', 10)
    longGun = Weapon('Long Gun', 12)
    bomb = Weapon('Bomb', 20)
    dagger = Weapon('Dagger', 9)
    ak = Weapon('AK-47', 11)
    gunAiming = Weapon('Gun Aiming', 21)

    weapons = [shortGun, longGun, bomb, dagger, ak, gunAiming]

    weapon_player_1 = random.choice(weapons)
    weapon_player_2 = random.choice(weapons)

    _round = 1
    HP_1 = player1.HP
    HP_2 = player2.HP

    while HP_1 > 0 and HP_2 > 0: 
        print('----------Round %d----------' % _round)
        HP_1 -= weapon_player_2.damage
        print('Player: ', player1.name, \
                'HP: ', HP_1, \
                'Weapon: ', weapon_player_1.name)
        HP_2 -= weapon_player_1.damage
        print('Player: ', player2.name, \
                'HP: ', HP_2, \
                'Weapon: ', weapon_player_2.name)

        weapon_player_1 = random.choice(weapons)
        weapon_player_2 = random.choice(weapons)
        _round += 1

    if HP_1 <= 0 and HP_2 > 0:
        result = (player2.name, HP_2)
    elif HP_1 > 0 and HP_2 <= 0:
        result = (player1.name, HP_1)
    elif HP_1 <= 0 and HP_2 <= 0:
        player1.HP = 0
        player2.HP = 0
        return result
        
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # def attack(player1, player2):

    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter('Rick', 100)
    player2 = Fighter('Negan', 100)
    print(solve(player1, player2))


if __name__ == "__main__":
    main()
