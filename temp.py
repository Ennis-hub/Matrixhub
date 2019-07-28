#the variuable
TheMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

adj=["", ""]
profession= ["", "", "", ""]

#getting input from User

print("Welcome User!")
print("Let's play a game, bitch!")
neo = input("Whats your name? ")
print(f"Hello {neo}! Are you ready?")
TheMatrix= input("What do you want to know more about? ")
print(f"Oh... you want to know about {TheMatrix}?")
print(f"First, tell me what you know about {TheMatrix}")
system = input(f"What do you think {TheMatrix} is? ")
enemy = input(f"What is something negative about {system} ")
inside = input(f"Give me a relaxing noun. ")
print(f"What are four professions related to {TheMatrix}?")
for i in range(len(profession)):
    profession [i]= input(f"Profession (plural) {i+1} / {len(profession)} ")

save = input(f"What is an honorable verb? " )
unplugged = input("Now I need an past tense adjective. ")
fight = input(f"Gimme another verb! ")
print(f"Give me two negative adjectives now!")
for i in range(len(adj)):
    adj[i] = input(f"Adjective {i+1} / {len(adj)} ")


madlibsstory= (f"{TheMatrix} is a {system}, {neo}. That {system} is our {enemy}. " +
f"But when you're {inside}, you look around, what do you see? " +
f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}.The very minds " +
f"of the people we are trying to {save}. But until we do, " +
f"these people are still a part of that {system} and that makes " +
f"them our {enemy}. You have to understand, most of these people " +
f"are not ready to be {unplugged}. And many of them are so {adj[0]}, " +
f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.");
print(madlibsstory)
