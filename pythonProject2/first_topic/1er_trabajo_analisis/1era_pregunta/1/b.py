def sum_reverse(series):
    total = 0
    for i in range(len(series) - 1, -1, -1):
        print(f'summing {series[i]} to total = {total}')
        total += series[i]
    return total

series = [1, 2, 3, 4, 5]
print("Sum in reverse order:", sum_reverse(series))