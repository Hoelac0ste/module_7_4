team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s' % team1_num)
print('Итого сегодня в командах участников: %(1team)s и %(2team)s' % {'1team': team1_num, '2team': team2_num})

score_2 = 42
team1_time = 18015.2
print('Команда Волшебники данных решила задач: {score}'.format(score = score_2))
print('Волшебники данных решили задачи за : {time}'.format(time = team1_time))

score_1 = 40
challenge_result = 'Мастера кода'
tasks_total = score_1 + score_2
time_avg = 350.4
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: победа команды {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


