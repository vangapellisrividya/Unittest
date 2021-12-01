'''
@Date:  2021-11-28	
@Author:Srividya
@Title : test_Userlogin

'''

import unittest
from user_login import firstname,lastname,email,phonenumber,password

class TestCaseUser(unittest.TestCase):

    def test_username1(self):
        """"
        Description: this function will test the firstname
        Parameter: self
        Return: None
        """
        firstname = 'Srividya'
        self.assertEqual(firstname,'Srividya')

    
    def test_username2(self):
        """"
        Description: this function will test the lasstname
        Parameter: self
        Return: None
        """
        lastname = 'Vangapelli'
        self.assertEqual(lastname,'Vangapelli')

    def test_Email(self):
        """"
        Description: this function will test the E-mail
        Parameter: self
        Return: None
        """
        email = 'vangapellisreevidya@gmail.com'
        self.assertEqual(email, 'vangapellisreevidya@gmail.com')

    def test_PhoneNumber(self):
        """"
        Description: this function will test the password
        Parameter: self
        Return: None
        """
        phonenumber = '917036653770'
        self.assertEqual(phonenumber,'917036653770')

    def test_Password(self):
        """"
        Description: this function will test the phonenumber
        Parameter: self
        Return: None
        """
        password = 'Sri@123'
        self.assertEqual(password, 'Sri@123')

    def test_values1(self):
        """"
        Description: this function will test the firstname
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError,firstname(123),123)
    def test_values2(self):
        """"
        Description: this function will test the lasstname
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError,lastname(123),123)
        
    def test_values3(self):
        """"
        Description: this function will test the email
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError,email('vidygmail.com'),'vidygmail.com')
            
    def test_values4(self):
        """"
        Description: this function will test the phonenumber
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError,phonenumber('helo'),'helo')
    def test_values5(self):
        """"
        Description: this function will test the password
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError ,password('vidya123'),'vidya123')

if __name__=='__main__':
    unittest.main()