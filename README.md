# Selenium Automation Practice

This project contains a collection of automation exercises using **Selenium WebDriver** with Python.
All exercises were done using **Visual Studio Code** as code editor.

---

## Files & Descriptions

### 1. `test_google.py`
- **Description:**
  First practice using Selenium to open Google and perfom an automated search
- **Website used:**
  [https://www.google.com]
- Learn the basics of Selenium
- Launch an automated browser
- Type a search query and press Enter

---

### 2. `login_test.py`
- **Description:**
  Second practice focusing on testing the **login** process on a dummy website
- **Website used**
  [https://practicetestautomation.com/practice-test-login/]
- **Learning goals:**
  - Fill in username and password automatically
  - Click the login button
  - verify that login is successful

---

### 3. `saucedemotest.py`
- **Description:**
  Third practice based on an e-commerce scenario to test the shopping flow.
- **Website used:**
  [https://www.saucedemo.com/]
- **Learning Goals:**
  - Log in to the site automatically
  - Add a product to the cart
  - Proceed to checkout
  - Fill in buyer information
  - Complete the purchase
 
---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Pandelll/Selenium-first-learning.git
   cd selenium-practice
   ```
2. Create a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\active  #Windows
   source venv/bin/active # Mac/Linux
   ```
3. Install all dependencies
   ```bash
   pip install -r requirements.txt
   ```
## How to Run

Run the following command:
```bash
python file_name.py
```

Example:
```bash
python test_google.py
```

## Technologies Used

- Python 3.13.3
- Selenium
- WebDriver Manager

