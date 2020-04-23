products = []

while True:
	name = input('Please enter product name: ')
	if name == 'q':
		break
	price = input('Enter price: ')
	price = int(price)
	stock = input('Enter number of stock: ')
	stock = int(stock)
	# p = []
	# p.append(name)
	# p.append(price)
	# p.append(stock) # ->	p = [name, price, stock]

	products.append([name, price, stock])

print(products)

print(products[0][2])

for product in products:
	print(product[0], 'price: NT', product[1], 'remaining stock: ', product[2])

#write file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Product Name, Price(NTD), Stock\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + '\n')