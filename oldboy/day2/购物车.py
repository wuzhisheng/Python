# by luffycity.com
'''
1. 让用户输入金额
2. 选择要购买的商品加入购物车
3. 当商品的总价超过了你的金额提示余额不足
4. 让用户输入N结算,输入Q退出
5. 让用户退出后提示消费了多少钱,剩余多少钱
6. 当余额不足的时候让用户从购物车中删除多余的商品
'''
goods = [
    {'name':'电脑','price':1999},
    {'name':'鼠标','price':10},
    {'name':'美女','price':50},
    {'name':'游艇','price':20},
    {'name':'火箭','price':250},
]

shop_car = {}  # 键 == 列表的索引   值 == 商品的数量
money = input('请输入您的金额:')
if money.isdigit():
    # 这是真钱
    while 1:
        for i in range(len(goods)):
            print(i+1,goods[i]['name'],goods[i]['price'])
        # ===================商品展示======================
        choose = input('请输入您要购买的商品序号(N/结算 -- Q/退出):')
        # 让用户选择要购买的商品
        if choose.isdigit() and 0 < int(choose) <= len(goods):
            # 让用户输入商品序号并判断是不是数字以及在不在正常输入范围内
            int_index = int(choose) - 1
            # 通过用户输入的内容减一获取到goods的索引
            if shop_car.get(int_index) == None:
                # 通过get本质功能去判断商品在不在购物车中
                shop_car[int_index] = 1   # shop_car[0] = 1
                # 这个商品不存在购物车中就添加一个
            else:
                shop_car[int_index] =  shop_car[int_index] + 1
                # 这个商品在购车中存在,然后对此商品对应的数量进行加一

            # ====================让用户把商品加入到购物车中====================
            # print(shop_car)
        elif choose.upper() == 'N':
            # 结算
            # ... == pass
            # 1.2 - 1.0 == 0.2  获取到是False  一个数学算法(牛顿偏离法)导致的

                fei_yong = 0
                # 定义一个空的变量,方便以后消费进行求和

                for f in shop_car:
                    # 循环字典获取所有的健
                    fei_yong = fei_yong + shop_car[f] * goods[f]['price']
                    # 通过商品的数量和单价以及上边定义的空值获取本次消费的总价

                if int(money) - fei_yong >= 0:
                    # 判断用户的资金是不是大于消费的总价
                    for k in shop_car:
                        # 循环购物车
                        print(f'您购买的商品是{goods[k]["name"]},单价{goods[k]["price"]},数量{shop_car[k]}')
                        # 打印购物车中的商品价格和数量
                else:
                    print('余额不足')
                    for i in shop_car:
                        # 循环购物侧
                        print(i,goods[i]['name'],shop_car[i])
                        # 打印要删除的商品
                    str_del = input('请选择要删除的商品序号:')
                    # 让用户选择要删除的商品序号
                    if shop_car[int(str_del)] == 1:
                        # 判断这个商品在购物车中是不是就是一个
                        shop_car.pop(int(str_del))
                        # 是一个的时候就直接把这个商品从购物车中删除
                    else:
                        shop_car[int(str_del)] = shop_car[int(str_del)] - 1
                        # 说明购物车中这个商品不止一个对吧,对这个商品的数量进行修改 减一

        elif choose.upper() == 'Q':
            # 退出
            print(f'您此次购物消费了{fei_yong},剩余余额{int(money) - fei_yong}')
            break

        else:
            print('输入有误,请重新输入!')
else:
    # 三炮,你给假钱
    print('请正确输入!')