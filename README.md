**Install**

```$ pip install -r requirements.txt```



**Run**
1. Replace xxxxxxxxxxxxxxxxxxx in _PRIVATE.txt with access token
2. ```$ python server.py start``` to start the server
3. App will run on ```http://localhost:5000/```




**Working**
1. Flask app
2. Two API's, one for totals and another for daily numbers. API endpoints have start date, end date and access token input attributes. These are then used when querying the data from giosg Reporting APIs.
3. App makes ```HTTP GET``` request to giosg reporting API to fetch chat counts between those two given dates.
4. After recieving data, it is display on a UI and is paginated to display maximum of 5 items on the table per view/page ```homepage.html```(Screenshot below)

![](/images/screenshot.png)

