

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

![Dashboard Screenshot](screenshots\Dashboard.png) 

### This shows the second part of the dashboard while you can add and display locations

![Locations Screenshot](screenshots\Locations.png)  

### This shows the Movements section which illustrates source and destination of a product


![Movement Screenshot](screenshots\Movement.png)  

### Display  the momevements recorded

![MovementTable Screenshot](screenshots\MovementTable.png)  

### Demonstrate the product balance reports  which indicates the quantities of each product in each location

![balanceReport Screenshot](screenshots\balanceReport.png)  




