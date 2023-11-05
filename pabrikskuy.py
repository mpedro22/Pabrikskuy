from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel


class User(BaseModel):
	iduser: int
	nama: str
	alamat: str
	email: str
	NoTelp: str
	Password: str
	
class Item(BaseModel):
	iditem: int
	nama: str
	kategori: str
	harga: int
	jumlah: int

class Order(BaseModel):
	idorder: int
	iduser: int
	iditem: int
	tanggalpesan: str
	statuspesan: str

json_filename="menu.json"

with open(json_filename,"r") as read_file:
	data = json.load(read_file)

app = FastAPI()

# Get
@app.get('/user')
async def read_all_user():
	return data['user']

@app.get('/order')
async def read_all_order():
	return data['order']

@app.get('/item')
async def read_all_item():
	return data['item']



@app.get('/user/{user_id}')
async def read_user(user_id: int):
	for user in data['user']:
		print(user)
		if user['iduser'] == user_id:
			return user
	raise HTTPException(
		status_code=404, detail=f'user not found'
	)

@app.get('/item/{item_id}')
async def read_item(item_id: int):
	for item in data['item']:
		print(item)
		if item['iditem'] == item_id:
			return item
	raise HTTPException(
		status_code=404, detail=f'item not found'
	)

@app.get('/order/{order_id}')
async def read_order(order_id: int):
	for order in data['order']:
		print(order)
		if order['idorder'] == order_id:
			return order
	raise HTTPException(
		status_code=404, detail=f'order not found'
	)

@app.post('/user')
async def add_user(user: User):
	user_dict = user.dict()
	user_found = False
	for user in data['user']:
		if user['iduser'] == user_dict['iduser']:
			user_found = True
			return "user ID "+str(user_dict['iduser'])+" exists."
	
	if not user_found:
		data['user'].append(user_dict)
		with open(json_filename,"w") as write_file:
			json.dump(data, write_file, indent=4)

		return user_dict
	raise HTTPException(
		status_code=404, detail=f'user not found'
	)

@app.post('/item')
async def add_item(item: Item):
	item_dict = item.dict()
	item_found = False
	for item in data['item']:
		if item['iditem'] == item_dict['iditem']:
			item_found = True
			return "item ID "+str(item_dict['iditem'])+" exists."
	
	if not item_found:
		data['item'].append(item_dict)
		with open(json_filename,"w") as write_file:
			json.dump(data, write_file, indent=4)

		return item_dict
	raise HTTPException(
		status_code=404, detail=f'item not found'
	)

@app.post('/order')
async def add_order(order: Order):
	order_dict = order.dict()
	order_found = False
	for order in data['order']:
		if order['idorder'] == order_dict['idorder']:
			order_found = True
			return "order ID "+str(order_dict['idorder'])+" exists."
	
	if not order_found:
		data['order'].append(order_dict)
		with open(json_filename,"w") as write_file:
			json.dump(data, write_file, indent=4)

		return order_dict
	raise HTTPException(
		status_code=404, detail=f'order not found'
	)

@app.put('/user')
async def update_user(user: User):
	user_dict = user.dict()
	user_found = False
	for user_idx, user in enumerate(data['user']):
		if user['id'] == user_dict['id']:
			user_found = True
			data['user'][user_idx]=user_dict
			
			with open(json_filename,"w") as write_file:
				json.dump(data, write_file)
			return "updated"
	
	if not user_found:
		return "User ID not found."
	raise HTTPException(
		status_code=404, detail=f'user not found'
	)

@app.put('/item')
async def update_item(item: Item):
	item_dict = item.dict()
	item_found = False
	for item_idx, item in enumerate(data['item']):
		if item['id'] == item_dict['id']:
			item_found = True
			data['item'][item_idx]=item_dict
			
			with open(json_filename,"w") as write_file:
				json.dump(data, write_file)
			return "updated"
	
	if not item_found:
		return "Item ID not found."
	raise HTTPException(
		status_code=404, detail=f'item not found'
	)

@app.put('/order')
async def update_order(order: Order):
	order_dict = order.dict()
	order_found = False
	for order_idx, order in enumerate(data['order']):
		if order['id'] == order_dict['id']:
			order_found = True
			data['order'][order_idx]=order_dict
			
			with open(json_filename,"w") as write_file:
				json.dump(data, write_file)
			return "updated"
	
	if not order_found:
		return "Order ID not found."
	raise HTTPException(
		status_code=404, detail=f'order not found'
	)

@app.delete('/user/{iduser}')
async def delete_user(iduser: int):

	user_found = False
	for iduserx, user in enumerate(data['user']):
		if user['iduser'] == iduser:
			user_found = True
			data['user'].pop(iduserx)
			
			with open(json_filename,"w") as write_file:
				json.dump(data, write_file, indent=4)
			return "updated"
	
	if not user_found:
		return "user ID not found."
	raise HTTPException(
		status_code=404, detail=f'user not found'
	)
