total_sum = 0

def valid_input():
    while True:
        try:
            user_input = int(input("Enter int:"))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an int.")

for _ in range(5):
    user_input = valid_input()
    total_sum += user_input

print("Sum of the entered integers:", total_sum)
