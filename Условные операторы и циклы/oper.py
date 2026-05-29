'''
Ранний возврат - это это концепт написания функций так, что ожидаемый положительный результат возвращается в конце,
если остальной код в случае расхождения с целью функции должен завершить ее выполнение настолько раньше, насколько возможно
'''

#Пример:
def process_data(data):
    if not data:
        return None
    if not validate(data):
        return None
    return result

#Когда simple value mapping (простое сопоставление значений):
def status_get_color(status):
    colors = {
        'active': 'green',
        'inactive': 'gray',
        'pending': 'yellow',
        'error': 'red'
    }
    return colors.get(status,'black')

#Когда complex logic:
def calculate_discount(user_type,amount):
    if user_type=='vip':
        return amount*0,3
    elif user_type=='regular' and amount>100:
        return amount*0,1
    else:
        return 0
#Extract complex conditions (выделение сложных условий):
can_edit = (user.is_admin or user.is_owner and not post.is_locked)
has_valid_subscription = (user.subscription_active and not user.subscription_expired and user.payment_up_to_date)
if can_edit and has_valid_subscription:
    allow_editing()

#Avoid magic numbers
#Good:
MAX_RETRIES = 3
MIN_SCORE = 70
if attemps<MAX_RETRIES and score>=MIN_SCORE:
    #...
#Bad:
if attemps<3 and score>=70:
    #...

#enumerate() для получения индекса:
#Bad:
items = ['apple','banana','cherry']
for i in range(len(items)):
    print(f"{i}: {items[i]}")
#Good:
items = ['apple','banana','cherry']
for i, item in enumerate(items,start=1): #start позволяет начать с i = n
    print(f"{i}: {item}")

#zip() для параллельной итерации
names = ['Alice', 'Bob', 'Charlie']
scores = [85,92,78]
ages = [25,30,28]
for name, score, age in zip(names,scores,ages):
    print(f"{name} ({age} лет): {score} баллов")
#с обработкой разных длин:
from itertools import zip_longest
for name, score in zip_longest(names,scores, fillvalue='N/A'):
    print(name,score)

#itertools для сложных итераций:
from itertools import chain, cycle, islice, pairwise
#Объединение итераторов
list1 = [1,2,3]
list2 = [4,5,6]
for item in chain(list1,list2):
    print(item) #1, 2, 3, 4, 5, 6
#Скользящие пары
data = [1,2,3,4,5]
for a,b in pairwise(data):
    print (f"{a} => {b}") # 1 => 2, 2 => 3 и т.д.

#Циклическая итерация
colors = ['red','green','blue']
for i, color in enumerate(cycle(colors)):
    if i>=10:
        break
    print(color)

#Вложенные циклы с product:
from itertools import product
for x, y in product(range(3),range(2)):
    print(x,y)

#Итерация с помощью itertools.groupby
from itertools import groupby
data = [1,1,2,2,2,3,1,1,1]
for key, group in groupby(data):
    count = len(list(group))
    print (f"{key: {count} раз(а)}")