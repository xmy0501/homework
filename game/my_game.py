# 定义一个fight方法
# 引入random 模块
import random

def fight(my_hp, my_power, enemy_hp, enemy_power):
    # print(f"我的血量是：{my_hp}")
    # print(f"我的攻击力是：{my_power}")
    # print(f"敌人的血量是：{enemy_hp}")
    # print(f"敌人的血量是：{enemy_power}")

    # 添加while循环，使游戏进行多轮
    while True:
        # 血量计算方式
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 判断血量多少定输赢
        if my_hp >= enemy_hp:
            print("我赢了")
            print(f"我最终的血量是{my_hp}, 敌人的最终血量是{enemy_hp}")
            break
        elif my_hp <= enemy_hp:
            print("我输了")
            print(f"我最终的血量是{my_hp}, 敌人的最终血量是{enemy_hp}")
            break
        elif my_hp == enemy_hp:
            print("平局")
            print(f"我最终的血量是{my_hp}, 敌人的最终血量是{enemy_hp}")
            break

# 定义main方法，利用列表推导生成随机值
if __name__ == "__main__":
    # 生成hp随机值
    hp = [x for x in range(950, 1050)]
    # 我的血量从hp列表随机获取
    my_hp = random.choice(hp)
    # 敌人的血量从hp列表中随机获取
    enemy_hp = random.choice(hp)
    # 打印输出我和敌人的血量分别使多少
    print(f"我的随机血量{my_hp}, 敌人的随机血量{enemy_hp}")
    # 随机获取我的攻击力
    my_power = random.randint(150, 200)
    # 随机获取敌人的攻击力
    enemy_power = random.randint(100, 150)
    # 打印输出我和敌人的攻击力分别使多少
    print(f"我的随机攻击力{my_power}, 敌人的随机攻击力{enemy_power}")
    #调用fight方法实现游戏
    fight(my_hp, my_power, enemy_hp, enemy_power)


