products = []

while True:
	name = input('Please enter product name: ')
	if name == 'q':
		break
	price = input('Enter price: ')
	stock = input('Enter number of stock: ')
	# p = []
	# p.append(name)
	# p.append(price)
	# p.append(stock) # ->	p = [name, price, stock]

	products.append([name, price, stock])

print(products)

print(products[0][2])

for product in products:
	print(product[0], 'price: NT', product[1], 'remaining stock: ', product[2])