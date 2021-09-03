import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv('.env')
# load_dotenv('.test.env')
from app import create_app
from models import setup_db, User, Binder

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
        self.database_name = "poketrack"
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
        res = self.client().post('/user/create', json={"name": "ash", "pokemongo_id": "12312555"}, headers=(get_headers(USER_TOKEN)))
        print(res)
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
    
    def patch_user_by_id(self):
        res = self.client().patch('/user/1', json={"name": "Likey likes to programmm", "pokemongo_id": "100000"}, headers=(get_headers(ADMIN_TOKEN)))

        
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated username'], 'Likey likes to programmm')
        # test case fails for data['updated pokemonGO id'] but updates and passes after running agian 
        self.assertEqual(data['updated pokemonGO id'], "100000")
    
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

    






    
    # def test_404_sent_if_users_is_none(self):
    #     # todo : create function that drops all users from db
    #     res = self.client().get('/user/')
    #     data = json.loads(res.data)


        
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')
    #     self.assertEqual(data['total users'], 0) 

    # def test_404_request_beyond_valid_page(self):
    #     response = self.client().get('/questions?page=1000')
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_delete_questions(self):
    #         res = self.client().delete('/questions/15')
    #         data = json.loads(res.data)

    #         question = Question.query.filter(Question.id == 15).one_or_none()
    #         self.assertEqual(res.status_code, 200)
    #         self.assertEqual(data['success'], True)
    #         self.assertEqual(data['deleted'], 15)
    #         # self.assertTrue(data['total_questions'])
    #         # self.assertTrue(len(data['questions']))
    #         self.assertEqual(question, None)

    # def search_question(self):
    #     res = self.client().post('questions/search', json={"searchTerm": "title"})
    #     data = json.loads(res.data)

    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['total_questions'])

    # def test_404_invalid_search(self):
    #     res = self.client().post('questions/search', json={"searchTerm": "beebop"})
    #     data = json.loads(res.data)

    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 404)
    #     self.assertEqual(data['message'], "resource not found")





    # def test_404_if_question_does_not_exist(self):
    #         res = self.client().delete('/questions/1000')
    #         data = json.loads(res.data)

    #         self.assertEqual(res.status_code, 422)
    #         self.assertEqual(data['success'], False)
    #         self.assertEqual(data['message'], 'unprocessable')


    # def test_get_category_questions(self):
    #     response = self.client().get('/categories/1/questions')
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(data['current_category'])

    # def test_404_get_category_questions(self):
    #     response = self.client().get('/categories/a/questions')
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "resource not found")

    # def test_get_quiz(self):
    #     quiz_round = {'previous_questions': [], 'quiz_category': {
    #         'type': 'Geography', 'id': 15}}
    #     response = self.client().post('/quizzes', json=quiz_round)
    #     data = json.loads(response.data)

        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_422_get_quiz(self):
    #     response = self.client().post('/quizzes', json={})
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()