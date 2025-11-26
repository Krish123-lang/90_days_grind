# import random

# def play_game():
#     secret_number = random.randint(1, 100)
#     print(secret_number)
#     attempts = 7
    
#     print(f"You have {attempts} attempts to guess it.\n")
    
#     while attempts > 0:
#         try:
#             user_guess = int(input("Enter your guess: "))
            
#             # Validate input range
#             if user_guess < 1 or user_guess > 100:
#                 print("Please enter a number between 1 and 100.")
#                 continue
            
#             attempts -= 1
            
#             if user_guess == secret_number:
#                 print(f"Congratulations! You guessed it correctly in {7 - attempts} attempts!")
#                 return True
#             elif user_guess < secret_number:
#                 print(f"Too low! Try again. ({attempts} attempts left)")
#             else:
#                 print(f"Too high! Try again. ({attempts} attempts left)")
        
#         except ValueError:
#             print("Invalid input! Please enter a valid number.")
    
#     print(f"Game Over! The number was {secret_number}. Better luck next time!")
#     return False


# def main():
#     """Main function to run the game with replay option."""
#     while True:
#         play_game()
#         play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
#         if play_again not in ['yes', 'y']:
#             print("Thanks for playing! Goodbye! ")
#             break


# if __name__ == "__main__":
#     main()




import random
import sys
secret_num=random.randint(1, 20)
print(secret_num)
attempts=3

while attempts>0:
    try:
        user_guess=int(input("Enter a number between 1 to 20: "))    
        if user_guess<0 or user_guess>20:
            print("Please enter the number between 1 to 20 !!")
            continue
        attempts -= 1
        
        if user_guess == secret_num:
            print("Congratulations! You've won.")
            break
        elif user_guess<secret_num:
            print(f"To low! You've {attempts} left.")
        elif user_guess>secret_num:
            print(f"To high! You've {attempts} left.")
        else:
            print('Something went wrong!')
    except ValueError:
        print("Please enter the valid number!")
        
    print(f"Sorry! you've lost. The correct number is {secret_num}")
    break
      
    