# 1 standard imports                                                       #optimize import ctrl+alt+o
# 2 third party packages
# 3 local imports
import unittest
from datetime import datetime
# from object_oriented_program_oop--6.oop37_medicine_example.py import Medicine
from object_oriented_program_oop--6.oop37_medicine_example.py import Medicine
from object_oriented_program_oop--6.oop38_medicine_implement.py import Medicine, MedicineExpired


# @unittest.skip                    # to skip whole class
class TestMed(unittest.TestCase):
    
    def setUp(self) -> None:                          #it is executed before testcase
        self.mi = Medicine()
        crocin = Medicine(1, "crocin", "cipla", 5, datetime(2023, 3, 18), datetime(2020, 3, 18), 100)
        paracetamol = Medicine(2, "paracetamol", "mankind", 2, datetime(2022, 3, 19), datetime(2019, 3, 25), 200)
        self.mi.create(crocin)
        self.mi.create(paracetamol)
    
    def tearDown(self) -> None:                       #it is executed after testcase use for closing file,database connection close, etc
        print("testcase execution run successfully")

    def test_selll_medicine_positive(self):
       self.assertEqual(self.mi.sell_medicine(1,10),{"status": f"please pay amount 50"})

    def test_sell_medicine_qty_exhausted(self):
        self.assertEqual(self.mi.sell_medicine(1, 110), {"status": "sorry we don't have that qty"})

    @unittest.expectedFailure                 #if you know that there is failure happen in that test case then we use it and if it is fail but it show pass in console
    def test_sell_medicine_not_available(self):
        self.assertEqual(self.mi.sell_medicine(3, 25), {"status": "cNot Available"})

    @unittest.skip("Will be used in future")           #to skip the testcase
    def test_sell_medicine_expired(self):
        self.assertRaises((MedicineExpired), self.mi.sell_medicine,2,5)


if __name__ == '__main__':
    unittest.main()

# test discovery will search all folder, files and find all testcases and class which name start from test_,and it is run from command prompt.

























