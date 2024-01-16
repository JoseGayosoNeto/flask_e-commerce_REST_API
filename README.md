# Flask E-commerce

E-commerce Flask API Project.

## Description

This project is a simple e-commerce API developed using Flask. It provides functionality for managing products, shopping carts, and order processing.

## Getting Started

### Dependencies

## Dependencies

* alembic==1.12.0
* aniso8601==9.0.1
* blinker==1.6.2
* cffi==1.16.0
* click==8.1.7
* colorama==0.4.6
* cryptography==41.0.4
* Flask==3.0.0
* Flask-JWT-Extended==4.6.0
* flask-marshmallow==0.15.0
* Flask-Migrate==4.0.5
* Flask-RESTful==0.3.10
* Flask-SQLAlchemy==3.1.1
* greenlet==3.0.0
* importlib-metadata==6.8.0
* itsdangerous==2.1.2
* Jinja2==3.1.2
* Mako==1.2.4
* MarkupSafe==2.1.3
* marshmallow==3.20.1
* marshmallow-sqlalchemy==0.29.0
* mysqlclient==2.2.0
* packaging==23.2
* passlib==1.7.4
* pycparser==2.21
* PyJWT==2.8.0
* PyMySQL==1.1.0
* python-dotenv==1.0.0
* pytz==2023.3.post1
* six==1.16.0
* SQLAlchemy==2.0.21
* typing_extensions==4.8.0
* Werkzeug==3.0.0
* zipp==3.17.0


### Installing

1. Clone the repository:
    ```bash
   git clone https://github.com/JoseGayosoNeto/flask_e-commerce_REST_API.git
    ```

2. Navigate to the project repository:
    ```bash
    cd yourrepository
    ```

3. Navigate to the virtual environment (venv):
    ```bash
    cd venv/Scripts
    activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Executing program

1. Enter in the virtual environment:
    ```bash
    cd venv/Scripts
    activate
    ```

2. Create a `.env` file in the project root with the following content:
    ```bash
    SECRET_KEY = your_secret_key
    MAX_CONTENT_LENGTH = your_content_length
    CACHE_TYPE = your_cache_type
    USERNAME = your_username
    PASSWORD = your_password
    DB = your_db_name
    SQLALCHEMY_TRACK_MODIFICATIONS = your_sqlalchemy_track_modifications (True recommended)
    SQLALCHEMY_DATABASE_URI = mysql://{username}:{password}@localhost/{db_name}
    ```

    Replace `username`, `password`, `db_name` with your MySQL database credentials and a secure secret_key for Flask.

3. Apply database migrations:
    ```bash
    flask db init
    flask db migrations
    flask db upgrade
    ```

4. Set up the Flask application:
    * In Windows (cmd):
        ```bash
        set FLASK_APP=API
        ```

    * In Windows (PowerShell):
        ```bash
        $env:FLASK_APP = "API"
        ```

    * In Linux / macOS:
        ```bash
        export FLASK_APP=API
        ```

5. Run the Flask application:
    ```bash
    flask run
    ```

    ```bash
    flask --app API run
    ```  

6. Use tools like Postman or Insomnia to interact with the API endpoints.
    Set the base URL to `http://localhost:5000`
    * Example API routes:
        - `GET /products`: Retrieve all products.
        - `POST /user`: Register a new user account.
        - `POST /manage_cart`: Manage with the shopping cart.
        - `POST /complete-purchase`: Purchase of the products in the cart.
        - `PATCH /user/update_balance`: Update the user balance.

7. Explore and manipulate the routes using your preferred API testing tool.        

## Authors

* José Pires Gayoso de Almendra Freitas Neto
    * GitHub: https://github.com/JoseGayosoNeto
    * Email: josegayosoneto@outlook.com.br

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

