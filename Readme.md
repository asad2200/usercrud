# User CRUD Project

## Steps to run project :

1. open project folder in terminal
2. create virtual env
    ` virtualenv -p python3 venv `
3. Run virtualenv `source venv/bin/activate`
4. Install requirements `pip install -r requirements.txt`
5. Run server `python manage.py runserver`

Web - http://127.0.0.1:8000/  <br />
Api - http://127.0.0.1:8000/api/  <br />
    List All user           - (GET)   http://127.0.0.1:8000/api/  <br />
    Single User             - (GET)   http://127.0.0.1:8000/api/1/  <br />
    Create User             - (POST)  http://127.0.0.1:8000/api/  <br />
    Update User             - (PUT)   http://127.0.0.1:8000/api/1/  <br />
    Update User(Partialy)   - (PATCH) http://127.0.0.1:8000/api/1/ <br />

    Note: Browser support is enabled.

## Apartment:
- WEB:
    - Apartment List - http://127.0.0.1:8000/apartment/
    - Apartment Review (Add/View) - http://127.0.0.1:8000/apartment/review/<apartment_id>

- Api:(Attached Postman Collection)
    - View User Review - GET http://127.0.0.1:8000/api-apartment/review/2
    - Add User Review  - POST http://127.0.0.1:8000/api-apartment/review/2






