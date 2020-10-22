def fight():
    # 定义四个变量存储数据
    my_hp = 1000
    enemy_hp = 1000
    my_power = 200
    enemy_power = 199

    # 加入循环，使游戏进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        print(my_hp)
        # 判断谁的血量小于等于0
        if my_hp <= 0:
            print("I'm lose")
            break
        elif enemy_hp <= 0:
            print("I'm win")
            break
fight()