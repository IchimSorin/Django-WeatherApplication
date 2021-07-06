![Capture](https://user-images.githubusercontent.com/34681854/124608414-62809300-de77-11eb-88d9-99a500b71c7e.PNG)

# Django-WeatherApplication
The application involves displaying weather conditions in different cities around the world. The operation of the application involves the following steps: <br>
1. The user enters the name of a city. The backend of the application takes the information through a form and saves it in the database, refreshing the page. <br>
2. Call the route / access the application database from which it extracts all the cities registered by the user, then use the REQUESTS library to obtain the meteorological information for each city <br>
3. The list of information obtained in step 2 is displayed in the HTML file using a for loop. <br>
<br><hr>
FEATURES:<br>
a) Implementing the city delete button in the database.<br>
b) Before saving a new city to the database, check if it exists in the API database.<br>
c) The cities in the database must be unique. If an attempt is made to save an existing city, the run command is not executed.<br>
d) All actions display a suggestive message.<br>
<br><hr>
How to run the application:<br>
a) Source the virtual environment: [pipenv shell] <br>
b) Install the dependencies: [pipenv install requests] <br>
c) Run the command: python .\manage.py runserver
<br><hr>
Tutorial link: https://www.digitalocean.com/community/tutorials/how-to-build-a-weather-app-in-django
