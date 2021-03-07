def solution(n):
    digits = [digit for digit in str(n)]
    return int(''.join(sorted(digits, reverse=True)))

# str and join