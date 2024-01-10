# NBAjerseyShop 

Welcome to the NBA Jersey Shop, online store selling NBA player jerseys.
Project created to show our skills.

![Homepage](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/home_page.png?raw=true)

## Table of contents
* [Installation process](#installation-process)
* [Technologies](#technologies)
* [Features](#features)
* [Tests](#tests)
* [About authors](#authors)

## Installation process:

1. Clone the repository to your local computer:

    ```
    $ git clone 'https://github.com/cyberaff/NBAjerseyShop.git'
    ```

2. Navigate to the project directory:

    ```
    $ cd NBAjesrseyShop
    ```

3. (Optional) It is recommended to create and activate a Python virtual environment:

    ```
    $ python -m venv venv
    ```
    Activate for windows:
    ```
    $ python venv\Scripts\activate
    ```
    Activate for Linux:
    ```
    $ python venv/bin/activate
    ```

4. Install the required dependencies:

    ```
    $ pip install -r requirements.txt
    ```

5. Create database 'db.sqlite3' using migration:

    ```
    $ python manage.py migrate
    ```

6. Run the Django development server:

    ```
    $ python manage.py runserver
    ```

    The application will be available at http://localhost:8000/.

7. (Optional) Change the database to the one available at the link below with all NBA teams saved and 10 sample player jerseys:

    https://drive.google.com/drive/folders/1vmaOkXcj8qwCzvUDUeTdR3fSuZd0w0zx?usp=sharing 



## Technologies

### HTML5, CSS3 and Bootstrap

For the frontend, we used HTML5, CSS3 and Bootstrap5, which allowed us to create an intuitive and user-friendly user interface.

### Python and Django

We provided a strong backend foundation by using Python 3.11 and Django 4.2. Python offers the latest features, bug fixes and optimizations, which contributes to effective and modern application development. Django 4.2, as a high-level web framework, provides tools for quickly creating solid web applications.



## Features

The aim of the project was to create an online store enabling users to buy NBA players' jerseys, where orders and adding products are handled by the administrator. The website was created to improve skills in the Django framework, as a culmination of the comprehensive "Python from scratch" course at Software Development Acadamy.

### Accounts app:
An application created to manage user accounts. Enables registration, login and logout.

#### Registration:

![Registrationpage](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/registration_page.png?raw=true)

#### Log in:

![Loginpage](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/login_page.png?raw=true)

### Shop app:
The shop application is responsible for displaying products on the home page and on the page with jerseys of a specific selected team, as well as on the page with details of the selected product.

#### Homepage:

![Homepage](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/home_page.png?raw=true)

#### Team jerseys page:

![Teampage](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/team_page.png?raw=true)

#### Jersey detail page:

![Jerseydetail](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/detail_page.png?raw=true)

### Cart app:

It allows you to view the contents of the basket, add and remove products, as well as update the quantity of the selected product. Everything was implemented using sessions.

#### Cart view:

![Cart](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/cart_page.png?raw=true)

### Orders app:

Responsible for placing orders and saving them to the database. This application also allows you to view previously placed orders.

#### Order page:

![Orderpage](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/order_page.png?raw=true)

#### Thank you page after placing your order:

![Ordercreated](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/order_created_page.png?raw=true)

#### User's order page:

![Orderspage](https://github.com/cyberaff/NBAjerseyShop/blob/main/README_img/user_orders_page.png?raw=true)

### Administration panel:

All order processing and adding products is possible thanks to the administration panel.

![Adminpanel](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/adminpanel.PNG?raw=true)



## Tests:

Using the built-in test module provided by Django, specifically using the `TestCase` class, we conducted comprehensive unit tests of the implemented components of our applications.

The report on the level of code coverage with tests is presented below:

![Coveragereport](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/coveragereport.PNG?raw=true)



## Authors:

 <h2>Rafał Ćwikła</b>
 <h3>Junior Python Developer</p>
 <li><a href="https://www.linkedin.com/in/rafalcwikla/">LinkedIn Profile</a></li>
 <br>
 <p>And</p>

 <h2>Filip Fibakiewicz</b>
 <h3>Junior Python Developer</p>
 <li><a href="https://www.linkedin.com/in/filfib/">LinkedIn Profile</a></li>
 <br>
 <h3>Final visual effects (background, footer etc.) made by Rafał Ćwikła</p>
 
