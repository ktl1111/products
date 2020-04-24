import os

# 讀取檔案
def read_file(filename):
	products = [] 
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'Product Name' in line:
				continue
			name, price, stock= line.strip().split(',') #.strip()把尾巴的換行符號\n去掉，再用.split(',')來用逗點做分割
			products.append([name, price, stock])
	return products 

#讓使用者輸入
def user_input(products):
	while True:
		name = input('Please enter product name: ')
		if name == 'q':
			break
		price = input('Enter price: ')
		price = int(price)
		stock = input('Enter number of stock: ')
		stock = int(stock)
		products.append([name, price, stock])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0], 'price: NT', product[1], 'remaining stock: ', product[2])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Product Name, Price(NTD), Stock\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('yeah! file found!')
		products = read_file(filename)
	else:
		print('file not found...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


#執行程式 
main()