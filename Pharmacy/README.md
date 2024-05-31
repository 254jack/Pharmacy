Pharmacy Management System
Introduction
This project is a comprehensive Pharmacy Management System designed to streamline and automate the various processes involved in running a pharmacy. The system includes features for managing inventory, sales, prescriptions, customer records, and more. This README provides a detailed overview of the system, installation instructions, and how to use it.

Table of Contents
Introduction
Features
Tech Stack
Installation
Usage
API Integration
Configuration
Testing
Contributing
License
Contact
Features
Inventory Management: Track and manage stock levels, expiration dates, and batch details.
Sales Management: Process sales transactions, print receipts, and track daily sales.
Prescription Management: Manage prescriptions, doctor information, and patient records.
Reporting: Generate reports on sales, inventory, and prescriptions.
User Management: Role-based access control for admin, pharmacists, and assistants.
Alerts and Notifications: Expiry alerts and low stock notifications.
Tech Stack
Backend: Django, Django REST Framework
Frontend: HTML, CSS, JavaScript, Bootstrap
Database: PostgreSQL
APIs: Integration with LinkedIn API for user articles data
Others: ModemManager for HSDPA modem connectivity
Installation
Prerequisites
Ensure you have the following installed:

Python 3.8+
PostgreSQL
pip (Python package installer)
Steps
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/pharmacy-management-system.git
cd pharmacy-management-system
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Database Setup:

Create a PostgreSQL database.
Update the database settings in settings.py.
python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourdbuser',
        'PASSWORD': 'yourdbpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Run Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser:

bash
Copy code
python manage.py createsuperuser
Run the Server:

bash
Copy code
python manage.py runserver
Usage
Accessing the System
Open your web browser and go to http://127.0.0.1:8000/.
Log in with the superuser credentials created earlier.
Managing Inventory
Navigate to the Inventory section.
Add, update, or delete products.
Monitor stock levels and expiry dates.
Processing Sales
Navigate to the Sales section.
Enter product details and process transactions.
Print receipts for customers.
Managing Prescriptions
Navigate to the Prescriptions section.
Add new prescriptions and associate them with customer records.
Manage doctor and patient information.
API Integration
LinkedIn API
This system includes integration with the LinkedIn API to fetch data related to user articles (title, likes, impressions, etc.).

Configuration
Get LinkedIn API Credentials:

Register your application on the LinkedIn Developer Portal.
Obtain your Client ID and Client Secret.
Set Up Environment Variables:

Create a .env file in your project root and add your LinkedIn credentials.
env
Copy code
LINKEDIN_CLIENT_ID=your_client_id
LINKEDIN_CLIENT_SECRET=your_client_secret
Fetch User Articles:

Implement the API calls in your Django views to fetch and display LinkedIn article data.
Testing
Run the following command to execute the test suite:

bash
Copy code
python manage.py test
Contributing
We welcome contributions from the community. Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries, please contact:

Taixon J (taixonj@gmail.com)
