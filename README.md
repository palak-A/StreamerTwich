# How to run server:
python manage.py runserver

# How to access in browser:
http://localhost:8000/
1. Authenticate twitch
2. Enter the streamer name and click "Set", suggested values: "fuslie", "moczy"

#Improvements:
1. Database can be used for storing the credentials amd user info, events etc.
2. Authentication could be improved by using refresh token.
3. Testcases can be added.
4. Design could be more generic to handle multiple thrind party integrations.


Question:
How would you deploy the above on AWS? (ideally a rough architecture diagram will help)
Answer: Lets assume for now that we are trying to handle for 100/request per day for now.
 
Based on this load we can initially start with 2 instance of EC2 and deploying the code on both the machines.
2. We can use Elastic Load balanace from AWS for balancing the load on these servers.
3. Maintaning two servers will also take care of single point of failure .
4. We need to maintain a Database to store the credentials /user info /events in db.
   We can go with SQL kind of database , preferrably Mysql to store this informatino .
   Why SQL - Most of the data in our case is structured and possibly not required too many iterations of db changes , We can make it work with NoSQL(Casandra , Mongo etc) as well but NoSQL is not best suited here .
   We can also use Amazon SQL offeerings.

For Mysql , we can have two servers (Primary Server and Secodary Server) for handling this load ,two servers are required so that we do not have single point of failre.


Where do you see bottlenecks in your proposed architecture and how would you approach scaling this app starting from 100 reqs/day to 900MM reqs/day over 6 months?
Answer: Currently i have proposed the architecture with two instances. we can choose auto scaling here to support growing request and also we can add more load balancers if required, so that there is no single point of failure for load balancers as well.
