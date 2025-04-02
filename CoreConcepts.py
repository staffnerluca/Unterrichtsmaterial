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
