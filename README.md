
# Python CRUD Application for Car Rental Management System

A **car rental management system** built with Python. This application allows rental center staff to manage cars: adding new ones, updating details, handling rentals/returns, filtering lists, and more — all through a simple terminal interface.

---

## Features

- **Rent a Car**
  - View available cars, choose, and pay based on rental duration.
- **Return a Car**
  - Return rented cars, with late return handling.
- **Add New Cars**
  - Input car details and add to the system.
- **View & Filter Cars**
  - Display all cars or filter by price, model, brand, status, etc.
- **Update Car Data**
  - Modify existing car details (brand, model, fuel type, etc.).
- **Remove Cars**
  - Delete one, many (using filters), or all cars from the system.
- **Simulate Time**
  - Reduce remaining rental days for all rented cars.

---

## Data Structure

Car data is stored as a dictionary:

```python
database = {
    "LICENSE_PLATE": ["License Plate", "Brand", "Model", "Fuel Type", "Price/Day", "Status", "Days Left"]
}
```

Two additional sets are used to track car availability:
- `available_keys`
- `not_available_keys`

---

## Dependencies

- Python 3.x
- `tabulate` (for clean table display)

Install it using:
```bash
pip install tabulate
```

---

## Usage

1. Make sure Python and `tabulate` are installed.
2. Run the script:
```bash
python Capstone_1.py
```
3. Follow the on-screen prompts in the terminal.

