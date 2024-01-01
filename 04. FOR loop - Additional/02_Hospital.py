period = int(input())

patients_per_day = 0
patients_left = 0
patients_treated = 0
doctors = 7

for days in range(1, period + 1):

   if days % 3 == 0 and patients_left > patients_treated:
       doctors += 1

   current_day_patients = int(input())

   if current_day_patients > doctors:
       patients_left += (current_day_patients - doctors)
       patients_treated += doctors
   elif current_day_patients <= doctors:
       patients_treated += current_day_patients

print(f"Treated patients: {patients_treated}.")
print(f"Untreated patients: {patients_left}.")