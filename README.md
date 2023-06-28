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

This part is for you! Please drop your loom video link in here as well as anything else you'd like to add/link to.
