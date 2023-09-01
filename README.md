![image](https://user-images.githubusercontent.com/13378850/176657886-e99a1dff-afcf-431f-a093-757cddba0d15.png)

## Sano Genetics Backend Engineer Test
Thank you for taking the time to work on the Sano Genetics Backend Engineer test!

⚠️ Please, **do not fork this repository**. Instead, clone it into your own **private** repository called `sano-be-test` on GitHub.

Instead of commiting your changes directly to the main/master branch, create a separate branch to commit your changes to. At the end of the test, submit a pull request to the main/master branch. This will allow us to see all the changes during the code review.

Use as many commits as you normally would and write a detailed description for the PR to describe any decisions you've made and anything else you feel is relevant.

Ideally, you should aim to spend no longer than 3 hours on the tasks. If you can’t completely finish it, that’s not a problem - just explain what is left to do and how you would do it.

If, due to time constraints, you prefer to take some shortcuts, or in a real world scenario you would implement a particular logic/code in a better way, please feel free to leave comments thoughout your code explaining your alternative approach.


## Installation
This project was created using Python 3.8.10.

Install all dependencies, and run the application using:
```
export FLASK_ENV=development                                  
flask run
```


## Task 1

The goal of this task is to add an endpoint to our API that allows our admin users to place DNA Kit Orders on behalf of existing users on the platform. In `core/models.py` you'll see the `User` and `DNAKitOrder` models. 

Placing an order should notify the user that the order was successfully placed. Admin users would also like to be able to specify the channel used to send the notification (`email` or `sms`).

DNAKitOrders of type `whole-exome-sequencing` should notify users via `sms` while other types should notify them via `email`. To replicate a scenario where we need to integrate an external service (like [Postmark](https://postmarkapp.com/), [Amazon SES](https://aws.amazon.com/ses/), or [Twilio](https://www.twilio.com/messaging)) into your application. We have provided you a **Dummy Email Delivery Service** and a **Dummy SMS Delivery Service**, implemented as two endpoints on our development server, https://dev.sanogenetics.com. Note that these endpoints do not actually send emails or SMS messages and only serve to mimic the functionality of these external services.

#### Dummy Email Delivery Service

```
POST https://dev.sanogenetics.com/dev/home-test/email-delivery-service
```

The following header is required on each request:

```
Authorization: Bearer 7lPIazekwQu7Raz7FqBQmsLvlH29IDwG
```

Example of the expected payload:

```json
{
    "recipient": "user@email.com",
    "message": "Hi {user_name}, your order has been successfully placed."
}
```

#### Dummy SMS Delivery Service
```
POST https://dev.sanogenetics.com/dev/home-test/sms-delivery-service
```

The following header is required on each request:

```
Authorization: Bearer o8deGqg2vTGYXtvIsA05zOW8ywAPBQuB
```

Example of the expected payload:
```json
{
    "recipient": "07451277972",
    "message": "Hi {user_name}, your order has been successfully placed."
}
```

    

We would like you to interact with these notification services as part of a `NotificationService` class in your implementation. A potential way that developers could interact with this service could be something like the following:

```python
notification_service.notify(user, message="Your order has been placed!", channel='sms')
```

But we are open to different suggestions if you have different ideas! We expect this service to be extended in the future, for example, by adding new notification channels such as push notifications.


## Task 2

Update the existing `GET /users/` endpoint to return an additional `orders` property, which contains all `DNAKitOrders` associated with each `user`.


## Task 3

Create test cases for the above tasks. The external delivery APIs should not be accessed during server tests, as their usage should be limited to production only. However, we **do** want to test the logic of the notification code.


## Additional details
Here are some of the things we will be assessing in these tasks:
* Documentation and clarity
* Testing 
* Architecture & System design
* Web standards
* Error handling

Feel free to refactor the provided boilerplate code or update anything that you think doesn't look right or could be improved.


# Submitting the test

1. Please create a short Loom video (~5 minutes) to explain:
* How you approached the test.
* Where you took a pause to make a decision about any task. Why did you make that decision?
* If you struggled with any parts of the test, what were they?
* If you had more time, what would you improve or change?


2. Give the GitHub user [@sano-review](https://github.com/sano-review) access to your private repository

Thank you and we hope you have fun with the test!

# Solution

[Link to Loom video](https://www.loom.com/share/13dca2c4be604f3a9c82145a0eeb54cb)

- The project is written using Hexagonal architecture (separated into modular use cases/gateways) and TDD principles.
- Each created python file has its test counterpart in the parallel "test" package, which mimics the main project structure.
- There are two disabled tests - it's on purpose as they are e2e tests that checks the interaction between the application and the third party API. They are disabled so they don't send requests every time tests runs.
- Although there is a small UI prototyped, the application works primarily through web API.
- Tests are run by running "pytest".
- Users can access the prototyped UI of the application by going to localhost:5000.
- Users can also send POST/GET requests to the application itself through these commands:

Adding a user
```
curl --location 'localhost:5000/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "phone_number": "123456789",
    "email": "test.testington@gmail.com",
    "address": {
        "street": "123 Main Street"
    },
    "name" : "Jack"
}'
```

Ordering a kit
```
curl --location 'localhost:5000/order' \
--header 'Content-Type: application/json' \
--data '{
    "user_id": "cRzpaRTeP6o8SYkUFLsZ4p",
    "sequencing_type": "dna-whole-exome-sequencing",
    "shipping_info": {
        "some": "info"
    }
}'
```

Potential improvements:
- Use a .env file to store keys
- There's some implementation information bleeding between gateways and usecase. In theory gateways should return entities/null while usecases should return dictionaries of data. In this particular case, the `get_by_id` and `get_all_users` from the UserGateway returns two different types.
- The UI is not tested (I kept the focus on the backend side) and optimizable.

About Task 3 in particular, using hexagonal architecture lets it naturally be tested in its various stages (data loading/usecase/blueprint).
The tests in particular are:
- Gateway level:
  - `test_user_gateway_gets_user_by_id_from_database`
  - `test_order_gateway_returns_order_data` 
  - `test_order_gateway_returns_order_data (integration)`
- UseCase level:
  - `test_get_all_users_usecase_returns_list_of_users_with_order_information`
- Blueprint level:
  - `test_get_all_users_api_returns_list_of_users_with_order_information`


About `test_order_gateway_returns_order_data` and `test_order_gateway_returns_order_data (integration)`, I wrote these particular tests as I couldn't mock the database library functions (as I'm not used to the particular library) - so I've created two tests, one that "circumvents" the problem by mocking a helper function in the gateway itself where the data loading is placed, while the other test file checks the integration itself with the database.
