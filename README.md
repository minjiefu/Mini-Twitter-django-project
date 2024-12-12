#  Title
A Twitter-like Website (backend development)

# Purpose
This project aimed at develop the backend of a twitter-like website. It implemented the core functionalities including Tweets, Friendships, News Feeds, Comments, and Likes. 

# Highlights
- Used push model to fanout news feeds
- Employed Redis and Memcached to minimize database queries for high read-to-write ratio tables
- Leveraged HBase for optimal database query optimization on tables with more write operations
- Implemented denormalization techniques to reduce database queries by storing comment and like counts
- Utilized Message Queues for asynchronous task execution, enhancing system responsiveness

# Technical Stack
Git, Python, Django, MySQL, HBase, Redis, Memcached, RabbitMQ, Amazon S3
