# e-martAPI

e-martAPI is a Django REST Framework-based backend for an e-commerce platform, providing APIs for managing products, orders, and user authentication.

## Features

- **Product Management**: APIs to create, retrieve, update, and delete products.
- **Order Processing**: Handle customer orders, including order creation and status updates.
- **User Authentication**: User registration and login functionalities.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DavidDanso/e-martAPI.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd e-martAPI
   ```

3. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Products**:
  - `GET /api/products/`: List all products.
  - `POST /api/products/`: Create a new product.
  - `GET /api/products/{id}/`: Retrieve a specific product.
  - `PUT /api/products/{id}/`: Update a product.
  - `DELETE /api/products/{id}/`: Delete a product.

- **Orders**:
  - `GET /api/orders/`: List all orders.
  - `POST /api/orders/`: Create a new order.
  - `GET /api/orders/{id}/`: Retrieve a specific order.
  - `PUT /api/orders/{id}/`: Update an order.
  - `DELETE /api/orders/{id}/`: Delete an order.

- **Authentication**:
  - `POST /api/auth/register/`: Register a new user.
  - `POST /api/auth/login/`: Log in a user and obtain a token.

## Configuration

- **Database**: Configured to use SQLite by default. To use another database, update the `DATABASES` setting in `settings.py`.
- **Environment Variables**: Create a `.env` file to manage sensitive settings like secret keys and database credentials.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:

   ```bash
   git checkout -b feature-branch
   ```

3. **Make your changes and commit**:

   ```bash
   git commit -m "Description of changes"
   ```

4. **Push to your fork**:

   ```bash
   git push origin feature-branch
   ```

5. **Create a pull request**.
