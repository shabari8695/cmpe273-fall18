import requests

number_of_pings = 3
file_name = "output.txt"
file_argument = 'a'

output = open(file_name,file_argument)
output.write("......Sync Call......\n")

for i in range(0,number_of_pings):
    response = requests.get("https://webhook.site/#/")
    #print(response.status_code == requests.codes.ok)
    #print(response.headers.get('Date'))
    output.write(response.headers.get('Date')+"\n")

output.close()