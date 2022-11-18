import collections
import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k) -> int:
    policy: int = 0
    last_order: int = 0
    max_heap = []

    while stock <= k:
        while last_order < len(supplies) and dates[last_order] <= stock:
            heapq.heappush(max_heap, -1 * supplies[last_order])
            last_order += 1
        policy += 1
        flour = heapq.heappop(max_heap)
        stock += -1*flour

    return policy


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
