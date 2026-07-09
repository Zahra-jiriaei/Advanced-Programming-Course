# Zahra Jiriaei 98300065

# import  libraries
import math as m
import datetime as dt
import csv
import unittest

class MedadRangi:
    '''
    Medad Rangi shop
    '''
    
    # Class attribute
    discount_rate=0.1
    Longitude=51.50185488303431
    latitude=35.74317403843504
    
    # For gathering all product, we could use __repr__ "magic function" too
    All_Product=[]
    
    # Instance attribute
    def __init__(self,name,price,quantity,country_name,company_name):
        '''
        This method is a magic method which define Instance attribute
        
        It needs 5 arguments name, price, quantity, country_name, company_name
        '''
        self.name=name
        self.price=price
        self.quantity=quantity
        self.country_name=country_name
        self.company_name=company_name
    
        MedadRangi.All_Product.append(self)
        
        if type(self.name)!=str:
            raise TypeError("It must be string!")
            
        if type(self.country_name)!=str:
            raise TypeError("It must be string!")
            
        if type(self.company_name)!=str:
            raise TypeError("It must be string!")
            
        if self.price<=0 :
            raise ValueError("Entered number must be greater than 0!")
            
        if self.quantity<=0:
            raise ValueError("Entered number must be greater than 0!")
            
            
    # Instance method
    def final_price(self):
        '''
        This function calculate final price for each product
        '''
        Final_Price=self.price*MedadRangi.discount_rate*self.quantity
        return Final_Price
    
    # Instance method
    def calculate_distance(self,destination_Longitude,destination_latitude):
        '''
        This function calculate distance between our shop and destination
        '''
        self.destination_Longitude=destination_Longitude
        self.destination_latitude=destination_latitude
        
        Longitude_distance= (self.destination_Longitude-MedadRangi.Longitude)**2
        latitude_distance= (self.destination_latitude-MedadRangi.latitude)**2
        
        Distance=m.sqrt(latitude_distance+Longitude_distance)
        
        return Distance
        
    # Instance method
    def welcome(self):
        '''
        This function say welcome to user each time
        '''
        now=dt.datetime.now()
        Hour=now.hour
        
        if Hour<12 and Hour>=6:
            return "Good morning"
        elif Hour<18 and Hour>=12:
            return "Good afternon"
        else:
            return "Good evening"
    
    # Class method
    @classmethod
    def load_csv(cls,csv_file_name):
        csv_file_name=str(csv_file_name)
        with open(csv_file_name, "r") as f:
            reader = csv.DictReader(f)
            product = list(reader)
        
        for Product in product:
            MedadRangi(
                name=Product.get("name"),
                price=Product.get("price"),
                quantity=Product.get("quantity"),
                country_name=Product.get("country_name"),
                company_name=Product.get("company_name"))

# UNITTEST

class TestMedadRangi(unittest.TestCase):
    
    def test_final_price(self):
        
        shop1=MedadRangi("medad",2000,100,"Iran","papco")
        self.assertAlmostEqual(shop1.final_price(),2000*100*0.1)
        shop2=MedadRangi("medad",1000,100,"Iran","papco")
        self.assertAlmostEqual(shop2.final_price(),1000*100*0.1)
        
    def test_calculate_distance(self):
        self.assertAlmostEqual(shop1.calculate_distance(-20,10),m.sqrt(((51.50185488303431+20)**2)+((35.74317403843504-10)**2)))
        self.assertAlmostEqual(shop2.calculate_distance(20,10),m.sqrt(((51.50185488303431-20)**2)+((35.74317403843504-10)**2)))

                               
if __name__ == "__main__":
    unittest.main()
    
