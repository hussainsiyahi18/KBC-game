print("Hello World!!")
print("welcome to KBC")

qs = [ "1. Which of these is the chemical symbol for Gold?",
             "2. In the context of computers, what does 'ROM' stand for?",
             "3. Which planet is known as the 'Red Planet'?",
             "4. Who was the first Indian woman to win an Olympic medal?",
             "5. Which of these festivals is specifically associated with the harvest in Punjab?", 
             "6. The 'Fortress of Solitude' is the headquarters of which fictional superhero?",
             "7. Which Indian city is known as the 'Oxford of the East'?",
             "8. In which year did the first session of the Indian National Congress take place?",
             "9. Who was the first programmer to be credited in the history of computing?"
]

ans = [ "1. Au  \n2. Fe  \n3. Gd  \n4. Go",
        "1. Read-Only Memory  \n2. Random-Only Memory  \n3. Run-Only Memory  \n4. Real-Only Memory", 
        "1. Venus  \n2. Mars  \n3. Jupiter  \n4. Saturn",
        "1. P.T. Usha  \n2. Saina Nehwal  \n3. Karnam Malleswari  \n4. Mary Kom",
        "1. Diwali  \n2. Baisakhi  \n3. Holi  \n4. Lohri",
        "1. Batman  \n2. Superman  \n3. Spider-man \n4. Ironman",
        "1. Mumbai  \n2. Delhi  \n3. Pune  \n4. Kolkata",
        "1. 1885  \n2. 1905  \n3. 1915  \n4. 1925",
        "1. Alan Turing  \n2. Charles Babbage  \n3. Ada Lovelace  \n4. John von Neumann"
]
balance = 0
print("Let's start the game!")
while True:
    if balance < 10000:
        print("For 10,000 Rs., here is your first question:")
        print(qs[0])
        print(ans[0])
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "au" or user_ans == "1":
            print("Correct answer! You have won 10,000 Rs.")
            balance = 10000
        else:
            print("Wrong answer. The correct answer is Au. You leave with 0 Rs.")

    if balance >= 10000:
        print("For 20,000 Rs., here is your second question:")
        print(qs[1])
        print("Options: \n1. Read-Only Memory  \n2. Random-Only Memory  \n3. Run-Only Memory  \n4. Real-Only Memory")
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "read-only memory" or user_ans == "1":
            print("Correct answer! You have won 20,000 Rs.")
            balance = 20000
        else:
            print("Wrong answer. The correct answer is Read-Only Memory. You leave with 10,000 Rs.")
            balance = 10000 
        
    if balance >= 20000:
        print("For 40,000 Rs., here is your third question:")
        print(qs[2])
        print("Options: \n1. Venus  \n2. Mars  \n3. Jupiter  \n4. Saturn")
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "mars" or user_ans == "2":
            print("Correct answer! You have won 40,000 Rs.")
            balance = 40000
        else:
            print("Wrong answer. The correct answer is Mars. You leave with 20,000 Rs.")
            balance = 20000
        
    if balance >= 40000:
        print("For 80,000 Rs., here is your fourth question:")
        print(qs[3])
        print("Options: \n1. P.T. Usha  \n2. Saina Nehwal  \n3. Karnam Malleswari  \n4. Mary Kom")
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "karnam malleswari" or user_ans == "3":
            print("Correct answer! You have won 80,000 Rs.")
            balance = 80000
        else:
            print("Wrong answer. The correct answer is Karnam Malleswari. You leave with 40,000 Rs.")
            balance = 40000
            
        
    if balance >= 80000:
        print("For 1,60,000 Rs., here is your fifth question:")
        print(qs[4])
        print("Options: \n1. Diwali  \n2. Baisakhi  \n3. Holi  \n4. Lohri")
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "baisakhi" or user_ans == "2":
            print("Correct answer! You have won 1,60,000 Rs.")
            balance = 160000
        else:
            print("Wrong answer. The correct answer is Baisakhi. You leave with 80,000 Rs.")
            balance = 80000
            
    if balance >= 160000:
        print("For 3,20,000 Rs., here is your sixth question:")
        print(qs[5])
        print("Options: \n1. Batman  \n2. Superman  \n3. Spider-man \n4. Ironman")
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "superman" or user_ans == "2":
            print("Correct answer! You have won 3,20,000 Rs.")
            balance = 320000
        else:
            print("Wrong answer. The correct answer is Superman. You leave with 1,60,000 Rs.")
            balance = 160000
            
    if balance >= 320000:
        print("For 6,40,000 Rs., here is your seventh question:")
        print(qs[6])
        print("Options: \n1. Mumbai  \n2. Delhi  \n3. Pune  \n4. Kolkata")
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "pune" or user_ans == "3":
            print("Correct answer! You have won 6,40,000 Rs.")
            balance = 640000
        else:
            print("Wrong answer. The correct answer is Pune. You leave with 3,20,000 Rs.")
            balance = 320000
            
    if balance >= 640000:
        print("For 1,00,00,000 Rs., here is your eighth question:")
        print(qs[7])
        print("Options: \n1. 1885  \n2. 1905  \n3. 1915  \n4. 1925")
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "1885" or user_ans == "1":
            print("Correct answer! You have won 1,00,00,000 Rs.")
            balance = 10000000
        else:
            print("Wrong answer. The correct answer is 1885. You leave with 6,40,000 Rs.")
            balance = 640000
            
        
    if balance >= 10000000:
        print("For 7,00,00,000 Rs., here is your ninth question:")
        print(qs[8])
        print("Options: \n1. Alan Turing  \n2. Charles Babbage  \n3. Ada Lovelace  \n4. John von Neumann")
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == "ada lovelace" or user_ans == "3":
            print("7 CRORE!!!")
        else:
            print("Wrong answer. The correct answer is Ada Lovelace. You leave with 1,00,000 Rs.")

    balance = 0