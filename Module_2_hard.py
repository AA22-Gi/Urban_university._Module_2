"""
Задание "Слишком древний шифр":
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали
в ловушку местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки)
с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.

К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус,
где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно).

Во вторую вставку нужно было написать те пары чисел друг за другом,
чтобы число из первой вставки было кратно сумме их значений.
Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20)
программа выдавала нужный пароль result, для одного введённого числа.
"""

n = int(input('Введите число от 3 до 20: '))
result = []

for i in range(1, 21):
    for e in range(1, 21):
        if n % (i + e) == 0 and i != e:
            if str(i) not in result or str(e) not in result:
                result.append(str(i))
                result.append(str(e))

result = ''.join(result)
print(f'Паролем для числа {n} является - {result}')
