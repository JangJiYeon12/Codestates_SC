# 아래 코드는 변경하지 마세요!
class counter:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)

@counter
def part2_tab(n):
    cnt = [0] * (n+1)

    for i in range(2, n+1):
        cnt[i] = cnt[i-1] + 1

        if i % 2 == 0:
            cnt[i] = min(cnt[i], cnt[i//2]+1)
        if i % 3 == 0:
            cnt[i] = min(cnt[i], cnt[i//3] + 1)
    
    return cnt[-1]


@counter
def part2_memo(n, memo = {}):
    pass