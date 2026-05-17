# # # # # # #  CONTINUING THE LECTURE   #

# # # # # # # PROJECT -PERSONAL INTRODUCTION THINGY

 
# # # # # # #below is the upgraded and cleaner code of above which is my orignal creation 


# # # # # # #print("What is your name :")
# # # # # # #name=input("")    #asking for name input and naming it "name"

# # # # # # #print("state your age :")
# # # # # # #age=input("")    #asking for age input and naming it "age"

# # # # # # #print("What is your favourite hobby ?")
# # # # # # #hobby=input("")   #asking for hobby input and naming it"hobby"

# # # # # # #print("what do you want to be in the future ?")
# # # # # # #oal=input("")     #asking their life goals and naming it goals

# # # # # # #goal=goal.capitalize()
# # # # # # #goal=goal.strip()

# # # # # # #name=name.capitalize()
# # # # # # #name=name.strip()

# # # # # # #age=age.strip()

# # # # # # #hobby=hobby.capitalize()
# # # # # # #hobby=hobby.strip()


# # # # # # #print("Hello! My name is ",name)
# # # # # # #print(f"My favourite hobby is ",hobby)
# # # # # # #print("My dream  is to become an ",goal)
# # # # # # #print("Nice to meet you !")  
# # # # # # """
# # # # # # """
# # # # # # #name = input("What is your name: ").strip().capitalize()
# # # # # # #age = input("State your age: ").strip()
# # # # # # #obby = input("What is your favourite hobby: ").strip().capitalize()
# # # # # # #goal = input("What do you want to be in the future: ").strip().capitalize()

# # # # # # #print(f"Hello! My name is {name}")
# # # # # # #print(f"I am {age} years old")
# # # # # # #print(f"My favourite hobby is {hobby}")
# # # # # # #print(f"My dream is to become a {goal}")
# # # # # # #print("Nice to meet you!")




# # # # # # # trying to print all inputs in one paragraph

# # # # # # # name=input("State your name :")
# # # # # # # age=input("state your age :")
# # # # # # # hobby=input("state your hobby :")
# # # # # # # country=input("Which country are you from :")
# # # # # # # dream=input("what is your dream ?")
# # # # # # # language=input("what language you speak?")

# # # # # # # name=name.capitalize()
# # # # # # # name=name.strip()


# # # # # # # language=language.strip()
# # # # # # # language=language.capitalize()

# # # # # # # age=age.strip()
# # # # # # # hobby=hobby.capitalize()
# # # # # # # hobby=hobby.strip()
# # # # # # # dream=dream.capitalize()
# # # # # # # dream=dream.strip()
# # # # # # # country=country.capitalize()
# # # # # # # country=country.strip()


# # # # # # # print(f"{name} is a {age} year oldf from {country} who speaks  {language}, \n loves {hobby},and dreams of becoming an {dream} .")




# # # # # # # trying more cleaner code and more simple and short


# # # # # # name=input("State your name :").strip().capitalize()
# # # # # # age=input("state your age :").strip().capitalize()
# # # # # # hobby=input("state your hobby :").strip().capitalize()
# # # # # # country=input("Which country are you from :").strip().capitalize()
# # # # # # dream=input("what is your dream ?").strip().title()
# # # # # # language=input("what language you speak?").strip().capitalize()



# # # # # # print(f"{name} is a {age} year old from {country} who speaks  {language},\n loves {hobby},and dreams of becoming an {dream} .")


# # # # #      #   learning new things from here #


# # # # # # # split function

# # # # # # name=input("what is your name ?").capitalize()
# # # # # # first,last=name.split(" ")    #it seeems like we can only use .split() when there are only 2 names like "sugam kharel"  . it doesnt work if name is "dipesh kumar kharel"
# # # # # # print("hello",first)



# # # # #                      # INTEGERS #


# # # # # #making caluclator.py as shown in the lecture 0





# # # # # # # def function
# # # # # # def hello():
# # # # # #     print("hello")
# # # # # # name=input("whats your name?")
# # # # # # hello()
# # # # # # print(name)


# # # # # #def fuction try to iniclude vatiable name inside the def function too

# # # # # def hello():
# # # # #     name=input("whats your name ?")
# # # # #     print("hello ",name)

# # # # # hello()




# # # # #   using parameters 
# # # # def hello(to="world")
# # # #     name=input("whats your name?")
# # # #     print("hello ,", to)


# # # # hello()
    
# # # def hello():     #why cant i do this instead of using parameters ??? this below seems quiet simplified and easier to do insteaed of that using complex parameters

# # #     name=input("whats your name? " )
# # #     print("hello ,",name)

# # # hello()


# # def hello(name="world"):
# #     print("Hello", name)

# # name = input("What's your name? ")


# # hello(name)



# def main():

#     x=int(input("what's x ?",))
#     print("the square of x is",x*x)
    

# main()