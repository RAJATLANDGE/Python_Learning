from object_oriented_program_oop6.oop35_product_example import Product

NOT_PRESENT = {"status": "product not in database" }
database = []


class ProductCRUD:

    def create(self, product):
        database.append(product)

    def read(self):
        return database

    def read_one(self, pid):
        for product in database:
            if product.pid == pid:
                return product


    def update(self, pid, new_product):
        db_prod = self.read_one(pid)
        if db_prod:
            db_prod.pid = new_product.pid
            db_prod.product_name = new_product.product_name
            db_prod.manufacturer = new_product.manufacturer
            db_prod.cost = new_product.cost
            db_prod.quantity = new_product.quantity
            db_prod.category = new_product.category
            db_prod.warranty = new_product.warranty

        else:
            return NOT_PRESENT


    def delete(self, pid):
        db_prod = self.read_one(pid)
        if db_prod:
                database.remove(db_prod)
        else:
            return NOT_PRESENT



pc = ProductCRUD()
iron = Product(pid=1, pname="steam iron", mfg="Bajaj", price=1250, qty=10, categoary="electric")
bike = Product(pid=2, pname="Ninja", mfg="Kawasaki", price=150000, qty=15, categoary="Two wheeler")
cell_phone = Product(pid=3, pname="MotoG5", mfg="Motorola", price=10000, qty=20, categoary="electronic")
washing_powder = Product(pid=4, pname="Ariel", mfg="Unilever", price=450, qty=50, categoary="cleaning")
pc.create(iron)
pc.create(bike)
pc.create(cell_phone)
pc.create(washing_powder)
print(database)
print(pc.read_one(1))
print(pc.read_one(2))
print(pc.read_one(3))
print(pc.read_one(4))
print(pc.read_one(5))

pc.delete(4)
print(pc.delete(10))
print(database)

temp_product = Product(pid=2, pname="Z900", mfg="Kawasaki", price=200000, qty=20, categoary="Two wheeler")

print(pc.read_one(2))
pc.update(2, temp_product)
print(pc.update(8, temp_product))
print(pc.read_one(2))

