# Lebed' Pavel, Tunikov Dmitri, Federov Dmitri, 2019
# Course opt project
from Condition.Condition import Condition
from MaxValueSolver.MaxValueSolver import find_max_solution

have_money = 100
projects_count = 7
left_indexes = [0, 1]
right_indexes_1 = [2, 4, 5]
right_indexes_2 = [6, 3]
project_costs = [30, 20, 10, 10, 20, 50, 50]
project_wins = [54, 56, 12, 1, 23, 60, 59]


def explain_condition():
    print('Have money: ' + str(have_money))
    print('Project costs: ')
    print(str(project_costs))
    print('Project wins: ')
    print(str(project_wins))
    print('')


def explain_result(r_array, win, cost):
    print('Projects used (1 - used, 0 - not): ')
    for bit in r_array:
        value = 1 if bit else 0
        print(str(value), end=' ')
    print('')
    print('Max win: ' + str(win))
    print('Cost: ' + str(cost))


if __name__ == '__main__':
    explain_condition()
    condition = Condition(projects_count, left_indexes, right_indexes_1, right_indexes_2)
    res_array, wins, cost = find_max_solution(have_money, project_costs, project_wins, condition)
    explain_result(res_array, wins, cost)
