def start_game():
    print("🌟 Welcome to the Adventure Game!")
    print("You are in a dark forest. Two paths lie ahead.")

    choice1 = input("Do you go left or right? (left/right): ").lower()

    if choice1 == "left":
        print("You meet a friendly dragon who gives you treasure. 🎁 You win!")
    elif choice1 == "right":
        print("You fall into a pit. 💀 Game over!")
    else:
        print("Invalid choice. The game ends.")

if __name__ == "__main__":
    start_game()
