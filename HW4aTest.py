import unittest
from HW4a import gitHubAPI

class testHW4GitHub(unittest.TestCase):
    def testUser1(self):
        self.assertEqual(gitHubAPI("atorres98"), [ ('Classify-Triangles', 1), ('Hello-World', 2), ('HW2a567', 29), ('HW4', 21)])  
    
    def testUser2(self):
        self.assertEqual(gitHubAPI("richkempinski"), [('hellogitworld', 30), ('helloworld', 2), ('Project1', 2), ('threads-of-life', 1)])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
