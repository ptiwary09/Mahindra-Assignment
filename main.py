def accounts_below_threshold(accounts, threshold):
    below_threshold = [account for account in accounts if account['balance'] < threshold]
    return below_threshold

# Function to take user input for bank accounts
def get_bank_accounts():
    accounts = []
    num_accounts = int(input("Enter the number of bank accounts: "))
    
    for _ in range(num_accounts):
        name = input("Enter account holder's name: ")
        balance = float(input(f"Enter balance for {name}: "))
        accounts.append({'name': name, 'balance': balance})
        
    return accounts

# Take threshold value from user
threshold = float(input("Enter the threshold balance: "))

# Take bank account details from the user
accounts = get_bank_accounts()

# Call the function to find accounts below the threshold
accounts_below = accounts_below_threshold(accounts, threshold)

# Output the result
print(f"Accounts with balance below Rs {threshold}:")
if accounts_below:
    for account in accounts_below:
        print(f"{account['name']}: rs {account['balance']}")
else:
    print("No accounts found below the specified threshold.")
