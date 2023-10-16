# SrushEats
I have created a serverless, micro service-driven web application created completely using AWS cloud services. The main application of this chatbot is to provide restaurant recommendations to the users based on the preferences provided to it through conversations.  We have support for Yelp-API with suggestions and real time chat.

Here are the following steps :
1. S3 bucket 
2. html link : https://srusheats.s3.amazonaws.com/chat.html
enable cors on the terminal as I was having issues by : open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security
then access the chrome tab

Functionalities deployed :
1. Amazon S3 - To host the frontend
2. Amazon Lex - To create the bot
3. API Gateway - To set up the API
4. Amazon SQS - to store user requests on a first-come bases
5. ElasticSearch Service - To quickly get restaurant ids based on the user preferences of cuisine collected from SQS
6. DynamoDB - To store the restaurant data collected using Yelp API
7. Amazon SNS - To send SMS to registered phone number.
8. Amazon SES - to send restaurant suggestions to users through email
9. Lambda - To send data from the frontend to API and API to Lex, validation, collecting restaurant data, sending suggestions using SNS.
10. Yelp API - To get suggestions for food
