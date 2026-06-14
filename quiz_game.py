questions=(("What is the largest animal?:"),
           ("which animal is the fastest?:"),
           ("Which bird is the smallest?:"))
options=(("A.Whale","B.Elephant","C.Tiger"),
         ("A.Cheetah","B.Hyena","C.Rabbit"),
         ("A.Kingfisher","B.Humming Bird","C.Eagle"))

question_num=0
answer=["A","A","B"]
guess=[]
score=0
for x in questions:
    print("\n")
    print(x)
    for y in options[question_num]:
        print(y)
    user=input("Enter option(A,B,C,D):").upper()
    guess.append(user)
    if guess[question_num]==answer[question_num]:
        score+=1
        print("Your Answer is correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is:{answer[question_num]}")

    
    question_num+=1
print()

print("-----------",end="")
print("RESULTS",end="")
print("-----------")

print("ANSWER:",end="")
for a in answer:
    print(a,end="")
print()

print("GUESSES:",end="")
for b in guess:
    print(b,end="")
print()

score= int(score/len(questions) * 100)
print(f"Your score is {score}")