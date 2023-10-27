from bs4 import BeautifulSoup
import requests
import unittest

def get_emblem(soup):
    """
    Task 2: Get the source path (src) to the image for the University of Michigan's emblem.
    """
    # YOUR CODE HERE
    pass 



def get_school_rankings(soup):
    """
    Task 3: Get the details of the table named “USNWR Global Program Rankings” in the University of Michigan Wikipedia page. 
    
    Get all of the programs and the ranking and organize the information into key-value pairs in a dictionary
    
    Use the structure: 
    {'Program': Ranking}

    Be sure to convert the ranking to an integer.
    """
    # YOUR CODE HERE
    pass



def main():
    # Task 1: Create a BeautifulSoup object. 

    # YOUR CODE HERE

    # Task 4: sort the dictionary by rank to see what the 3 highest ranked programs are at the University of Michigan 
    pass

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/University_of_Michigan').text, 'html.parser')

    def test_get_link(self):
        self.assertEqual(get_emblem(self.soup), '//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Seal_of_the_University_of_Michigan.svg/150px-Seal_of_the_University_of_Michigan.svg.png')

    def test_get_school_founded_year(self):
        self.assertEqual(get_school_rankings(self.soup)['Social Sciences & Public Health'], 6)

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)