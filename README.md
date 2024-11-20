# Scraper
Repository for scraping weekly menu data

It was implemented using Python Scrapy.


# Logic

![kiryong-scrapy](https://github.com/user-attachments/assets/04f58d5c-7a2e-4838-a613-a707076fb65b)

### Scraping

1. Create a scheduler in EventBridge to trigger a Lambda function every Monday at 9 AM.
2. The triggered Lambda function uploads the scraper to an ECS task.
3. The scraper performs the scraping and stores the results in an S3 bucket.

### Data Update

1. When the `output.csv` in the S3 bucket is updated, a trigger activates and invokes a Lambda function.
2. The invoked Lambda function sends an HTTPS request to the Spring server.
3. The server receiving the request reads the data from the S3 bucket and executes logic to insert it into the database.

