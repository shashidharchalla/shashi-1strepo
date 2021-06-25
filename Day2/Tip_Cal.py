bill = float(input("Enter the total bill $:\n"))
members = int(input("How may members to split the bill:\n"))
tip = int(input("Enter tip percentage:\n"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
bill_Per_Person = bill + bill * (tip / 100)
Total_per_person = bill_Per_Person / members
#Format the result to 2 decimal places = 33.60
Total_per_person = round(Total_per_person, 2)
print(f"Total bill per person is: ${Total_per_person}")