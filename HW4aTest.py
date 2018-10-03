import unittest
from unittest import mock
from unittest.mock import MagicMock as Mock
from HW4a import gitHubAPI
from unittest.mock import patch
m = Mock()


class DummyObject(object):
    def __init__(self, content):
        self.content = content

class testHW4GitHub(unittest.TestCase):
    @patch('requests.get')
    def testInput(self, json):
        json_obj = json.loads(json)
        m.json.return_value = json_obj
        json_results_list = []
        results = [Mock(), Mock(), Mock()]
        json_results_list.append(json.loads('[{"name" : "Classify-Triangles"}. {"name": "Hello-World"}, {"name": "HW2a567"}, {"name": "HW4"}]'))
        json_results_list.append(json.loads('[ { "commit" : "1" }, { "commit" : "10" }, { "commit" : "2" }, { "commit" : "29" },  { "commit" : "19" } ]'))
        m.json.side_effect = results

    # def testInput1(self, injMock):
        # mockedResp = [0, 0, 0]
        # mockedResp[0] = DummyObject(b' [{"id": "147019757", "name": "Classify-Triangles"}, {"id": "146317000", "name": "Hello-World"}, {"id": "147615028", "name": "HW2a567"}, {"id": "150050014", "name": "HW4"}]')
        # mockedResp[1] = DummyObject(b'[{"author": "jrr"}, {"author": "jrr"}, {"author": "jrr"}]')
        # mockedResp[2] = DummyObject(b'[{"author": "jrr"}, {"author": "jrr"}]')
        # mockedRequests.side_effect = mockedResp
        # self.assertEqual(gitHubAPI("atorres98"), [('Classify-Triangles', 1), ('GitHubApi', 10), ('Hello-World', 2), ('HW2a567', 29), ('HW4', 7)])
    
    # def testUser1(self):
    #     self.assertEqual(gitHubAPI("atorres98"), [ ('Classify-Triangles', 1), ('GitHubApi567', 10), ('Hello-World', 2), ('HW2a567', 29), ('HW4', 6)])  
    
    # def testUser2(self):
    #     self.assertEqual(gitHubAPI("richkempinski"), [('hellogitworld', 30), ('helloworld', 2), ('Project1', 2), ('threads-of-life', 1)])



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False)

# old code
# import unittest
# from HW4a import gitHubAPI

# class testHW4GitHub(unittest.TestCase):
#     def testUser1(self):
#         self.assertEqual(gitHubAPI("atorres98"), [ ('Classify-Triangles', 1), ('Hello-World', 2), ('HW2a567', 29), ('HW4', 17)])  
    
#     def testUser2(self):
#         self.assertEqual(gitHubAPI("richkempinski"), [('hellogitworld', 30), ('helloworld', 2), ('Project1', 2), ('threads-of-life', 1)])

# if __name__ == '__main__':
#     print('Running unit tests')
#     unittest.main()
