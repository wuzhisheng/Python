''''''
'''
购物车
1. 用户先给自己的账户充钱：比如先充3000元。
2. 页面显示 序号 + 商品名称 + 商品价格，如：
        1 电脑 1999 
        2 鼠标 10
        …
        n 购物车结算
3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
5. 用户输n入为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
6. 用户输入Q或者q退出程序。
7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
'''
goods=[
{"name":"主机","price":1000},
{"name":"视频","price":100},
{"name":"鼠标","price":20},
{"name":"cpu","price":100},
]
# ===================商品展示======================
good_car={}
wallet=input("您账户金额：")
if wallet.isdigit():
    while 1:
        for l1 in range(len(goods)):
            print(l1+1,goods[l1]["name"],goods[l1]["price"])

# ====================让用户把商品加入到购物车中====================

        choose=input('请选择您购买商品序号(N为结算，Q为退出)：')
        if choose.isdigit() and 0<int(choose)<len(goods):
            index=int(choose) - 1
            if good_car.get(index) ==  None:
                good_car[index]=1
                print(good_car)
            else:
                good_car[index]=good_car[index] + 1
                print(good_car)

# ==================== N 的情况  ====================

        elif choose.upper() == 'N':
            sum = 0
            for l in good_car:
                sum = sum + good_car[l] * goods[l]['price']
                print(sum)
            if int(wallet) - sum >= 0:
                for l2 in good_car:
                    print(f'购买商品{goods[l2]["name"]},价格为{goods[l2]["price"]}，数量为{good_car[l2]}')
            else:
                print("您余额不足")
                for l3 in good_car:
                    print(l3,goods[l3]["name"],good_car[l3])
                good_del=input("请输入您要删除商品序号：")
                if good_car[int(good_del)] == 1:
                    good_car.pop(int(good_del))
                    print(good_car)
                else:
                    good_car[int(good_del)]=good_car[int(good_del)] -1
                    print(good_car)

        # ==================== Q 的情况  ====================

        elif choose.upper() == 'Q':
            print(f'您总消费{sum},余额{int(wallet) - sum }')
            break
        else:
            print("您输入有误，请重新输入")
else:
    print("请交真币")



'''
购物车
1. 用户先给自己的账户充钱：比如先充3000元。
2. 页面显示 序号 + 商品名称 + 商品价格，如：
        1 电脑 1999 
        2 鼠标 10
        …
        n 购物车结算
3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
6. 用户输入Q或者q退出程序。
7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
'''

# wallet = int(input("请输入您的总资产："))
# while True:
#     print("下面是商品展示：")
#     commodity = [
#         {"name": "电脑", "price": 1999},
#         {"name": "鼠标", "price": 10},
#         {"name": "键盘", "price": 50},
#         {"name": "内存条", "price": 100},
#     ]
#
#     for n1 in range(len(commodity)):
#         print(n1 + 1, commodity[n1]["name"], commodity[n1]["price"])
#     user_list = {}
#     sum = 0
#     while True:
#         nu1 = input("请输入商品序号,退出请按Q|q）：").upper()
#         if nu1 == "Q":
#             break
#         else:
#             nu2 = input("输入选择的商品的数量：")
#             user_list[nu1] = nu2   #记录商品序号和份数
#             print("您购买的{}，数量为{}".format(commodity[int(nu1) - 1]["name"], nu2))
#             sum1 = commodity[int(nu1) - 1]["price"] * int(nu2)
#             sum = sum + sum1
#
#     print("购买商品总花费为：" + str(sum))
#     if sum <= int(wallet):
#         print("购买成功！您的资产剩余为：{}".format((int(wallet) - sum)))
#     else:
#         print("余额不足，购买失败！")
#     wallet = wallet - sum
#     assure = input("继续购买请输Y，N退出：").upper()
#     if assure == "N":
#         break

