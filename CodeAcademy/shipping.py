from decimal import *

def input_validation(questiontext, validationRequired):
    while True:
        if (validationRequired == "Float"):
            try:
                answer = float(input(questiontext))
            except ValueError:
                print("Not a valid number! Try again.\n")
                continue
            else:
                return answer
                break

def main():
    getcontext().rounding = ROUND_HALF_UP
    weight = input_validation("What is the weight of the package? ","Float")

    #Dictionary of Shipping Costs
    shippingCosts = {'Ground Shipping': 
                        {'2 lb or less': {'Price per Pound': 1.50, 'Flat Charge': 20.00},
                        'Over 2 lb but less than or equal to 6 lb': {'Price per Pound': 3.00, 'Flat Charge': 20.00},
                        'Over 6 lb but less than or equal to 10 lb': {'Price per Pound': 4.00, 'Flat Charge': 20.00},
                        'Over 10 lb': {'Price per Pound': 4.75, 'Flat Charge': 20.00}
                        },
                    'Ground Shipping Premium': 
                        {'2 lb or less': {'Price per Pound': 0, 'Flat Charge': 125.00},
                        'Over 2 lb but less than or equal to 6 lb': {'Price per Pound': 0, 'Flat Charge': 125.00},
                        'Over 6 lb but less than or equal to 10 lb': {'Price per Pound': 0, 'Flat Charge': 125.00},
                        'Over 10 lb': {'Price per Pound': 0, 'Flat Charge': 125.00}
                        },
                    'Drone Shipping': 
                        {'2 lb or less': {'Price per Pound': 4.50, 'Flat Charge': 0},
                        'Over 2 lb but less than or equal to 6 lb': {'Price per Pound': 9.00, 'Flat Charge': 0},
                        'Over 6 lb but less than or equal to 10 lb': {'Price per Pound': 12.00, 'Flat Charge': 0},
                        'Over 10 lb': {'Price per Pound': 14.25, 'Flat Charge': 0}
                        }}

    if (weight <= 2) and (weight > 0):
        weightBracket = '2 lb or less'
    elif (weight > 2) and (weight <= 6):
        weightBracket = 'Over 2 lb but less than or equal to 6 lb'
    elif (weight > 6) and (weight <= 10):
        weightBracket = 'Over 6 lb but less than or equal to 10 lb'
    elif (weight > 10):
        weightBracket = 'Over 10 lb'
    else:
        weightBracket = 'Invalid weight'
    
    print(f"The cost to ship a {weight}lb package is:")

    for s_Type, s_Info in shippingCosts.items():
        shippingCost = Decimal(weight * shippingCosts[s_Type][weightBracket]['Price per Pound'] + shippingCosts[s_Type][weightBracket]['Flat Charge'])
        print(f"{s_Type}: ${shippingCost:.2f}")

if __name__ == "__main__":
    main()