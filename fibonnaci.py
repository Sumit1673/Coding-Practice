cube = lambda x: x**3 # complete the lambda function 

def fibonacci_1(n):
    # return a list of fibonacci numbers
    res = [0,1]
    first = 0
    second = 1
    while len(res) < n:
        sum_ = res[first] + res[second]
        res.append(sum_)
        first += 1
        second += 1     
    
    return res

def fibonacci_2(n):
     # return a list of fibonacci numbers
     # slower when list is very long
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])
    
def fibonacci_3(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    # n = int(input())
    print(list(map(cube, fibonacci_3(5))))
