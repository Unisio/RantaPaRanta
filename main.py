##

print('Hur många år kommer du att spara?')
years = int(input('Ange år : '))

print('Hur mycket har du sparat nu?')
principal = float(input('Ange hur mycket sparandet är nu : '))

print('Hur mycket kommer du att månadsspara?')
monthly_invest = float(input('Ange summa: '))

print('Vilken årlig ränta vill du räkna på?')
interest = float(input('Ange procent i decimalform : '))

print('')

monthly_invest = monthly_invest * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

final_amount = (final_amount + monthly_invest) * (1 + interest)

print('Slutgiltigt sparande efter {} år:'.format(years) + str(final_amount))
