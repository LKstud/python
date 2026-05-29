import datetime
#цель: рассчитать стоимость ДОСТАВКИ
#пусть order - словарь с ключами weight, price, type
#пусть customer - словарь с ключами status, reg (где reg - дата регистрации, являющаяся классом date из библиотеки datetime), regtime (количество дней от регистрации)
#пусть address - словарь с ключами region, town, street, house
#пусть у нас есть массив fargeo, который содержит в себе отдаленные регионы
#пусть mtown - переменная, обозначающая город, в котором располагается компания доставки
#пусть у нас есть массив reggeo, который содержит в себе все регионы
currentdate = datetime.date.today()
#пусть пользователь будет считаться новым, если customer["regtime"]<=7
def calculate_delivery_cost(order,customer,address):
    if order is None:
        return {"success": False, "cost": 0, "message": "Заказ не существует"}
    if address is None:
        return {"success": False, "cost": 0, "message": "Адрес не указан"}
    if order.get("weight",0)<=0:
        return {"success": False, "cost": 0, "message": "Вес не является положительным или не существует"}
    if order.get("weight",0)>50:
        return {"success": False, "cost": 0, "message": "Вес больше 50 кг недопустим для доставки"}
    if order.get("price",0)<1000:
        return {"success": False, "cost": 0, "message": "Стоимость заказа менее 1000 рублей недопустима"}
    if order["type"]=="pickup":
        return {"success": True, "cost": 0, "message": "Заказ принят, доставка бесплатная (самовывоз)"}
    if order.get("price",0)>10000 and address["region"] not in fargeo:
        return {"success": True, "cost": 0, "message": "Заказ принят, доставка бесплатная, так как цена более 10000 рублей и регион доставки не является отдаленным"}
    if customer["status"]=="vip" and order.get("price",0)>=5000:
        return {"success": True, "cost": 0, "message": "Заказ принят, доставка бесплатная (вип клиент + заказ>5000"}
    if order.get("weight",0)<5 and address["town"]==mtown:
        currentcost = 300
    if order.get("weight",0)>=5 and order.get("weight",0)<=10 and address["town"]==mtown:
        currentcost = 500
    if order.get("weight", 0) > 10 and address["town"] == mtown:
        currentcost = 500 + (order.get("weight",0)-10)*50
    if (address["region"] in reggeo) and address["town"]!=mtown:
        currentcost = 1000+(100*order.get("weight",0))
    if customer["regtime"]<=7:
        currentcost = currentcost*0.85
    if address["region"] in fargeo:
        currentcost=currentcost*1.2
    return {"success": True, "cost": currentcost, "message": "Заказ принят"}