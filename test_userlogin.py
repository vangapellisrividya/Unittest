'''
@Date:  2021-11-21	
@Author:Srividya
@Title : test_Userlogin

'''

import unittest
from user_login import firstname, lastname, email, password, phonenumber

class TestCaseUser(unittest.TestCase):

    def test_username1(self):
        """"
        Description: this function will test the firstname
        Parameter: self
        Return: None
        """
        Firstname = firstname('Srividya')
        self.assertEqual(Firstname, 'Srividya')
    def test_username2(self):
        """"
        Description: this function will test the lasstname
        Parameter: self
        Return: None
        """
        Lastname = lastname('Vangapelli')
        self.assertEqual(Lastname,'Vangapelli')
    def test_Email(self):
        """"
        Description: this function will test the E-mail
        Parameter: self
        Return: None
        """
        Email = email('vangapellisreevidya@gmail.com')
        self.assertEqual(Email, 'vangapellisreevidya@gmail.com')

    def test_PhoneNumber(self):
        """"
        Description: this function will test the password
        Parameter: self
        Return: None
        """
        PhoneNumber = phonenumber('917036653770')
        self.assertEqual(PhoneNumber, '917036653770')

    def test_Password(self):
        """"
        Description: this function will test the phonenumber
        Parameter: self
        Return: None
        """
        Password = password('Sri@123')
        self.assertEqual(Password, 'Sri@123')

if __name__=='__main__':
    unittest.main()