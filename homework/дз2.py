

def calculate(x,y)->int:
    result = (x - y) / (1 + x * y)
    return result
x = 1000
y = 500
result = calculate(x,y)
print(result)