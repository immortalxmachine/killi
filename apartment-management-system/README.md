# Apartment Management System

This project is a web-based application for managing apartments, residents, staff, maintenance requests, rent payments, and visitors. It is built using Flask, a lightweight WSGI web application framework in Python.

## Project Structure

```
apartment-management-system
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Defines the application routes
│   ├── static
│   │   └── styles.css       # CSS styles for the application
│   ├── templates
│   │   └── killi3.html      # HTML template for the front end
│   └── database.py          # Manages database connections and queries
├── requirements.txt         # Lists project dependencies
├── run.py                   # Entry point for running the application
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd apartment-management-system
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   Ensure you have a MySQL database set up and configured as per the `database.py` file.

5. **Run the application:**
   ```
   python run.py
   ```

## Usage

- Navigate to `http://127.0.0.1:5000` in your web browser to access the application.
- Use the provided interface to manage apartments, residents, staff, maintenance requests, rent payments, and visitors.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.