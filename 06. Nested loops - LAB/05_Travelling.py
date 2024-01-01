destination = input()

is_enough = False
all_visited = False

while destination != "End":

    min_budget = float(input())
    savings = 0

    while savings < min_budget:

        current_sum = float(input())
        savings += current_sum

    print(f"Going to {destination}!")
    destination = input()
