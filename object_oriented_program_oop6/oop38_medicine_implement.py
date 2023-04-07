from object_oriented_program_oop6.oop37_medicine_example import Medicine
from datetime import datetime
from datetime import timedelta

class MedicineExpired(Exception):
    pass


NOT_PRESENT = {"status": "product not in database" }



class MedicineImpl:
    database = []

    def read(self):
        return MedicineImpl.database

    def read_one(self, mid):
        for medicine in MedicineImpl.database:
            if medicine.mid == mid:
                return medicine

    def create(self, medicine):
        MedicineImpl.database.append(medicine)

    def delete(self, mid):
        db_med = self.read_one(mid)
        if db_med:
            MedicineImpl.database.remove(db_med)
        else:
            return NOT_PRESENT

    def update(self, mid, medicine):
        db_med = self.read_one(mid)
        if db_med:
            db_med.mid = medicine.mid
            db_med.name = medicine.name
            db_med.manufacturer = medicine.manufacturer
            db_med.price = medicine.price
            db_med.exp_date = medicine.exp_date
            db_med.mfg_date = medicine.mfg_date
            db_med.qty = medicine.qty
        else:
            return NOT_PRESENT


    def sell_medicine(self, mid : int, qty: int) ->  dict:              #this is type hint
        """

        :param mid: id of the  medicine unique id
        :param qty:quantity for purchase
        :return:
        """
        db_med = self.read_one(mid)
        if db_med:
            current_date = datetime.now()
            if db_med.exp_date > current_date:
                if db_med.qty >= qty:
                    total = qty * db_med.price
                    db_med.qty = db_med.qty - qty
                    return {"status": f"please pay amount {total}"}
                else:
                    return {"status": "sorry we don't have that qty"}
            else:
                raise MedicineExpired("Medicine is expired ", db_med.name, db_med.exp_date)
        else:
            return {"status": "Not Available"}

    def stock_check(self,mid):
        db_med = self.read_one(mid)
        current_date = datetime.now()
        delta = timedelta(days = 30)
        low_medicine = []
        expire_medicine = []
        d30_exp = []

        if db_med.qty < 5:
            low_medicine.append(db_med.name)

        if db_med.exp_date < current_date:
            expire_medicine.append(db_med.name)

        if db_med.exp_date - current_date < delta:
            d30_exp.append(db_med.name)







mi = MedicineImpl()

crocin = Medicine(1, "crocin", "cipla", 5, datetime(2023,3,18), datetime(2020,3,18), 100)
paracetamol = Medicine(2, "paracetamol", "mankind", 2, datetime(2024,3, 19), datetime(2019,3,25), 200)
paracetamol_update = Medicine(2, "paracetamol", "mankind", 5, datetime(2025,3, 20), datetime(2019,3,25), 100)

dolo = Medicine(3, "Dolo", "lupin", 7, datetime(2025,3, 18), datetime(2020,3,25), 25)
Lomotil = Medicine(4, "Lomotil", "Sun Pharma", 8, datetime(2025,4, 18), datetime(2020,4,25), 5)
Florastor = Medicine(5, "Florastor", "Dr.Reddy", 9, datetime(2025,5, 18), datetime(2020,5,25), 35)
Diamode = Medicine(6, "Diamode", "Divis", 10, datetime(2022,3, 18), datetime(2020,6,25), 40)
Opium = Medicine(7, "Opium", "Aurobindo", 11, datetime(2022,4, 18), datetime(2020,7,25), 45)
Mystesi = Medicine(8, "Mystesi", "Torrent", 12, datetime(2025,8, 18), datetime(2020,8,25), 50)
Motofen = Medicine(9, "Motofen", "Zydus", 13, datetime(2025,9, 18), datetime(2020,9,25), 55)
Oralyte = Medicine(10, "Oralyte", "Abbott", 14, datetime(2025,10, 18), datetime(2020,10,25), 60)
ReVital = Medicine(11, "ReVital", "Alkem", 15, datetime(2025,11, 18), datetime(2020,11,25), 65)
Ceralyte = Medicine(12, "Ceralyte", "Biogen", 16, datetime(2025,12, 18), datetime(2020,12,25), 70)

mi.create(dolo)
mi.create(Lomotil)
mi.create(Florastor)
mi.create(Diamode)
mi.create(Opium)
mi.create(Mystesi)
mi.create(Motofen)
mi.create(Oralyte)
mi.create(ReVital)
mi.create(Ceralyte)

mi.create(crocin)
mi.create(paracetamol)
# print(database)
# print(mi.read())
# print(mi.read_one(2))
mi.update(2,paracetamol_update)
# print(mi.read_one(2))
# mi.delete(1)
# print(mi.read())
# print(mi.delete(3))
print(mi.update(3,paracetamol_update))


# print(mi.sell_medicine(6,10))
print(mi.sell_medicine(2,10))

print(mi.sell_medicine(1,20))
print(mi.sell_medicine(1,80))
print(mi.sell_medicine(1,20))
print(mi.read_one(1))


print(mi.stock_check(1))
# print(mi.stock_check())
# print(mi.stock_check())
# print(mi.stock_check())
# print(mi.stock_check())

