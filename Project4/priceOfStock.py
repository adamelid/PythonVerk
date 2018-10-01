again = True

def prompt_user():
    while True:
        try:
            shares = int(input("Enter number of shares: "))
            break
        except ValueError:
            print("Invalid number!")
    while True:
        try:
            userinput = input("Enter price (dollars, numerator, denominator): ")
            dollars, numerator, denominator = userinput.split()
            dollars = int(dollars)
            numerator = int(numerator)
            denominator = int(denominator)
            break
        except ValueError:
            print("Invalid price!")
    return shares, dollars, numerator, denominator

def run_again():
    userinput = input("Continue: ")
    if userinput.lower() == 'y':
        return True
    else:
        return False


def calculate_price(shares, dollars, numerator, denominator):
    
    price = (dollars + (numerator/denominator)) * shares

    print("{} shares with market price {} {}/{} have value ${:.2f}".format(shares, dollars, numerator, denominator, price))


while again:
    shares, dollars, numerator, denominator = prompt_user()
    calculate_price(shares, dollars, numerator, denominator)
    again = run_again()