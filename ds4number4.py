# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
#  Пример:
#  k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
filter_func = lambda x: x[0]!=0 and x[1]!=0

polynome=''
k = int(input('Введите k '))
coefs_arr = [random.randint(0,3) for i in range(k)]
grade_arr = list (range(k,0,-1))

terms_pair_arr = list(filter(filter_func,zip(coefs_arr,grade_arr)))
terms_arr = list(map(lambda x: f'{x[0]}x**{x[1]}',terms_pair_arr))

for elem in terms_arr:
    polynome+=elem+' + '
c = random.randint(0,10)
if c!=0:
    polynome+=str(c)+" = 0"
print(polynome)

with open('file_polynome.txt', 'w',encoding='utf-8') as data:
    data.write(polynome)