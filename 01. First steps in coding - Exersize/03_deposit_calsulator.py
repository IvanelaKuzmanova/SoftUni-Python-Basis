deposit=float(input())
months=int(input())
divident_percentage=float(input())/100

monthly_divident=(deposit*divident_percentage)/12

final_sum=deposit+(months*monthly_divident)

print(final_sum)

