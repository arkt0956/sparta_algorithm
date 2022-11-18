input = 20


def find_prime_list_under_number(number):
    prime = [2]
    for i in range(3, number+1):
        for p in prime:
            if i % p == 0:
                break
        else:
            prime.append(i)

    return prime


result = find_prime_list_under_number(input)
print(result)
