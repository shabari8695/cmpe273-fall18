import requests
from multiprocessing import Pool
import time

number_of_pings = 25
file_name = "output.txt"
file_argument = 'a'

output = open(file_name,file_argument)
output.write("......Async Call......\n")

def pingQuery(id):
    #print("Query : "+str(id))
    #time.sleep(1)
    response = requests.get("https://webhook.site/#/")
    return "id : "+str(id)+" "+response.headers.get('Date')

result_list = []
def log_result(result):
    # This is called whenever pingQuery returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

pool = Pool()
for i in range(0,number_of_pings):
    pool.apply_async(pingQuery,args = (i, ), callback = log_result)

pool.close()
pool.join()

for result in result_list:
    print(result)
    output.write(result+"\n")

output.close()

