print("Welcome to Letter Counter App")
name=input("\nWhat is your Name :").title().strip()
print("Hello, " + name + "!")
print("I will count the No. of times that a specific letter occurs in message.")
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occrrences of: ")
message = message.lower()
letter = letter.lower()
letter_count=message.count(letter)
print("\n" + name + ",your message has " + str(letter_count) + " " + letter + " 's in it.")


