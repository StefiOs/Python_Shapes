name = input('What is the name of the customer? ')
address = input('What is the address of the customer? ')
size = eval(input('What is the radius of the room (in feet)? '))
pi = 3.14
area = size**2*pi
flooring = (2.0)
installation = (1.5)
print('Estimate for', name)
print(address)
print('Circle room with an area of', area, 'square feet.')
print('Estimated cost for flooring is ','$',flooring*area,'.', sep='')
print('Estimated cost for installation is ', '$',  installation*area,'.', sep='')
flooringcost= flooring*area
installationcost= installation*area
print('Total estimate is ','$', flooringcost+installationcost,'.', sep='' )
print('Thank you for your business!')

