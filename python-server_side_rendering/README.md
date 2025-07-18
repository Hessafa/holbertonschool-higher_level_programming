# Python Server-Side Rendering with Flask
This project demonstrates how to build server-rendered web applications using Flask and Jinja2. It covers generating HTML on the server side, using dynamic templates, and loading data from JSON, CSV, and SQLite sources.

## Main Points 
Server-side rendering vs client-side rendering

Dynamic HTML generation with Jinja2

Flask routing and templating

Reading data from JSON, CSV, and SQLite

Handling query parameters and errors

## Tasks Overview
0. Templating with Python
Created a function that reads a text template and a list of attendees, generating personalized invitation files. Included error handling for missing data or invalid inputs.

1. Basic Flask Template
Built a simple Flask app with a homepage using Jinja templates. Added reusable header and footer templates, and created separate pages for Home, About, and Contact.

2. Dynamic Template with JSON
Used a JSON file to display a list of items dynamically in an HTML page. Used Jinja loops and conditionals to handle empty lists gracefully.

3. Load Data from JSON or CSV
Extended the app to load product data from JSON or CSV, based on the ?source= parameter. Supported optional filtering with ?id=, and displayed error messages for invalid inputs.

4. Integrate SQLite
Added support for loading product data from a SQLite database with ?source=sql. Reused the same HTML template and handled database errors or invalid queries.

## Project Structure
<pre> 
python-server_side_rendering/
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── templates/
│ ├── index.html
│ ├── about.html
│ ├── contact.html
│ ├── items.html
│ ├── product_display.html
│ ├── header.html
│ └── footer.html
├── items.json
├── products.json
├── products.csv
└── products.db  </pre>
