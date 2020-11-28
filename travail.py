# Petit questionaire pour un utilisateur
print("Bonjour, je suis Anthony et je veut te demander quelques questions, quand tu est pret, repond avec 1")
ready = input()
if ready=="1":
    print("C'est quoi ton nom?")
userName = input()
print("Bonjour, "+ userName)
print("Quel age as tu?")
age = input()
print("Ahh tu est " + age + ", j'ai 17 ans")
print("6 fois quoi donne 36?")
x = input()
if x=="6": 
    print("Correct!")
elif x!="6": 
    print("Incorrect, la reponse est 6")
print("C'est quoi 1.5 + 2.6")
c = input()
if c=="4.1":
    print("Correct!")
elif c!="4.1":
    print("Incorrect, la reponse est 4.1")
print("Merci pour avoir répondu aux questions, c'est finis! Bonne journée")