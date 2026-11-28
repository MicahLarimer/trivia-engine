def calculate_score(difficulty, correct):
    if not isinstance(difficulty, str):
        raise TypeError("Difficulty must be a string.")
    if not isinstance(correct, bool):
        raise TypeError("Correct must be a Boolean.")
    difficulty = difficulty.title()
    if difficulty not in ["Easy", "Medium", "Hard"]:
        raise ValueError("Invalid difficulty. Choose Easy, Medium, or Hard.")
    if correct and difficulty == "Easy":
        return 10
    elif correct and difficulty == "Medium":
        return 20
    elif correct and difficulty == "Hard":
        return 30
    else:
        return 0
    
print(calculate_score("easy", True))       # 10
print(calculate_score("MEDIUM", True))     # 20
print(calculate_score("Hard", True))       # 30
print(calculate_score("Easy", False))      # 0

try:
    calculate_score(10, True)
except TypeError as error:
    print(error)

try:
    calculate_score("Impossible", True)
except ValueError as error:
    print(error)

try:
    calculate_score("Easy", "yes")
except TypeError as error:
    print(error)
