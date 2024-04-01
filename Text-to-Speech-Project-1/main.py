import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to the Text-to-Speech project!")
    print("Type 'exit' to stop the program.")
    while True:
        user_input = input("Enter text to pronounce: ")
        if user_input == 'exit':
            say("Thanks for using have a good day, Bye")
            break
        say(user_input)
