accountA = {
    'name': 'Yavuzhan Namlı',
    'accountNO': '1234567890',
    'balance': 3000,
    'additionalBalance': 2000
}


def withdrawMoney(account, amount):
    print(f'Hello {account["name"]}')

    if (account['balance'] >= amount):
        account['balance'] -= amount
        print('You can get your money.')
    else:
        totalBalance = account['balance'] + account['additionalBalance']

        if (totalBalance >= amount):
            additionalBalanceUse = input('Do you want to use the additional balance? (Yes/No)')

            if additionalBalanceUse == 'Yes':
                amountToUseAdditionalBalance = amount - account['balance']
                account['balance'] = 0
                account['additionalBalance'] -= amountToUseAdditionalBalance
                print('You can get your money.')
            else:
                print(f"There is a balance of {account['balance']}$ in your account numbered {account['accountNO']}.")
        else:
            print('Your balance is insufficient.')
def balanceInquiry(balance):
            print(f"There is a balance of {accountA['balance']}$ in your account numbered {accountA['accountNO']}. Your additional balance limit is {accountA['additionalBalance']}$")

withdrawMoney(accountA, 2000)
balanceInquiry(accountA)

print('*****************')
withdrawMoney(accountA, 2000)
balanceInquiry(accountA)
