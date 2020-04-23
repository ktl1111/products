import os

# 讀取檔案
products = []   
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('yeah! file found!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'Product Name' in line:
				continue
			name, price, stock= line.strip().split(',') #.strip()把尾巴的換行符號\n去掉，再用.split(',')來用逗點做分割
			products.append([name, price, stock])
	print(products)
else:
	print('file not found...')

#讓使用者輸入
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

# 印出所有購買紀錄
for product in products:
	print(product[0], 'price: NT', product[1], 'remaining stock: ', product[2])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Product Name, Price(NTD), Stock\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + '\n')