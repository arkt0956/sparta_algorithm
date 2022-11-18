input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_string_length = []
    for size in range(1, n // 2 + 1):
        compressed = ""
        count = 1
        splited = [string[i:i+size] for i in range(0, n, size)]
        for i in range(1, len(splited)):
            prev, cur = splited[i-1], splited[i]
            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1

        if count > 1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]
        compression_string_length.append(len(compressed))
    return min(compression_string_length)


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))