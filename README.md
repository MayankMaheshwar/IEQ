# 🧹 IEQ - Monorepo Microservices System

This project is a scalable monorepo-based microservices architecture, designed with security, reliability, and modularity in mind. Each microservice handles a specific domain (e.g., Products, Customers) and communicates via RESTful APIs.

---

## ⚙️ Features

- ✅ Microservices for modular and scalable architecture
- 🔐 JWT token-based authentication and password hashing for security
- 💥 Centralized error handling with try-catch blocks for reliability
- 📦 Monorepo structure for easier dependency and code management

---

## 📁 Microservices

### 1. **Products Service**

Handles product-related operations.

#### ➕ Create a Product
- **Endpoint**: `POST /products`
- **Request Body**:
  ```json
  {
    "name": "Product Name",
    "price": 19.99,
    "category": "Product Category"
  }
  ```
- **Responses**:
  - `201 Created` — Product created successfully
  - `400 Bad Request` — Missing or invalid data

#### 📆 Get All Products
- **Endpoint**: `GET /products`
- **Query Parameters**:
  - `search`: Filter products by name or category
  - `sort`: Field to sort by (e.g., name, price)
  - `order`: `asc` or `desc`
- **Response**:
  - `200 OK` — Returns a list of products

#### ✏️ Update a Product
- **Endpoint**: `PUT /products/<id>`
- **Request Body**:
  ```json
  {
    "name": "New Product Name",
    "price": 29.99
  }
  ```
- **Responses**:
  - `200 OK` — Product updated successfully
  - `404 Not Found` — Product not found

#### ❌ Delete a Product
- **Endpoint**: `DELETE /products/<id>`
- **Responses**:
  - `200 OK` — Product deleted successfully
  - `404 Not Found` — Product not found

---

### 2. **Customers Service**

Handles customer-related operations.

#### ➕ Create a Customer
- **Endpoint**: `POST /customers`
- **Request Body**:
  ```json
  {
    "name": "Customer Name",
    "email": "customer@example.com"
  }
  ```
- **Responses**:
  - `201 Created` — Customer created successfully
  - `400 Bad Request` — Missing or invalid data

#### 👤 Get Customer Details
- **Endpoint**: `GET /customers/<id>`
- **Response**:
  - `200 OK` — Returns customer details
  - `404 Not Found` — Customer not found

#### ✏️ Update Customer Details
- **Endpoint**: `PUT /customers/<id>`
- **Request Body**:
  ```json
  {
    "name": "Updated Name",
    "email": "updated@example.com"
  }
  ```
- **Responses**:
  - `200 OK` — Customer updated successfully
  - `404 Not Found` — Customer not found

#### ❌ Delete a Customer
- **Endpoint**: `DELETE /customers/<id>`
- **Responses**:
  - `200 OK` — Customer deleted successfully
  - `404 Not Found` — Customer not found

---

## 🔒 Security

- JWT-based user authentication
- Hashing (e.g., bcrypt) for sensitive data like passwords

---

## 📦 Dependencies

All necessary tools and libraries are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

