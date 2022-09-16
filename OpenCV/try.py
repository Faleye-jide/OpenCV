# nums = [1, 2, 3, 4, 5, 6]

# def is_odd(num):
#     return num % 2 == 0

# result = list(filter(is_odd, nums))
# print(result)

# output = ['yes' if num % 2 != 0 else 'No' for num in nums]
# ans = []
# for x in output:
#     if x == 'yes':
#         ans.append(x)
        
# print(ans)

result = None

a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))

try:
    result = a / b
except Exception as e:
    print('Error', e)
    

print('RESULT', round(result, 2))
print('End')