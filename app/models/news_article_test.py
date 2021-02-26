import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("nbd_news","Sahil Kapur, Leigh Ann Caldwell","Senate ruling says Democrats can't put $15 minimum wage in Covid relief bill - NBC News","Senate ruling deals severe blow to minimum wage hike in Covid relief package", "https://www.cnn.com/2021/02/25/politics/mitch-mcconnell-donald-trump-2024/index.html", "https://cdn.cnn.com/cnnnext/dam/assets/210202094920-01-mitch-mcconnell-0126-super-tease.jpg", "2021-02-26T01:54:00Z", "(CNN)Senate Minority Leader Mitch McConnell said Thursday he would \"absolutely\" support former President Donald Trump if he became the GOP presidential nominee in 2024, a notable commitment following… [+2467 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__ == '__main__':