
import requests
from flask import Flask, redirect, url_for, session, request, render_template
import json
import math


app = Flask(__name__)
app.debug = True
app.secret_key = 'development'


#Access token from private file
access_token = open('_PRIVATE.txt').read().split()[0]


@app.route('/', methods=['GET'])
def fetchdata_giosg_api():

            #API call number 1 'GET' total_conversation_count, total_user_message_count and total_visitor_message_count
            try:
                start_date = '2017-05-01'
                end_date = '2017-06-15'
                api_url = "https://api.giosg.com/api/reporting/v1/rooms/84e0fefa-5675-11e7-a349-00163efdd8db/chat-stats/daily/?start_date=" + \
                    start_date+"&end_date="+end_date
                header = {'Authorization': 'Bearer {0}'.format(access_token)}

                response = requests.get(url=api_url, headers=header)
                data = response.json()

                total_conversation_count = data["total_conversation_count"]
                total_user_message_count = data["total_user_message_count"]
                total_visitor_message_count = data["total_visitor_message_count"]

                #API call number 2 'GET' daily numbers
                if(response != 'null'):
                    try:
                       response_bydate = requests.get(
                           url=api_url, headers=header)
                       data_incoming = response_bydate.json()
                       #daily numbers data
                       daily_numbers = data_incoming['by_date']

                       #Pagination
                       page = request.args.get('page')
                       if(not str(page).isnumeric()):
                                                  page = 1

                       size_per_page = 5
                       page = int(page)
                       lastpage = math.ceil(len(daily_numbers)/size_per_page)
                       #slicing daily_numbers data to 5 items per page
                       daily_numbers = daily_numbers[(
                           page-1)*size_per_page: (page-1)*size_per_page+size_per_page]

                       if(page == 1):
                              prev = "#"
                              next = "/?page="+str(page+1)
                       elif(page == lastpage):
                              prev = "/?page="+str(page-1)
                              next = "#"
                       else:
                              prev = "/?page="+str(page-1)
                              next = "/?page=" + str(page + 1)

                    except:
                            daily_numbers = 'error 404 - Giosg API not working'
                            prev = '#'
                            next = '#'

            except:
                total_conversation_count = 'error 404 - Giosg API not working'
                total_user_message_count = 'error 404 - Giosg API not working'
                total_visitor_message_count = 'error 404 - Giosg API not working'
                daily_numbers = 'error 404 - Giosg API not working'
                prev = '#'
                next = '#'

            return render_template('homepage.html', total_conversation_count=total_conversation_count,
                                   total_user_message_count=total_user_message_count,
                                   total_visitor_message_count=total_visitor_message_count,
                                   daily_numbers=daily_numbers,
                                   access_token=access_token,
                                   start_date=start_date,
                                   end_date=end_date,
                                   prev=prev,
                                   next=next)
