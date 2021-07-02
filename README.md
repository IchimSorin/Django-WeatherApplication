![Django-WeatherApp](https://user-images.githubusercontent.com/34681854/124274826-672d0a80-db4a-11eb-9787-e3fe0d83f995.png)
# Django-WeatherApplication
The application involves displaying weather conditions in different cities around the world. The operation of the application involves the following steps: <br>
1. The user enters the name of a city. The backend of the application takes the information through a form and saves it in the database, refreshing the page. <br>
2. Call the route / access the application database from which it extracts all the cities registered by the user, then use the REQUESTS library to obtain the meteorological information for each city <br>
3. The list of information obtained in step 2 is displayed in the HTML file using a for loop. <br>
<br><hr>
How to run the application:<br>
a) Source the virtual environment: [pipenv shell] <br>
b) Install the dependencies: [pipenv install requests] <br>
c) Run the command: python .\manage.py runserver
<br><hr>
Tutorial link: https://www.digitalocean.com/community/tutorials/how-to-build-a-weather-app-in-django
