import random  # Import random module

def random_integer(min, max):
    """
    Generates Random integer in the given range.
    Parameters:
    min: Number starting the range
    max: Number ending the range
    Output: Random Number between the specified range
    """
    return random.randint(min, max)


def random_math_operator():
    """
    Randomly select one of the three operators.
    Output: Any 1 of 3 operators
    """
    return random.choice(['+', '-', '*'])  # Out of 3 Mathematical operators 1 will be selected


def math_function(n1, n2, o):
    """
    Perform Mathematical Operation
    Parameters:
    num_1: First random integer
    num_2: Second random integer
    Output:
    p: String of the operation being performed
    a: Answer
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    """
    Function will ask for user inputs. Reward points for each correct answer and print the score at the end
    """
    counter = 0
    num_times = 3  # Let the Quiz run for 3 Loops

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_times):
        num_1 = random_integer(1, 10)  # n1 Integer between 1 to 10
        num_2 = random_integer(1, 5)   # n2 Integer between 1 to 5
        operator = random_math_operator()  # select a random operator

        PROBLEM, ANSWER = math_function(num_1, num_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        
        try: # Error Handling Loop
            useranswer = int(useranswer)  # Converting data type to Integer
            if isinstance(useranswer, int):
                print("You entered a correct integer input!")
            else:
                print("Please enter a valid data type.")
        except ValueError:
            print("Please enter a valid data type.")

        if useranswer == ANSWER:  # Compare user answer with actual
            print("Correct! You earned a point.")
            counter += 1  # Award point for each right answer
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {counter}/{num_times}")  # Print Final Score

if __name__ == "__main__":
    math_quiz()

