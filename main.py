
from fundemental_module import calculate_fundamental_scores
from valuation_module import calculate_valuation_scores

#loop that make sure its float and system wont crash
def get_float_correct_input(prompt):

    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. PLS try again ")


#asking user for fundamentals inputs: (in the future API)
growth = get_float_correct_input("Enter stock Revenue Growth %: ")


