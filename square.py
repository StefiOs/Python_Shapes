name = input('What is the name of the customer? ')
address = input('What is the address of the customer? ')
size = eval(input('What is the size of 1 side of the room (in feet)? '))
area = size**2
flooring = (2)
installation = (1.5)
print('The estimate for', name)
print(address)
print('Square room with an area of', area, 'square feet.')
print('Estimated cost for flooring is ','$',flooring*area,'.', sep='')
print('Estimated cost for installation is ', '$',  installation*area,'.', sep='')
flooringcost= flooring*area
installationcost= installation*area
print('Total estimate is','$', flooringcost+installationcost)
print('Thank you for your business!')

