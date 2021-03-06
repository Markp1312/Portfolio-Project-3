# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Mark_PC_Shop')


def Welcome_to_store():
    """
    This function is to collect the order information from the customer
    """
    
    products = SHEET.worksheet("orders").get_all_values()[0]
    
    print("Welcome to Mark's PC-SHOP, We currently have the following items in stock\n")
    for i in products:
        print(i)
    
    print("Please make your selection")
    
def Add_to_basket():

    """
    This function will collect the selected items from the customer and update the shopping basket accordingly
    """

    shopList = []
    maxLengthList = 6
    while len(shopList) < maxLengthList:
            item = input("Enter your Item to the List: ")
            shopList.append(item)
            print(shopList)
        return(shoplist)
        
def main ():

    """
    Run the program functions
    """

    Welcome_to_store()
    Add_to_basket()


main()
