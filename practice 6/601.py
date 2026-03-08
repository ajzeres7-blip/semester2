n=int(input())
lst=list(map(int, input().split()))
def sum_of_squares(a):
    return sum(x**2 for x in a)
print(sum_of_squares(lst))