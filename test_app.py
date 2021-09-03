import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
# load_dotenv('.env')
load_dotenv('.test.env')
from app import create_app
from models import setup_db, User, Binder
db = SQLAlchemy()

ADMIN_TOKEN = os.environ['ADMIN_TOKEN']
USER_TOKEN = os.environ['USER_TOKEN']
def get_headers(token):
    auth_header= {"Authorization": 'Bearer ' + (token)}
    return auth_header

class AppTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "poketrack_test"
        self.database_path = "postgresql://{}/{}".format('mike@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_all_users(self):
        res = self.client().get('/user/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['users'])
        self.assertTrue(data['total users']) 
    
    def create_new_user(self):
        res = self.client().post('/user/create', json={"name": "ffff", "pokemongo_id": "ffff"}, headers=(get_headers(ADMIN_TOKEN)))
                # res = self.client().post('/user/create', json={"name": "ffff","pokemongo_id": "ffff"}, headers={get_headers(ADMIN_TOKEN)})
        print(res)
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    
        
    def test_400_create_new_user(self):
        res = self.client().post('/user/create', json={"name": "", "pokemongo_id": ""}, headers=(get_headers(ADMIN_TOKEN)))
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], "Bad Request")



    def test_401_unauthorized_create_new_user(self):
        res = self.client().post('/user/create', json={"name": "ash", "pokemongo_id": "12312555"})
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], "Unauthorized")
    
    def get_user_by_id(self):
        res = self.client().get('/user/1', headers=(get_headers(ADMIN_TOKEN)))

        
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'], 1)
    
        
    def test_not_found_404_get_user_by_id(self):
        res = self.client().get('/user/2000', headers=(get_headers(ADMIN_TOKEN)))

        
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")
    
    def test_unauthorized_get_user_by_id(self):
        res = self.client().get('/user/1')

        
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unauthorized")
    
    def patch_user_by_id(self):
        res = self.client().patch('/user/1', json={"name": "Likey likes to program", "pokemongo_id": "100"}, headers=(get_headers(ADMIN_TOKEN)))

        
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated username'], 'Likey likes to program')
        # test case fails for data['updated pokemonGO id'] but updates and passes after running agian 
        self.assertEqual(data['updated pokemonGO id'], "100")
    

    def test_400_patch_user_by_id(self):
        res = self.client().patch('/user/1', json={"name": "", "pokemongo_id": ""}, headers=(get_headers(ADMIN_TOKEN)))

        
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')
        self.assertEqual(data['error'], 400)
    
    def test_404_patch_user_by_id(self):
        res = self.client().patch('/user/1000000', json={"name": "1111", "pokemongo_id": "111"}, headers=(get_headers(ADMIN_TOKEN)))

        
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['error'], 404)

    def test_401_patch_user_by_id(self):
        res = self.client().patch('/user/1')

        
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unauthorized")
    
    def add_card_to_binder(self):
        res = self.client().post('/binder/', json={"pokemon_id": "Base1-7", "user_id": "20"}, headers=(get_headers(USER_TOKEN)))

        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['pokemon added'], 'Base1-7')
        self.assertEqual(data['pokemon card added to user id'], '20')
    

    
    def test_400_add_card_to_binder(self):
        res = self.client().post('/binder/', json={"pokemon_id": "", "user_id": "20"}, headers=(get_headers(USER_TOKEN)))

        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')
        self.assertEqual(data['error'], 400)
    
    def test_401_add_card_to_binder(self):
        res = self.client().post('/binder/', json={"pokemon_id": "new user", "user_id": "20"})

        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unauthorized")

    

    def delete_card_from_binder(self):
        res = self.client().delete('/binder/', json={"pokemon_id": "base1-8", "user_id": "2"}, headers=(get_headers(USER_TOKEN)))

        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
    

    def test_400_delete_card_from_binder(self):
        res = self.client().delete('/binder/', json={"pokemon_id": "base1-8", "user_id": "2"}, headers=(get_headers(USER_TOKEN)))

        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')
        self.assertEqual(data['error'], 400)
    

    def test_401_delete_card_from_binder(self):
        res = self.client().delete('/binder/', json={"pokemon_id": "base1-8", "user_id": "2"})

        data = json.loads(res.data)
        


        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unauthorized")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()