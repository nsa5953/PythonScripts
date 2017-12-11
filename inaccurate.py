#Python Script for Calculating Decimals
from decimal import *

item = 0.70
rate = 1.05
tax = item * rate
total = item + tax

print('Item:\t', '%.2f' % item)
print('Tax:\t', '%.2f' % tax)
print('Total:\t', '%.2f' % total)

# Expand Variable to 20 places by %.20f
print('Iteam:\t', '%.20f' % item)
print('Tax:\t', '%.20f' % tax)
print('Total:\t', '%.20f' % total)

# Add Decimal() to show accurate results
items = Decimal(0.70)
rates = Decimal(1.05)
taxs = items * rates
totals = items + taxs
print('Items:\t', '%.2f' % items)
print('Taxs:\t', '%.2f' % taxs)
print('Totals:\t', '%.2f' % totals)

# Note: Use Decimal() object to calculate monetery Values or anywhare that accuracy is essensial
