import time

input = "abcba"

start_time = time.time()


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


print(is_palindrome(input))

end_time = time.time()
print("성능 측정", end_time-start_time)