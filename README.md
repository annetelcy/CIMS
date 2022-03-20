

# Clinical Inventory Management System (CIMS)

This application is designed to facilitate our inventory management. With CIMS, we can keep track of various drugs, medical supplies, their respective locations, and more, ensuring seamless operations and accurate product balance reports.

## Features

- **Inventory Tracking**: Maintain a list of drugs and medical supplies with the correct dates.
- **Location Management**: Keep track of where supplies are sourced from and where they're dispatched.
- **Date Records**: Always be informed of the exact dates of transactions or movements.
- **Product Balance Report**: Generate reports to understand the current status of supplies, ensuring to never run out of supplies.

## Technologies Used

- **Python**: Backend
- **Flask**: Web framework for API's
- **SQLAlchemy**: ORM (Object Relational Mapper) for our database operations

## Getting Started

### Prerequisites

Ensure you have Python and pip installed on your system. 

### Installation

1. Clone this repository:
   ```
   git clone [repository-link]
   ```

2. Navigate to the directory and install required packages:
   ```
   cd [directory-name]
   pip install -r requirements.txt
   ```

3. Run application:
   ```
   flask run
   ```

4. Navigate to `http://127.0.0.1:5000/` on your browser to access the application.


### Sreenshots

### This shows the first part of the dashboard which contains the Products and Locations sections

<img width="902" alt="image" src="https://github.com/annetelcy/CIMS/assets/99223782/1f7627a6-8395-4807-9c4c-552da672cbf1">

### This shows the second part of the dashboard while you can add and display locations

<img width="911" alt="image" src="https://github.com/annetelcy/CIMS/assets/99223782/29742b05-9efe-4ff9-b22c-4f44d31c687a">


### This shows the Movements section which illustrates source and destination of a product

<img width="791" alt="image" src="https://github.com/annetelcy/CIMS/assets/99223782/7b827b77-e0b1-4106-bf43-64c768b9dfe7">

### Display  the momevements recorded

<img width="791" alt="image" src="https://github.com/annetelcy/CIMS/assets/99223782/22832119-f453-4e15-899b-0c9ab2d76adf">


### Demonstrate the product balance reports  which indicates the quantities of each product in each location

<img width="787" alt="image" src="https://github.com/annetelcy/CIMS/assets/99223782/8b09bdf0-ac7e-4157-a530-5d8df7f559ca">





