from typing import List, Tuple


if __name__ == "__main__":
    tasks: List[Tuple[int, int]] = []

    # read game input
    nb_tasks = int(input())
    for _ in range(nb_tasks):
        starting_day, duration = map(int, input().split())
        ending_day = starting_day + duration - 1
        tasks.append((starting_day, ending_day))

    # Greedy Iterative Activity Selector
    tasks.sort(key=lambda task: task[1])
    nb_selected_tasks = 1
    previous_task_index = 0
    for i in range(1, nb_tasks):
        _, previous_end_day = tasks[previous_task_index]
        starting_day, _ = tasks[i]
        # check if task doesn't overlap
        if starting_day > previous_end_day:
            nb_selected_tasks += 1
            previous_task_index = i

    print(nb_selected_tasks)
