from fastapi.testclient import TestClient
from app.main import app # we need app for the test client

client = TestClient(app)

# define our test cases sucess 
def test_eligibility_pass():
    response = client.post('/loan-eligibility',json = {'income':60000, 'age' : 30, 'employment_status' : 'employed'})
# earlier we defined payload seperately and if required we can do 
# for now i will write directly 
# instead of writing it seperately we have written inside post which is also normal
    assert response.status_code == 200
    assert response.json() == {'eligible': True}

# define our 2nd test cases fail
def test_eligibility_fail():
    response = client.post('/loan-eligibility',json = {'income':30000, 'age' : 18, 'employment_status' : 'unemployed'})
# earlier we defined payload seperately and if required we can do 
# for now i will write directly 
# instead of writing it seperately we have written inside post which is also normal
    assert response.status_code == 200
    assert response.json() == {'eligible': False}
