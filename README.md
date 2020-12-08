# Hometap Coding Challenge

## This flask app pretends to call the HouseCanary API to determine if an inputted address has a septic sewage system.
---
## Setup
1. Clone Repo
2. From top level directory, run:
    - ` pip install -r requirements.txt`
    - `python routes.py`  
    _this will start the flask app_

3. From Postman:
    - Make a GET request to `http://127.0.0.1:5000`
        - Params:
            - address: 123 Elm St
            - zip: 98765
4. From cURL:
    ```
    curl -X GET \
    'http://127.0.0.1:5000/?address=123%20elm%20st&zip=98765' \
    -H 'Postman-Token: aa9730d9-3398-498b-9d41-ba1905d0a495' \
    -H 'cache-control: no-cache'
    ```

