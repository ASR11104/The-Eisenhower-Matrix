import json
import os

def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux or macOS
        os.system('clear')

def reset_eisenhower_matrix():
    data = {
        "do_first": [],
        "do_next": [],
        "do_later": [],
        "do_never": []
    }
    return data


def print_eisenhower_matrix(data):
    # Format the matrix with the data
    print("Eisenhower Matrix:")
    print("-" * 30)
    
    print("Do First (Important & Urgent):")
    for task in data.get("do_first", []):
        print(f"  - {task}")
    
    print("\nDo Next (Important & Not Urgent):")
    for task in data.get("do_next", []):
        print(f"  - {task}")
    
    print("\nDo Later (Not Important & Urgent):")
    for task in data.get("do_later", []):
        print(f"  - {task}")
    
    print("\nDo Never (Not Important & Not Urgent):")
    for task in data.get("do_never", []):
        print(f"  - {task}")
    
    print("-" * 30)


def get_user_input(data):

    print("Eisenhower Matrix Task Input")
    print("-" * 30)

    while True:
        print("\nPlease enter a task and its importance/urgency (type 'exit' to stop):")
        
        # Ask the user for the task description
        task = input("Task: ")
        if task.lower() == "exit":
            break
        
        # Ask for importance (Yes or No)
        importance = input("Is this task important? (yes/no): ").strip().lower()
        
        # Ask for urgency (Yes or No)
        urgency = input("Is this task urgent? (yes/no): ").strip().lower()

        selection = importance[0]+urgency[0]
        if selection not in ["yy", "yn", "ny", "nn"]:
            print("Invalid input for importance or urgency. Please enter 'yes' or 'no'.")
            continue

        match selection:
            case "yy":
                data["do_first"].append(task)
            case "yn":
                data["do_next"].append(task)
            case "ny":
                data["do_later"].append(task)
            case "nn":
                data["do_never"].append(task)
        
    return data

def main():
    print("Welcome to the CLI! for The Heisenhower Project")
    eisnhower_data = json.load(open("eisenhower-data.json"))
    print_eisenhower_matrix(eisnhower_data)
    while True:
        try:
            print("Select command:")
            print("1. Add Task")
            print("2. Clear Screen")
            print("3. Reset Tasks")
            print("4 Exit")
            command = input("Enter command: ")
            if command == "1":
                get_user_input(eisnhower_data)
            elif command == "2":
                clear_screen()
            elif command == "3":
                print("Are you sure you want to reset all tasks?")
                confirm = input("Enter 'yes' to confirm: ")
                if confirm.lower() == "yes":
                    eisnhower_data = reset_eisenhower_matrix()
            elif command == "4":
                raise KeyboardInterrupt
            clear_screen()
            print_eisenhower_matrix(eisnhower_data)
        except KeyboardInterrupt:
            json.dump(eisnhower_data, open("eisenhower-data.json", "w"))
            print("\nExiting...")
            break
        except Exception as e:
            print(e)
            json.dump(eisnhower_data, open("eisenhower-data.json", "w"))
            break

if __name__=="__main__":
    main()