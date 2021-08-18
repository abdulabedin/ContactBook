from contactbook import Contact
def menu():
  print("""Chose an option:
           1) Add a contact
           2) Delete a contact
           3) Find a contact 
           4) Update a contact
           5) Exit contact book""")
while True:
  menu()
  choice = int(input("Choice: "))
  info = Contact()
  if choice == 1:
    info.add()
  elif choice == 2:
    info.delete()
  elif choice == 3:
    info.retrive()
  elif choice == 4:
    info.update()
  elif choice ==5:
    break