quest = [
    [
        "What is the difference between a compiler and an interpreter?",
        "A) Compilers translate code line-by-line, while interpreters translate the entire source code.",
        "B) Compilers produce an executable file, while interpreters directly execute the source code.",
        "C) Compilers execute code directly, while interpreters generate bytecode.",
        "D) Compilers analyze code during execution, while interpreters analyze code before execution.",2],

    [
        "    What is object-oriented programming (OOP)?",
        "A) A programming paradigm based on procedural code execution.",
        "B) A way of organizing code based on functions only.",
        "C) A programming paradigm based on objects containing data and methods.",
        "D) A method of programming without using any objects.",3],

    [
        "    What is a variable?",
        "A) A value that remains constant throughout the program.",
        "B) A symbolic name associated with a value that can change during program execution.",
        "C) A function that takes input and produces output.",
        "D) A reserved keyword in programming languages.",2],

    [
        "What is the difference between == and === in JavaScript?",
        "A) == compares both value and type, while === only compares value.",
        "B) == compares value only, while === compares both value and type.",
        "C) == is used for assignment, while === is used for comparison.",
        "D) == is used for strict comparison, while === is used for loose comparison.",2],

    [
        "What is recursion?",
        "A) A process of writing code in a procedural manner.",
        "B) A technique for solving problems where a function calls itself.",
        "C) A way to create loops in programming languages.",
        "D) A method of error handling in programming.",2],

    [
        "What is a data structure?",
        "A) A way of organizing and storing data in a computer.",
        "B) A reserved keyword for defining classes in programming languages.",
        "C) A function used to manipulate data.",
        "D) A type of loop used in programming.",1],

    [
        "What is a linked list?",
        "A) A way to connect different data types.",
        "B) A data structure consisting of elements that each contain two pointers.",
        "C) A list of data where each element points to the previous one.",
        "D) A type of array with a fixed size.",2],

    [
        "What is a constructor in object-oriented programming?",
        "A) A function used to destroy objects.",
        "B) A method used to initialize an object's state.",
        "C) A reserved keyword for creating objects.",
        "D) A way to define methods in programming languages.",2],

    [
        "What is the difference between procedural programming and object-oriented programming?",
        "A) Procedural programming focuses on objects, while object-oriented programming focuses on procedures.",
        "B) Procedural programming focuses on data, while object-oriented programming focuses on functions.",
        "C) Procedural programming focuses on writing procedures or functions, while object-oriented programming focuses on creating objects.",
        "D)  Procedural programming does not emphasize inheritance, while object-oriented programming does.",3],

    [
        "What is Git?",
        "A) A programming language.",
        "B) A version control system used for tracking changes in source code.",
        "C) A cloud computing platform.",
        "D) A database management system.",2],

    [
        "What is the difference between a stack and a queue?",
        "A) A stack follows FIFO (First In, First Out) principle, while a queue follows LIFO (Last In, First Out) principle.",
        "B) A stack follows LIFO principle, while a queue follows FIFO principle.",
        "C) A stack and a queue are the same data structure.",
        "D) A stack and a queue both follow FIFO principle.",2],

    [
        "What is the purpose of the 'this' keyword in JavaScript?",
        "A) To refer to the current instance of a class.",
        "B) To create new instances of a class.",
        "C) To refer to the context in which a function is executed.",
        "D) To define static methods in a class.",3],

    [
        "What is an API?",
        "A) A programming language.",
        "B) A set of rules for defining functions.",
        "C) A set of rules and protocols for communication between software applications.",
        "D) A type of data structure.",3],
    [
        "What is the difference between a function declaration and a function expression in JavaScript?",
        "A) A function declaration defines a function within another function, while a function expression is standalone.",
        "B) A function declaration is hoisted, while a function expression is not.",
        "C) A function declaration defines a named function using the function keyword, while a function expression does not.",
        "D) Both function declaration and function expression can be used for defining standalone functions.",2],
    [
        "What is Big O notation?",
        "A) A way to express the output of a function.",
        "B) A method for counting the number of operations in an algorithm.",
        "C) A notation used to describe the upper bound or worst-case scenario of the time or space complexity of an algorithm.",
        "D) A notation for representing the largest element in a dataset.",3]

]
# quest=int(quest)

prize_level = [1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 500000, 10000000, 20000000, 30000000, 40000000,
               50000000,60000000,70000000 ]

money=0
for i in range(0,len(quest)):

    question=quest[i]
    # question=int('question')
    print(f"The question for prize of Rs, {prize_level[i]} on your screen now :")

    print(f" \n{question[0]}")

    print(f"       {question[1]} ")
    print(f"       {question[2]} ")
    print(f"       {question[3]} ")
    print(f"       {question[4]} ")
    # print(f"{question[3]}\n     {question[4]}\n")
    Ans=int(input(f"\nEnter your answer for the prize of Rs.{prize_level[i]} option form 0 to 4 give your opnion  "))

    if (Ans==0):
        print(" Quit Quiz")
        money=prize_level[i - 1]
        break

    if (Ans==question[-1]):
        print(f"  Your opnion is correct with prize level of Rs. {prize_level[i]}\n")

        if (i==4):
            money=10000

        elif (i==7):
            money=50000

        elif(i==10):
            money= 10000000

        elif (i==14):
            money=70000000

    else:
         print("Wrong answer")
         break

print(f"You final cash prize is {money}")






