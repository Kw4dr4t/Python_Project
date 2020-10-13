import functools
from time import time


def time_it(func):
    """
    [time_it(func):
    Check execution time of a given function]
    Returns:
    _time_it: Total execution time in seconds
    """

    @functools.wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time()))
        try:
            return func(*args, **kwargs)
        finally:
            end = int(round(time())) - start
            print(f"Total execution time: {end if end > 0 else 0} s")

    return _time_it


runCount = 0


def hanoi(n, a, b, c):
    global runCount
    runCount += 1
    if n == 1:
        print("Move", str(n), ":", "from", a, "to", c, "\n")
    else:
        hanoi(n - 1, a, c, b)
        print("Move", str(n), ":", "from", a, "to", c, "\n")
        hanoi(n - 1, b, a, c)


@time_it
def main():
    n = int(input("Please enter the number of discs: \n"))
    hanoi(n, "A", "B", "C")


if __name__ == "__main__":
    main()
print("Minimum of moves: ", runCount)
