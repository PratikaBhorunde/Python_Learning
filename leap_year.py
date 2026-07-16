year = int(input("enter a year:"))

if year %100 == 0 and year %400 == 0:
    print(f"{year} is a leap year.")

elif year %100 != 0 and year %4 == 0:
    print("its a leap year")

else:
    print(f"{year} is not a leap year.")