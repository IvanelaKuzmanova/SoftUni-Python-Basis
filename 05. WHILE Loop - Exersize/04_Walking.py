target = 10000

current_steps = input()

total_steps = 0

while current_steps != "Going home":

    total_steps += int(current_steps)

    if total_steps >= target:
        break

    current_steps = input()

if current_steps == "Going home":           #проверка извън цикъла, ако командата е going home; последно еднократно четене на променлива и добавяне към общата сума
    current_steps = input()
    total_steps += int(current_steps)

if total_steps >= target:
    print(f"Goal reached! Good job!")
    print(f"{abs(target - total_steps)} steps over the goal!")
else:
    print(f"{abs(target - total_steps)} more steps to reach goal.")