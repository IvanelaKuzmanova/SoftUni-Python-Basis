command = input()

prime_sum = 0
non_prime_sum = 0

while command != "stop":

    if int(command) < 0:
        print(f"Number is negative.")
        command = input()
        continue

    prime = True           # булевата променлива да се дефинира в основния цикъл, над цикъла, в който се използва;
                            # aко се дефинира над основния цикъл или вътре в тялото на вложения цикъл, смята грешно
    for number in range(2, int(command)):       #командата не се включва в рейнджа, защото всяко число, модулно разделено на себе си, ще даде 0

        if int(command) % number == 0:
            prime = False
            break

    if prime:
        prime_sum += int(command)
    else:
        non_prime_sum += int(command)

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")