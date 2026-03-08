from face_auth import authenticate
from voice_command import listen
from task_manager import execute

def main():

    print("Starting Zeno AI Assistant...")

    if not authenticate():
        print("Authentication Failed")
        return

    print("Welcome to Zeno")

    while True:

        command = listen()

        if command == "":
            continue

        if "exit" in command or "stop" in command:
            print("Goodbye")
            break

        execute(command)

if __name__ == "__main__":
    main()