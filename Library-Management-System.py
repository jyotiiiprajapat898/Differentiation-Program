from datetime import datetime,timedelta

today = datetime.now()

print(today.strftime("%d-%m-%Y").center(20,"-"))
print("It is your first time")
chh=input("yes or no---->").lower()
Name={"N":["Divya","Jash","Yash","Komal","Sharda"],"due_date":["02-06-2026","08-06-2026","14-06-2026","21-06-2026","29-06-2026"],"Books_issued":["The God of Small Things","Wings of Fire","Atomic Habits","The Da Vinci Code","And Then There Were None"]}
if chh in ["y","yes"]:
   name=input("Enter Your Name ").title()
   print(f"Welcome {name}")
   phone_no=int(input("enter your contact Number--->"))
   address=input("enter your address--->")
else:
   name=input("Enter Your Name ").title()
   print(f"Welcome {name}")
   id_no=int(input("enter your id Number--->"))
   if name in Name["N"]:
       i=Name["N"].index(name)
       print (f"You have to submit --->{Name["Books_issued"][i]}<--- books")
       Due_date=Name["due_date"][i]
       Books_issued=Name["Books_issued"][i]
       print(f"Your Due date is--->{Due_date}")
       Due_date = datetime.strptime(Due_date, "%d-%m-%Y")
       difference = today - Due_date
       print("Late Days:", difference.days)
       fine=difference.days*5
       print(fine)
    #    Name["N"].append(name)
    #    Name["due_date"].append(today.strftime("%d-%m-%Y"))
    #    Name["Books_issued"].append(selected_book)
 
   else:
    print("There is no book issued")
selected_book=[]
print("\n")
print("What are you going to READ today ?")
print("\n")
for books in ["1.Fiction & Literature","2.Indian Classics & History","3.Mystery & Adventure","4.Non-Fiction & Biography"]:
  print(books)
print("\n")
available_books={"Fiction & Literature":{"books":["The God of Small Things","The Alchemist","Pride and Prejudice","1984","To Kill a Mockingbird","A Tale of Two Cities"],
                 "Authors":["Arundhati Roy","Paulo Coelho","Jane Austen","George Orwell","Harper Lee","Charles Dickens"],
                 "Stocks":[4,3,6,8,1,3]},"Indian Classics & History":{"books":["The Guide","Train to Pakistan","Godan","The Discovery of India","A Suitable Boy"],"Authors":["R.K. Narayan","Khushwant Singh","Munshi Premchand"," Jawaharlal Nehru","Vikram Seth"],"Stocks":[3,4,5,2,1]},"Mystery & Adventure":{"books":["The Adventures of Sherlock Holmes","The Da Vinci Code","And Then There Were None"],"Authors":["Arthur Conan Doyle","Dan Brown","Agatha Christie"],"Stocks":[2,9,4]},"Non-Fiction & Biography":{"books":["The Story of My Experiments with Truth","Sapiens: A Brief History of Humankind","Wings of Fire","Atomic Habits"],"Authors":["Mahatma Gandhi"," Yuval Noah Harari","A.P.J. Abdul Kalam","James Clear"],"Stocks":[2,4,5,1]}}
#print(available_books)

for i in range(1, 5):
    print(i,end=" ")
print("\n")
while True:
 choice=int(input("Enter your choice" ))
 if choice==1:
  print(f"{"books":43} | {"Authors":25} | {"Stocks"}")
  for i in range(len(available_books["Fiction & Literature"]["books"])):
   #print(available_books['Fiction & Literature']['Authors'])
   print(f"{available_books["Fiction & Literature"]["books"][i]:43} | {available_books["Fiction & Literature"]["Authors"][i]:25} | {available_books["Fiction & Literature"]["Stocks"][i]}")
  print("\n")
  choice = int(input("\nEnter Book Serial Number: "))
  if 1 <= choice <= len(available_books["Fiction & Literature"]["books"]):

    index = choice - 1

    if available_books["Fiction & Literature"]["Stocks"][index] > 0:

        print(f"\nBook Issued Successfully!")
        print("Book :", available_books["Fiction & Literature"]["books"][index])
        selected_book.append(available_books["Fiction & Literature"]["books"][index])
        print("Author :",available_books["Fiction & Literature"]["Authors"][index])
       # print(selected_book)

        # Stock 1 kam kar do
        available_books["Fiction & Literature"]["Stocks"][index] -= 1

        print("Remaining Stock:", available_books["Fiction & Literature"]["Stocks"][index])

    else:
        print("Sorry! Book is out of stock.")

  else:
        print("Invalid Serial Number")
 
 elif choice==2:
  print(f"{"books":43} | {"Authors":25} | {"stocks"}")
  for i in range(len(available_books["Indian Classics & History"]["books"])):
   print(f"{available_books["Indian Classics & History"]["books"][i]:43} | {available_books["Indian Classics & History"]["Authors"][i]:25} | {available_books["Indian Classics & History"]["Stocks"][i]}")
  print("\n")
  book_choice = int(input("\nEnter Book Serial Number: "))
  if 1 <= choice <= len(available_books["Indian Classics & History"]["books"]):

    index = choice - 1

    if available_books["Indian Classics & History"]["Stocks"][index]> 0:

        print(f"\nBook Issued Successfully!")
        print("Book :", available_books["Indian Classics & History"]["books"][index])
        selected_book.append(available_books["Indian Classics & History"]["books"][index])
        print("Author :",available_books["Indian Classics & History"]["Authors"][index])

        # Stock 1 kam kar do
        available_books["Indian Classics & History"]["Stocks"][index] -= 1

        print("Remaining Stock:", available_books["Indian Classics & History"]["Stocks"][index])

    else:
        print("Sorry! Book is out of stock.")

  else:
        print("Invalid Serial Number")
 
 elif choice==3:
  print(f"{"books":43} | {"Authors":25} | {"stocks"}")
  for i in range(len(available_books["Mystery & Adventure"]["books"])):
   print(f"{available_books["Mystery & Adventure"]["books"][i]:43} | {available_books["Mystery & Adventure"]["Authors"][i]:25} | {available_books["Mystery & Adventure"]["Stocks"][i]}")
  print("\n")
  book_choice = int(input("\nEnter Book Serial Number: "))
  if 1 <= choice <= len(available_books["Mystery & Adventure"]["books"]):

    index = choice - 1

    if available_books["Mystery & Adventure"]["Stocks"][index] > 0:

        print(f"\nBook Issued Successfully!")
        print("Book :", available_books["Mystery & Adventure"]["books"][index])
        selected_book.append(available_books["Mystery & Adventure"]["books"][index])
        print("Author :", available_books["Mystery & Adventure"]["Authors"][index])

        # Stock 1 kam kar do
        available_books["Mystery & Adventure"]["Stocks"][index] -= 1

        print("Remaining Stock:", available_books["Mystery & Adventure"]["Stocks"][index])

    else:
        print("Sorry! Book is out of stock.")

  else:
        print("Invalid Serial Number")
 elif choice==4:
  print(f"{"books":43} | {"Authors":25} | {"stocks"}")
  for i in range(len(available_books["Non-Fiction & Biography"]["books"])):
   print(f"{available_books["Non-Fiction & Biography"]["books"][i]:43} | {available_books["Non-Fiction & Biography"]["Authors"][i]:25} | {available_books["Non-Fiction & Biography"]["Stocks"][i]}")
  if 1 <= choice <= len(available_books["Non-Fiction & Biography"]["books"]):

    index = choice - 1

    if available_books["Non-Fiction & Biography"]["Stocks"][index] > 0:

        print(f"\nBook Issued Successfully!")
        print("Book :", available_books["Non-Fiction & Biography"]["books"][index])
        selected_book.append(available_books["Non-Fiction & Biography"]["books"][index])
        print("Author :", available_books["Non-Fiction & Biography"]["Authors"][index])

        # Stock 1 kam kar do
        available_books["Non-Fiction & Biography"]["Stocks"][index] -= 1

        print("Remaining Stock:", available_books["Non-Fiction & Biography"]["Stocks"][index])

    else:
        print("Sorry! Book is out of stock.")

  else:
        print("Invalid Serial Number")
 else:
    print("Invalid choice")
 print("\n")
 print("Would You Like To Read More Books(y/n)")
 ch=input("Your Confirmation--->").lower().strip()
 if ch in ['y','yes']:
  for i in range(1, 5):
     print(i,end="")
  print("\n")
 else:
     print("Thank you For visiting our Library")
     break
print("You have chosen this books")
print("Selected bokks:",selected_book)

#print("How many books have you chosen")
books=int(input("Number of books---->"))
Name["N"].append(name)
Name["due_date"].append(today.strftime("%d-%m-%Y"))
Name["Books_issued"].append(selected_book)
print("\n")
print(Name)
print("Thank you For visiting our Library")
print("\n")







from datetime import datetime,timedelta

today = datetime.now()

print(today.strftime("%d-%m-%Y").center(20,"-"))
print("It is your first time")
chh=input("yes or no---->").lower()
Name={"N":["Divya","Jash","Yash","Komal","Sharda"],"due_date":["02-06-2026","08-06-2026","14-06-2026","21-06-2026","29-06-2026"],"Books_issued":["The God of Small Things","Wings of Fire","Atomic Habits","The Da Vinci Code","And Then There Were None"]}
if chh in ["y","yes"]:
   name=input("Enter Your Name ").title()
   print(f"Welcome {name}")
   phone_no=int(input("enter your contact Number--->"))
   address=input("enter your address--->")
else:
   name=input("Enter Your Name ").title()
   print(f"Welcome {name}")
   id_no=int(input("enter your id Number--->"))
   if name in Name["N"]:
       i=Name["N"].index(name)
       print (f"You have to submit --->{Name["Books_issued"][i]}<--- books")
       Due_date=Name["due_date"][i]
       Books_issued=Name["Books_issued"][i]
       print(f"Your Due date is--->{Due_date}")
       Due_date = datetime.strptime(Due_date, "%d-%m-%Y")
       difference = today - Due_date
       print("Late Days:", difference.days)
       fine=difference.days*5
       print(fine)
       del Name["N"][i]
       del Name["due_date"][i]
       del Name["Books_issued"][i]

       print("Book Returned Successfully!")
 
   else:
    print("There is no book issued")
selected_book=[]
print("\n")
print("What are you going to READ today ?")
print("\n")
for books in ["1.Fiction & Literature","2.Indian Classics & History","3.Mystery & Adventure","4.Non-Fiction & Biography"]:
  print(books)
print("\n")
available_books={"Fiction & Literature":{"books":["The God of Small Things","The Alchemist","Pride and Prejudice","1984","To Kill a Mockingbird","A Tale of Two Cities"],
                 "Authors":["Arundhati Roy","Paulo Coelho","Jane Austen","George Orwell","Harper Lee","Charles Dickens"],
                 "Stocks":[4,3,6,8,1,3]},"Indian Classics & History":{"books":["The Guide","Train to Pakistan","Godan","The Discovery of India","A Suitable Boy"],"Authors":["R.K. Narayan","Khushwant Singh","Munshi Premchand"," Jawaharlal Nehru","Vikram Seth"],"Stocks":[3,4,5,2,1]},"Mystery & Adventure":{"books":["The Adventures of Sherlock Holmes","The Da Vinci Code","And Then There Were None"],"Authors":["Arthur Conan Doyle","Dan Brown","Agatha Christie"],"Stocks":[2,9,4]},"Non-Fiction & Biography":{"books":["The Story of My Experiments with Truth","Sapiens: A Brief History of Humankind","Wings of Fire","Atomic Habits"],"Authors":["Mahatma Gandhi"," Yuval Noah Harari","A.P.J. Abdul Kalam","James Clear"],"Stocks":[2,4,5,1]}}
#print(available_books)

for i in range(1, 5):
    print(i,end=" ")
print("\n")
while True:
 choice=int(input("Enter your choice" ))
 if choice==1:
  print(f"{"books":43} | {"Authors":25} | {"Stocks"}")
  for i in range(len(available_books["Fiction & Literature"]["books"])):
   #print(available_books['Fiction & Literature']['Authors'])
   print(f"{available_books["Fiction & Literature"]["books"][i]:43} | {available_books["Fiction & Literature"]["Authors"][i]:25} | {available_books["Fiction & Literature"]["Stocks"][i]}")
  print("\n")
  choice = int(input("\nEnter Book Serial Number: "))
  if 1 <= choice <= len(available_books["Fiction & Literature"]["books"]):

    index = choice - 1

    if available_books["Fiction & Literature"]["Stocks"][index] > 0:

        print(f"\nBook Issued Successfully!")
        print("Book :", available_books["Fiction & Literature"]["books"][index])
        selected_book.append(available_books["Fiction & Literature"]["books"][index])
        print("Author :",available_books["Fiction & Literature"]["Authors"][index])
       # print(selected_book)

        # Stock 1 kam kar do
        available_books["Fiction & Literature"]["Stocks"][index] -= 1

        print("Remaining Stock:", available_books["Fiction & Literature"]["Stocks"][index])

    else:
        print("Sorry! Book is out of stock.")

  else:
        print("Invalid Serial Number")
 
 elif choice==2:
  print(f"{"books":43} | {"Authors":25} | {"stocks"}")
  for i in range(len(available_books["Indian Classics & History"]["books"])):
   print(f"{available_books["Indian Classics & History"]["books"][i]:43} | {available_books["Indian Classics & History"]["Authors"][i]:25} | {available_books["Indian Classics & History"]["Stocks"][i]}")
  print("\n")
  book_choice = int(input("\nEnter Book Serial Number: "))
  if 1 <= choice <= len(available_books["Indian Classics & History"]["books"]):

    index = choice - 1

    if available_books["Indian Classics & History"]["Stocks"][index]> 0:

        print(f"\nBook Issued Successfully!")
        print("Book :", available_books["Indian Classics & History"]["books"][index])
        selected_book.append(available_books["Indian Classics & History"]["books"][index])
        print("Author :",available_books["Indian Classics & History"]["Authors"][index])

        # Stock 1 kam kar do
        available_books["Indian Classics & History"]["Stocks"][index] -= 1

        print("Remaining Stock:", available_books["Indian Classics & History"]["Stocks"][index])

    else:
        print("Sorry! Book is out of stock.")

  else:
        print("Invalid Serial Number")
 
 elif choice==3:
  print(f"{"books":43} | {"Authors":25} | {"stocks"}")
  for i in range(len(available_books["Mystery & Adventure"]["books"])):
   print(f"{available_books["Mystery & Adventure"]["books"][i]:43} | {available_books["Mystery & Adventure"]["Authors"][i]:25} | {available_books["Mystery & Adventure"]["Stocks"][i]}")
  print("\n")
  book_choice = int(input("\nEnter Book Serial Number: "))
  if 1 <= choice <= len(available_books["Mystery & Adventure"]["books"]):

    index = choice - 1

    if available_books["Mystery & Adventure"]["Stocks"][index] > 0:

        print(f"\nBook Issued Successfully!")
        print("Book :", available_books["Mystery & Adventure"]["books"][index])
        selected_book.append(available_books["Mystery & Adventure"]["books"][index])
        print("Author :", available_books["Mystery & Adventure"]["Authors"][index])

        # Stock 1 kam kar do
        available_books["Mystery & Adventure"]["Stocks"][index] -= 1

        print("Remaining Stock:", available_books["Mystery & Adventure"]["Stocks"][index])

    else:
        print("Sorry! Book is out of stock.")

  else:
        print("Invalid Serial Number")
 elif choice==4:
  print(f"{"books":43} | {"Authors":25} | {"stocks"}")
  for i in range(len(available_books["Non-Fiction & Biography"]["books"])):
   print(f"{available_books["Non-Fiction & Biography"]["books"][i]:43} | {available_books["Non-Fiction & Biography"]["Authors"][i]:25} | {available_books["Non-Fiction & Biography"]["Stocks"][i]}")
  if 1 <= choice <= len(available_books["Non-Fiction & Biography"]["books"]):

    index = choice - 1

    if available_books["Non-Fiction & Biography"]["Stocks"][index] > 0:

        print(f"\nBook Issued Successfully!")
        print("Book :", available_books["Non-Fiction & Biography"]["books"][index])
        selected_book.append(available_books["Non-Fiction & Biography"]["books"][index])
        print("Author :", available_books["Non-Fiction & Biography"]["Authors"][index])

        # Stock 1 kam kar do
        available_books["Non-Fiction & Biography"]["Stocks"][index] -= 1

        print("Remaining Stock:", available_books["Non-Fiction & Biography"]["Stocks"][index])

    else:
        print("Sorry! Book is out of stock.")

  else:
        print("Invalid Serial Number")
 else:
    print("Invalid choice")
 print("\n")
 print("Would You Like To Read More Books(y/n)")
 ch=input("Your Confirmation--->").lower().strip()
 if ch in ['y','yes']:
  for i in range(1, 5):
     print(i,end="")
  print("\n")
 else:
     print("Thank you For visiting our Library")
     break
print("You have chosen this books")
print("Selected bokks:",selected_book)

#print("How many books have you chosen")
books=int(input("Number of books---->"))
Name["N"].append(name)
Name["due_date"].append(today.strftime("%d-%m-%Y"))
Name["Books_issued"].append(selected_book)
print("\n")
print(Name)
print("Thank you For visiting our Library")
print("\n")