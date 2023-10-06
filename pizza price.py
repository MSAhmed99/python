print("Thank you for chosing pizza deliveries")

# to select the size
size = input("what size pizza do you want? S, M, or L: ").upper()  #the .upper coverts the s to S
while size not in ["S", "M", "L"]:
    print("Invalid choice. Please select S, M, or L.")
    size = input("What size pizza do you want? S, M, or L: ").upper()


add_pepperoni = input("Do you want pepperoni? Y or N? ").upper()
while add_pepperoni not in ["Y", "N"]:
    print("Invalid choice. Please select Y or N.")
    add_pepperoni = input("Do you want pepperoni? Y or N? ").upper()
  

extra_cheese = input("Do you want cheese? Y or N? ").upper()
while extra_cheese not in ["Y", "N"]:
    print("Invalid choice. Please select Y or N.")
    extra_cheese = input("Do you want extra cheese? Y or N? ").upper()


bill = 0 

if size in("S", "s"):
    bill += 15

elif size in("M", "m"):
    bill += 20

else:
    bill += 25

if add_pepperoni in("Y", "y"):
    if size == 'S':
        bill += 2
    else:
        bill += 3


if extra_cheese in("Y", "y"):
    bill += 1

print(f"The final bill is: ${bill}")
