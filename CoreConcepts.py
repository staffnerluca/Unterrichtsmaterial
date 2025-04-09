# Hier benutzen wir eine Funktion von Python
print("Hallo Leute!")

# Das sind Variablen
my_name = "Luca"
my_age = 19

# Hier werden die Variablen ausgegeben
print(my_name)
print(str(my_age) + " Jahre alt")

# Hier werden zwei Werte mit einander verglichen. Wenn der Vergleich richtig ist wird der Code nach der "if" ausgeführt
# ansonsten der nach dem "else"
if my_age > 18:
    print("Du bist erwachsen")
else:
    print("Du bist ein Kind/Jugendlicher")

# Hiermit erhalten wir ein Eingabe vom Nutzer, die in user_input gespeichert wird.
user_input = input("Gib etwas ein: ")
print(user_input)

# Hiermit wird die Eingabe vom Nutzer zu einer Zahl gemacht, damit wir damit rechnen können.
user_number = int(input("Give us a number: "))
if user_number + 10 == 20:
    print("This is great")
else:
    print("not the right answer")

# while loop
number = 0
while number < 3:
    print(number)
    number += 1

# Listen
namen_aus_meiner_klasse = ["Luca", "Markus", "Daniil", "Erik"]
namen_aus_meiner_klasse[0] = "Charlotte"
namen_aus_meiner_klasse.append("Luca")

# For Loops
for num in range(3):
    print(num)

for name in namen_aus_meiner_klasse:
    print("Hallo " + name)
