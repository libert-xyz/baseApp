import unittest
#from flask.ext.testing import TestCase
from crud import app,db
from crud.models import Messages
import json

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass


    def test_index(self):
        response = self.app.get('/',content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_render(self):
        response = self.app.get('/',content_type='html/text')
        self.assertIn(b'Sample app for testing Web Services', response.data)


    def post_message(self,nick,text):
        return self.app.post(
            '/api',
            #data=dict(nick=nick,text=text),
            data=json.dumps(dict(nick=nick,text=text)),
            content_type='application/json')

    def test_message_post(self):
        response = self.post_message('Libert','Just Like you Imagined')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Just Like you Imagined',response.data)

        # response2 = self.app.get('/',content_type='html/text')
        # self.assertIn(b'Just Like you Imagined', response2.data)

    def test_message_get(self):
        self.post_message('Libert','Just Like you Imagined')
        response = self.app.get('/api',content_type='application/json')
        self.assertIn(b'Just Like you Imagined', response.data)



if __name__ == '__main__':
    unittest.main()
