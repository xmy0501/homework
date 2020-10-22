# 回合制游戏
# 一回合

#定义一个fight方法
def fight():
    # 定义四个变量存储数据
    my_hp = 1000
    enemy_hp = 1000
    my_power = 200
    enemy_power = 200

    # 定义最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power
    # 判断输赢
    if my_final_hp > enemy_final_hp:
        print("I'm win")
    elif enemy_final_hp < enemy_final_hp:
        print("I'm lose")
    else:
        print("draw")
fight()