#Количество выполненных ДЗ (запишите значение 12)
#Количество затраченных часов (запишите значение 1.5)
#Название курса (запишите значение 'Python')
#Время на одно задание (вычислить используя 1 и 2 переменные)

#Выведите на экран(в консоль), используя переменные, следующую строку:
#Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

Tasks=12
Hours=1.5
Course_Name='Python'
Task_Time=0

Task_Time=Hours/Tasks

print('Курс:', Course_Name, 'всего задач:',Tasks, 'затрачено часов:', Hours, 'среднее время выполнения', Task_Time, 'часа.')
#или так
print('Курс: ' +Course_Name +' всего задач:'+str(Tasks)+ ' затрачено часов: '+ str(Hours)+' среднее время выполнения '+str(Task_Time)+ ' часа.')