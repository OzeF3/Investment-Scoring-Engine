
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


#asking user for fundamentals inputs: (in the future will be API)
revenue_growth = get_float_correct_input("Enter stock Revenue Growth %: ")
operating_margin = get_float_correct_input("Enter stock Operating margin %: ")
debt_to_equity = get_float_correct_input("Enter stock Debt to Equity ratio: ")
fcf_margin = get_float_correct_input("Enter stock Free Cash Flow Margin %: ")

#asking user for valuations inputs: (in the future will be API)

result_1 = calculate_fundamental_scores(revenue_growth,operating_margin,debt_to_equity,fcf_margin)
print(f"Score is: {result_1}")





