# IEQ


Design the system of monorepo microservices
microservices will help in scalability, used JST token and hashing for security, proper error try-catch for reliability
tools and libraries are mentioned in requirements.txt


. Products Endpoint

Create a Product (POST): /products

Body: { "name": "Product Name", "price": 19.99, "category": "Product Category" }
Response: 201 Created with product details or 400 Bad Request if data is missing.

Get All Products (GET): /products

Query Parameters: search, sort, order
Response: 200 OK with a list of products.

Update a Product (PUT): /products/<id>

Body: { "name": "New Product Name", "price": 29.99 }
Response: 200 OK with updated product details or 404 Not Found if product doesn't exist.

Delete a Product (DELETE): /products/<id>

Response: 200 OK if deletion was successful or 404 Not Found if product doesn't exist.



. Customers Endpoint

Create a Customer (POST): /customers

Body: { "name": "Customer Name", "email": "customer@example.com" }
Response: 201 Created with customer details or 400 Bad Request if data is missing.

Get Customer Details (GET): /customers/<id>

Response: 200 OK with customer details or 404 Not Found if the customer doesn't exist.

Update Customer Details (PUT): /customers/<id>

Body: { "name": "Updated Name", "email": "updated@example.com" }
Response: 200 OK with updated customer details or 404 Not Found if the customer doesn't exist.


Delete a Customer (DELETE): /customers/<id>
Response: 200 OK if deletion was successful or 404 Not Found if the customer doesn't exist.