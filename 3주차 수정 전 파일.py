n, ans = input(), 0

def factorial(n):
    for i in n:
        ans = ans + i
    return ans

print(f"입력하신 n!의 값은 바로: {factorial(n)}")