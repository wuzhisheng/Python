wallet=int(input("请输入您的金额："))
goods=[
{"name":"鼠标","price":10},
{"name":"电脑","price":1000},
{"name":"cpu","price":200},
{"name":"键盘","price":300}
]
goods_car = {}
while 1:
    for n1 in range(len(goods)):
        print(n1+1,goods[n1]["name"],goods[n1]["price"])

    choose=input("请输入您选购商品序号（N结束，Q退出）:")
    if choose.isdigit() and 0<int(choose)<len(goods):
        index = int(choose) - 1
        if goods_car.get(index) == None:
            goods_car[index] = 1
            print(goods_car)
        else:
            goods_car[index] = goods_car[index] + 1
            print(goods_car)
    elif choose.upper() == "N":
        sum=0
        for n2 in goods_car:
            sum=sum+goods[n2]["price"]*goods_car[n2]
            print(f"购买商品金额为{sum}")
        if wallet < sum :
            for n2 in goods_car:
                print(f'{n2},{goods[n2]["name"]},{goods_car[n2]}')
        else:
            print("您的余额不足")
            goods_del=input("请输入删除商品序号:")
            if goods_car[int(goods_del)] == 1:
                goods_car.pop(int(goods_del))
                print(goods_car)
            else:
                goods_car[int(goods_del)]=goods_car[int(goods_del)] - 1
                print(goods_car)