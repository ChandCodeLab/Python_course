
'''
if applicant has high income AND good cerdit 
 Eligible for loan 
 '''
 
has_high_income = False
has_good_credit = False

if has_high_income and has_good_credit:
    print('Eligible for loan') 
else:
    print('Not eligible for loan')

# OR operators

if has_high_income or has_good_credit:
    print('Eligible for loan') 
else:
    print('Not eligible for loan')

# NOT operator

'''
if applicant has good credit AND doesn't have a criminal record
eligible for loan 
'''

has_good_cr = True
has_criminal_record = True

if has_good_cr and not has_criminal_record:
    print("Eligible for loan")    

else:
    print("Not eligible for loan")