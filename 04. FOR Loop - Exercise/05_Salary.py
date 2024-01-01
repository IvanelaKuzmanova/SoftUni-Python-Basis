open_tabs_number = int(input())
salary = float(input())

# facebook_tax = 150
# instagram_tax = 100
# reddit_tax = 50

for tabs in range(open_tabs_number):
    current_tab = input()
#
    if current_tab == "Facebook":
        salary -= 150

    elif current_tab == "Instagram":
        salary -= 100

    elif current_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(int(salary))



