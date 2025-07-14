KPA API Assignment – FastAPI

Developed by: Parthasarathy

This project is a backend API assignment for Suvidhaen, developed using "FastAPI".  
It implements "two functional APIs" from the provided Postman collection:
-> "POST /login" – Authenticates user and returns JWT token
-> "GET /getformdata" – Returns protected form data using token

---

Tech Stack
-> Python 3.x
-> FastAPI
-> Pydantic
-> JWT (python-jose)
-> dotenv
-> Uvicorn (ASGI server)
-> Postman (for testing)

---

Folder Structure

├── app/
│ ├── main.py
│ ├── auth.py
│ ├── routes.py
│ ├── schemas.py
│ └── utils.py
├── .env
├── requirements.txt
└── README.md

2. Install Dependencies

-> pip install -r requirements.txt

3. Create .env File

JWT_SECRET_KEY=secret123
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

4. Run the Server

uvicorn app.main:app --reload
