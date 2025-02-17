def calculate_income_tax(gross_income, deductions):
    """
    Calculate the income tax based on the Indian tax slabs for FY 2025-26.

    Parameters:
    gross_income (float): The total annual income before deductions.
    deductions (float): The total amount of deductions applicable.

    Returns:
    float: The total tax liability.
    """
    # Define the tax slabs and corresponding rates
    tax_slabs = [
        (400000, 0.05),      # ₹4,00,001 to ₹8,00,000: 5%
        (400000, 0.10),      # ₹8,00,001 to ₹12,00,000: 10%
        (400000, 0.15),      # ₹12,00,001 to ₹16,00,000: 15%
        (400000, 0.20),      # ₹16,00,001 to ₹20,00,000: 20%
        (400000, 0.25),      # ₹20,00,001 to ₹24,00,000: 25%
        (float('inf'), 0.30) # Above ₹24,00,000: 30%
    ]

    # Standard deduction
    standard_deduction = 75000

    # Calculate net taxable income
    net_income = gross_income - standard_deduction - deductions

    # Initialize tax liability
    tax_liability = 0
    remaining_income = net_income

    # Calculate tax based on slabs
    for slab_amount, rate in tax_slabs:
        if remaining_income > slab_amount:
            tax_liability += slab_amount * rate
            remaining_income -= slab_amount
        else:
            tax_liability += remaining_income * rate
            break

    return tax_liability

# Main program
if __name__ == "__main__":
    try:
        gross_income = float(input("Enter your gross annual income (in ₹): "))
        deductions = float(input("Enter your total deductions (in ₹): "))
        tax = calculate_income_tax(gross_income, deductions)
        print(f"\nFor a gross income of ₹{gross_income:,.2f} and deductions of ₹{deductions:,.2f},")
        print(f"the total tax payable is ₹{tax:,.2f}.")
    except ValueError:
        print("Invalid input. Please enter numerical values for income and deductions.")
