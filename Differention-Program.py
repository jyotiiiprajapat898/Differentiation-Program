
print("let's play")
name=input("enter your name:")
print("welcome",name)
print(f"Let's learn differentiation together, {name}!")
print("Level-1")
# let's solve questions one by one!
questions = [
    ("sinx", "cosx", ""),
    ("cosx", "-sinx", ""),
    ("x^6", "6x^5", "x^n = nx^(n-1)"),
    ("e^x", "e^x", ""),
    ("logx", "1/x", "")
    ("5x^4", "20x^3", "mx^n = mnx^(n-1)"),
    ("tanx", "sec^2x", ""),
    ("x^4+3x^2+2", ["4x^3+6x", "4x^3+6x+0"], "d(constant)=0"),
    ("8x^2+2", ["16x", "16x+0"], ""),
    ("6x^5+3x", "30x^4+3", ""),
    ("sin^2x", "2sinxcosx", ""),
    ("cos^2x", "-2cosxsinx", "x^n = nx^(n-1)"),
    ("xe^x", "e^x+xe^x", "d(uv) = u(dv) + v(du)"),
    ("1/x", "-1/x^2", ""),
    ("6x^2+sinx", "12x+cosx", ""),
    ("xsinx", "sinx+xcosx", "")
]

count = 0

for question, answer,hint in questions:
    print("\nNext problem")
    print(question)

    if hint != "":
       print("Hint:", hint)

    Ans = input("Enter your answer: ").lower().replace(" ", "")

    if isinstance(answer, list):
      if Ans in [a.lower().replace(" ", "") for a in answer]:
        print("Well done!")
        count += 1
      else:
        print("Fail")
    else:
     if Ans == answer.lower().replace(" ", ""):
         print("Well done!")
         count += 1
     else:
        print("Fail")
print("\n")
print("your highest score:")
print(count)
if count>=10:
     print("Well Played!")
else:
     print("Good effort! Try again next time.")
print("\n")
print("Would you like to play NEXT level?")
choice = input("YES or NO: ").upper()

if choice == "YES":
    print("Wait for LEVEL 2")
else:
    print("Thank you!")



