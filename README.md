# StockIQ

AI-Powered Inventory Management System built with FastAPI, PostgreSQL, JWT Authentication, Pandas, and Scikit-learn.

## Overview

StockIQ is a full-stack inventory management platform designed to help businesses track products, manage stock movements, generate reports, and forecast future inventory demand using machine learning.

## Features

### Authentication & Authorization

* User Registration
* User Login
* JWT Authentication
* Role-Based Access Control (Admin, Manager, Staff)

### Inventory Management

* Product Management
* Category Management
* Supplier Management
* Stock In Operations
* Stock Out Operations
* Inventory Tracking

### Analytics & Reporting

* Inventory Value Reports
* Low Stock Reports
* Stock Movement Reports
* CSV Export

### Machine Learning

* Demand Forecasting
* Reorder Recommendations
* Inventory Trend Analysis

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication

### Frontend

* HTML5
* CSS3
* JavaScript

### Machine Learning

* Pandas
* NumPy
* Scikit-learn
* Matplotlib

### Deployment

* Backend: Render / Railway
* Frontend: Vercel

## Project Structure

backend/
├── app/
│ ├── auth/
│ ├── models/
│ ├── schemas/
│ ├── routers/
│ ├── services/
│ ├── ml/
│ ├── database.py
│ ├── config.py
│ └── main.py
│
├── requirements.txt
├── .env
└── README.md

frontend/
├── index.html
├── dashboard.html
├── products.html
├── categories.html
├── transactions.html
└── reports.html


## Run Application

uvicorn app.main:app --reload

## API Documentation

http://localhost:8000/docs

## Future Improvements

* Barcode Scanner Integration
* QR Code Product Tracking
* Email Notifications
* Real-Time Dashboard
* Multi-Warehouse Support
* Deep Learning Demand Forecasting