name = input('What is the name of the customer? ')
address = input('What is the address of the customer? ')
length = eval(input('What is the length of the room (in feet)? '))
width = eval(input('What is the width of the room (in feet)?'))
area = length*width
flooring = (2)
installation = (1.5)
print('Estimate for', name)
print('Address:', address)
print('Circle room with an area of', area, 'square feet.')
print('Estimated cost for flooring is ','$',flooring*area,'.', sep='')
print('Estimated cost for installation is ', '$',  installation*area,'.', sep='')
flooringcost= flooring*area
installationcost= installation*area
print('Total estimate is ','$', flooringcost+installationcost,'.', sep='')
print('Thank you for your business!')
