def is_valid_currency(currency):
   
    return len(currency) == 3 and currency.isalpha() and currency.isupper()
