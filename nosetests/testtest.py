import unittest

from selenium import webdriver
from xvfbwrapper import Xvfb


class TestPages(unittest.TestCase):

    def setUp(self):
        self.xvfb = Xvfb(width=1280, height=720)
        self.addCleanup(self.xvfb.stop)
        self.xvfb.start()
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testCastHTML_to_png(self):
        self.browser.get('file:///home/ntak/Documents/mcgill/comp767/assignment5/little-network-toolkit/examples/network_example.html')
        b64 = self.browser.execute_script('cy=document.getElementById("cy");cy.png()')
        print(b64)

        self.assertIn('Ubuntu', self.browser.title)

    def testUbuntuHomepage(self):
        self.browser.get('http://www.ubuntu.com')
        self.assertIn('Ubuntu', self.browser.title)

    def testGoogleHomepage(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    unittest.main()