# Django & Django REST framework test project.


<b>Language:</b> Python <br>
<b>Frameworks:</b> Django, Django REST <br>


### Features

  - There is pre-build structure for Hotels and Apartments. With prefilled database.
      - superuser
        - username: **admin**
        - password: **admin**

  - This app sends JSON/API response of Apartment and Hotel Object.
  - JSON/API response of the object contains all the infos connected to it, 'listing_type', 'title', 'country', 'city', 'price'.
  - Here, returned objects are sorted lowest to highest price, that means 'price' in in ascending order.
  - Here, response can be filtered / searched based on filter / search criteria.



### Instructions to run this app on local machine

First, Clone the repository and go to the project folder
```console
git clone https://github.com/Jilanichy/BookingEngine && cd BookingEngine
```
Run the app on a virtualenvironment is preferred. To create a virtualenv
 ```console
 virtualenv --python=/usr/bin/python3.7 venv
```
To activate virtualenv
 ```console
 source venv/bin/activate
```
Install required dependencies of the project
 ```console
 pip install -r requirements.txt
```

After that, to populate the database with data run
```console
python manage.py makemigrations
python manage.py migrate
```

Finally, start the application with the following command and open it on local server
```console
python manage.py runserver
```
Three basic endpoints are
```console
api/v1/units/
admin/
api-auth/
```


## Request example:

http://localhost:8000/api/v1/units/?max_price=100&check_in=2021-12-09&check_out=2021-12-12


## Response example:

    {
        "items": [
            {
                "listing_type": "Apartment",
                "title": "Luxurious Studio",
                "country": "UK",
                "city": "London",
                "price": "40"

            },
            {
                "listing_type": "hotel",
                "title": "Hotel Lux 3***",
                "country": "BG",
                "city": "Sofia",
                "price": 60

            },
            {
                "listing_type": "Apartment",
                "title": "Excellent 2 Bed Apartment Near Tower Bridge",
                "country": "UK",
                "city": "London",
                "price": "80"
            },
            {   "listing_type": "apartment",
                "title": "Excellent 2 Bed Apartment Near Tower Bridge",
                "country": "UK",
                "city": "London",
                "price": 90
            },
            {
                "listing_type": "apartment",
                "title": "Hotel Lux 5***",
                "country": "UK",
                "city": "London",
                "price": 95
            }
        ]
    }


## Request example:

http://localhost:8000/api/v1/units/?city=Sofia

## Response example:
![2](https://user-images.githubusercontent.com/32903934/116540216-adc47580-a90b-11eb-9aa9-2816855ef67a.png)



## Request example:

http://localhost:8000/api/v1/

## Response example:
![1](https://user-images.githubusercontent.com/32903934/116541746-ac944800-a90d-11eb-8813-dc8aa6103ce7.png)

