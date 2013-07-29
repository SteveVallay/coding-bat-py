def round_sum(a,b,c):
   return round10(a) + round10(b) +round10(c)
def round10(n):
    y = n %10
    if y  <= 5:
        return n - y
    else:
        return n -y + 10

print round_sum(16,17,18)
print round_sum(12,13,14)
print round_sum(6,4,4)
