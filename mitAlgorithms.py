def f(n):
    assert n >= 0
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer


def fact(n):
    assert n >= 0
    if n <= 1:
        return
    else:
        return n * fact(n - 1)


def g(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x


def h(x):
    assert type(x) == int and x >= 0
    answer = 0
    s = str(x)
    for c in s:
        answer += int(c)
    return answer


print(f(1))
print(fact(1))
print(g(1))
print(h(1))
