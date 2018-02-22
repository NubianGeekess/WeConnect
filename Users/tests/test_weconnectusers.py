# WeConnect/tests/test_weconnectusers.py
#This script tests the functionality of User class

# third party imports
from unittest import TestCase

# local imports
from app.models.weconnect import WeConnect
from app.models.user import User


class WeConnectTestCase(TestCase):
    #Test user registration and login

    def setUp(self):
        self.weconnect = WeConnect()
        self.users = self.weconnect.users
        self.user = User("ivan", "safari", "ivansafari", "password to hash one")
        self.a_user = User("colla", "ann", "collaann", "password to hash two")

    def test_weconnect_instance(self):
        #Test if WeConnect instance is created

        self.assertIsInstance(self.weconnect, WeConnect,
                              msg="Object should be an instance of WeConnect!")

    def test_user_registration(self):
        #Test user registration

        user = self.weconnect.register(self.user)

        self.assertTrue(user, msg="User not created!")

    def test_user_already_exists(self):
        #Test if username already exists

        self.weconnect.register(self.user)
        a_user = self.weconnect.register(self.a_user)

        self.assertFalse(a_user, msg="Username not yet taken!")

    def test_user_login(self):
        #Test user login

        self.weconnect.register(self.user)

        user_instance = self.weconnect.login("ivansafari", "password to hash one")
        wrong_password = self.weconnect.login("ivansafari", "wrong password")
        wrong_username = self.weconnect.login("doris", "password to hash one")

        self.assertEqual(user_instance.username, "ivansafari",
                         msg="Login failed!")
        self.assertEqual(
            wrong_password, "Incorrect username and password combination!", msg="Login successful!")
        self.assertEqual(
            wrong_username, "This username does not exist! Please register!",
            msg="Login successful!")
