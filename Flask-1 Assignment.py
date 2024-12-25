# Q1. What is Flask Framework? What are the advantages of Flask Framework?
Flask is a micro web framework written in Python that allows you to build web applications quickly and efficiently. It is lightweight and easy to use, providing the necessary tools to build web services, APIs, and dynamic websites. Flask is designed to be flexible and modular, meaning that it does not impose any specific structure on how applications should be organized. This gives developers the freedom to structure their projects the way they want.

Advantages of Flask Framework:

Lightweight and Flexible: Flask is lightweight and provides only the essential tools, making it a flexible framework for developing applications.
Easy to Learn and Use: Flask is simple to understand and provides clear documentation, making it ideal for beginners.
Minimalistic: Flask does not impose any dependencies or libraries, allowing developers to add only what they need.
Extensibility: Flask is highly extensible, allowing you to add custom extensions for database integration, form handling, authentication, and more.
Good for Prototyping: Due to its simplicity and flexibility, Flask is a great choice for quickly building prototypes or small applications.
Active Community: Flask has an active and growing community that contributes to libraries, tutorials, and other resources.




# Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.
Here is a simple Flask application to display "Hello World!!":

python
Copy code
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Hello World!!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
To execute this code, run it in your local environment. The Flask server will start, and when you visit http://127.0.0.1:5000/ in your browser, it will display "Hello World!!".

Screenshot: Unfortunately, I cannot display or capture a screenshot directly in this environment. However, once you run the application, you should be able to see the result in the browser.





# Q3. What is App routing in Flask? Why do we use app routes?
App routing in Flask refers to the mechanism used to map URLs to specific functions or views in your application. Each route in Flask is associated with a URL pattern and a function that is executed when the URL is visited. This allows you to define different views or actions for different parts of your website.

Why do we use app routes?

URL Handling: Routes help define how a URL path corresponds to a function. They allow the server to respond to different URLs with appropriate content or actions.
Separation of Concerns: By using routes, you can clearly separate the logic for different parts of your application, making it more maintainable and organized.
Dynamic Responses: Flask routes can accept dynamic values through URL variables, allowing you to build dynamic web applications.
For example:

python
Copy code
@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/about')
def about():
    return 'About Us'
In this case, visiting / will call home(), and visiting /about will call about().






# Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/” route to show the following details:
Company Name: ABC Corporation
Location: India
Contact Detail: 999-999-9999
Here’s the code for both routes:

python
Copy code
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Route for welcome message
@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

# Route for company details
@app.route('/')
def company_details():
    return '''
    Company Name: ABC Corporation<br>
    Location: India<br>
    Contact Detail: 999-999-9999
    '''

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
To see the output:

Visit http://127.0.0.1:5000/welcome to see the welcome message.
Visit http://127.0.0.1:5000/ to see the company details.
Again, I can't show the screenshot here, but after running the Flask app, you should see the respective messages in your browser.







# Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.
The function used in Flask for URL building is url_for(). This function generates a URL for a given function (route). It is especially useful for creating links to views without hardcoding the URL paths.

Here’s an example of using url_for() to dynamically generate a URL for a route:

python
Copy code
from flask import Flask, url_for

# Create Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/generate-url')
def generate_url():
    # Use url_for() to generate URL for 'about' route
    about_url = url_for('about')
    return f'The URL for the About page is: {about_url}'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
The url_for('about') will return the URL for the about route, which in this case is /about.
To test the URL building, you can visit the route /generate-url, which will dynamically display the URL for the about page.
For instance, when you visit http://127.0.0.1:5000/generate-url, the response will show:

bash
Copy code
The URL for the About page is: /about