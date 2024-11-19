questions=[["What is capital city of Nepal","KTM","BKT",
          "banepa",1],
          ["What is capital city of India","BKT","New Dheli","BKT",
          "banepa",2],
          ["Which is the only body part that is fully grown from birth?","Eyes","heart",
          "backbone",1],
           ["Which planet is known as the Red Planet","Venus","Mars ","Jupiter",2],
           ["What is a group of crows called?","pack","flock","murder","caw",3],
           ["What is capital city of france","paris","new york","london",1],
           ["Which country is not involved in any war?","Switzerland","Nepal", "China",1],
           ["What is the most common disease that a person has?","Gastric","Sugar","Tooth",3],
           ["Which animal has three hearts ","Spider","pig","octopus",3],
          ]
levels=[1000,2000,3000,40000,60000,120000,3400000,560000,45000000,]
money=0
for i in range(0, len(questions)):


   question=questions[i]
   print(f"\n\nQuestion for Rs.{levels[i]}")
   print(f" {question[0]}    \n a. {question[1]}")
   print(f"b. {question[2]}   c. {question[3]}")
   reply=int(input("Enter your answer(1-4)"))
   if(reply==question[-1]):
      print(f"correct answer ,you have won Rs.{levels[i]}")
      if(i==4):
        money=3000000
      elif(i==9):
        money=400000000
   else:
    print("wrong answer!")
    break
   
print(f"your take home mone1y is {money}")