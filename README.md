## Task Management App

## Setting Up The Environment
To set up the environment, follow these steps:

- Clone the repository and install dependencies using pip: pip install -r requirements.txt
- Create a .env file and put your variables in it
- Run migrations to set up the database: python manage.py migrate
- Start the development server: python manage.py runserver
  # or
- docker-compose build
- docker-compose up
  
# Testing
The application includes test cases for SMS sending and listing: 
   - python manage.py test api.tests.CreateSmsTest
   - python manage.py test api.tests.ListSmsTest 


# API Endpoints
Here are some examples of API endpoints available in the application:

- GET /api/: Retrieves a list of all sent sms
- POST /api/: Send a sms 
    "body": {
					"sender"(optional): "30000000000000",
					"receptor"(require): "09123456789",
					"text"(require): "SMS MESSAGE",
          "provider"(optional): "smsir(default) or qasedak"
				}

# Background Processing
The application uses Celery to handle background processing of sending sms, it'll be added to a queue and processed asynchronously.
- In another terminal run this command -> celery -A sms_gateway.celery worker --loglevel=info
  or if you using docker-compose just check the main terminal on celery container logs
