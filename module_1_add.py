grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Biblo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students)) #=> преобразование множества в список и сортировка списка в алфавитном порядке
avg_grades_0 = (sum(grades[0]))/(len(grades[0])) #=> вычисление среднеарифметического значения вложенного списка
avg_grades_1 = (sum(grades[1]))/(len(grades[1]))
avg_grades_2 = (sum(grades[2]))/(len(grades[2]))
avg_grades_3 = (sum(grades[3]))/(len(grades[3]))
avg_grades_4 = (sum(grades[4]))/(len(grades[4]))
avg_grades = [avg_grades_0, avg_grades_1,avg_grades_2, avg_grades_3, avg_grades_4] #=> создание списка из среднеарифметических значений
students_dictionary = dict(zip(students_list, avg_grades)) #=> "склеивание" двух списков в один словарь
print(students_dictionary)
