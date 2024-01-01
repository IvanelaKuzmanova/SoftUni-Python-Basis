command = input()       #movie name or Finish

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

full = False

while command != "Finish":

   movie_name = command
   free_places = int(input())           #въвеждаме свободни места само ако командата не е Финиш

   tickets_bought = 0
   ticket_type = input()                # типът билет се дефинира преди втория цикъл
   while ticket_type != "End":

       tickets_bought += 1

       if ticket_type == "standard":
           standard_tickets += 1
       elif ticket_type == "student":
           student_tickets += 1
       elif ticket_type == "kid":
           kid_tickets += 1

       if tickets_bought == free_places:            #тъй като добавяме само по 1 билет на итерация, проверяваме дали местата са равни, а не дали са по-големи или равни
           full = True
           break

       ticket_type = input()


   print(f"{movie_name} - {tickets_bought / free_places :.2%} full.")           # след като са разпродадени всички билети или командата е енд

   command = input()  # movie name or Finish

total_tickets = standard_tickets + student_tickets + kid_tickets

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets :.2%} student tickets.")
print(f"{standard_tickets / total_tickets :.2%} standard tickets.")
print(f"{kid_tickets / total_tickets :.2%} kids tickets.")