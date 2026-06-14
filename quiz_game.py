questions=(("What is the largest animal?:"),
           ("which animal is the fastest?:"),
           ("Which bird is the smallest?:"))
options=(("A.Whale","B.Elephant","C.Tiger"),
         ("A.Cheetah","B.Hyena","C.Rabbit"),
         ("A.Kingfisher","B.Humming Bird","C.Eagle"))

question_num=0
answer=["A","A","B"]
guess=[]
for x in questions:
    print("\n")
    print(x)
    for y in options[question_num]:
        print(y)
    user=input("Enter option(A,B,C,D):").upper()
    guess.append(user)
    if guess[question_num]==answer[question_num]:
        print("Your Answer is correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is:{answer[question_num]}")

    
    question_num+=1