class collatz:
    cnt = 0
    def __init__(self, num):
        self.num = num
        while collatz.cnt<500:
            if num % 2 ==0:
                num /= 2
                collatz.cnt += 1
            else:
                num *= 3
                num += 1
                collatz.cnt += 1
            if num == 1:
                print(collatz.cnt)
                collatz.cnt =0
                break
            if collatz.cnt ==500:
                print(-1)
                collatz.cnt =0
                break
collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1
