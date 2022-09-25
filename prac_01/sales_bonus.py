"""
1.
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# sales = float(input("Enter sales: $"))
# if sales < 1000:
#     small_bonus = sales * 0.1
#     print(f"result: {small_bonus:.1f}")
# else:
#     big_bonus = sales * 0.15
#     print(big_bonus)


"""
Second part
"""
total_bonus = 0
sales = float(input("Enter sales: $"))
while sales >= 0:  # while sales is less than 0
    if sales < 1000:
        total_bonus = sales * 0.1
        print(total_bonus)
        sales = float(input("Enter sales: $"))
    else:
        big_bonus = sales * 0.15
        print(big_bonus)
        sales = float(input("Enter sales: $"))




