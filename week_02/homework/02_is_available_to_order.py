import collections

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "사이다"]


def is_available_to_order(menus, orders):
    dict = collections.defaultdict(int)
    for i, v in enumerate(menus):
        dict[v] = i+1
    for order in orders:
        if dict[order] > 0:
            continue
        else:
            print(order, "은/는 없는 메뉴입니다.")
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
