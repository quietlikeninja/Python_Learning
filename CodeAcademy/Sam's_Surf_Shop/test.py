import surfshop
import unittest
import datetime

class TestSurfShop(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()
    
    def test_add_surfboard(self):
        self.assertEqual(self.cart.add_surfboards(1),'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                self.assertEqual(self.cart.add_surfboards(i),f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    # def test_add_surfboard_2(self):
    #     self.assertEqual(self.cart.add_surfboards(2),'Successfully added 2 surfboards to cart!')

    #@unittest.skip
    def test_add_too_many_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError,self.cart.add_surfboards, 5)

    def test_invalid_checkout_date(self):
        self.assertRaises(surfshop.CheckoutDateError,self.cart.set_checkout_date, datetime.datetime.now())

    #@unittest.expectedFailure
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

unittest.main()
