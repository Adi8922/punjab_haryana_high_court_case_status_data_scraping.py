import requests
from bs4 import BeautifulSoup


final_list = []
final_dict_result = {}
session = requests.session()
url = "https://phhc.gov.in/home.php?search_param=case"
Headers1 = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "en-US,en;q=0.5",
        "Connection" : "keep-alive",
        "Content-Type" : "application/x-www-form-urlencoded",
        "Host" : "phhc.gov.in",
        "Origin" : "https://phhc.gov.in",
        "Referer" : "https://phhc.gov.in/home.php?search_param=case",
        "Sec-Fetch-Dest" : "document",
        "Sec-Fetch-Mode" : "navigate",
        "Sec-Fetch-Site" : "same-origin",
        "Sec-Fetch-User" : "?1",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
    }
res = session.get(url ,verify = False)
content = res.content
soup = BeautifulSoup(content , "lxml")
class_data = soup.find("select",{"id":"t_case_type"})

case_index = int(input("Enter only index number : "))
case_number = int(input("Enter only case number : "))
case_year = int(input("Enter only case year : "))
# print(class_data)


for count, z in enumerate(class_data):
    # print(z)
    case_types =[]
    case_type ={}
    case_name = z.text.strip()
    case_submit_value = z["value"]
    case_type ={
      "index" : count+1,
      "case_name": case_name,
      "case_submit_value" : case_submit_value
        }
    if case_index == case_type['index']:
        sub_val = case_type['case_submit_value']
        payload = {
            "t_case_type" : str(sub_val),
            "t_case_no" : str(case_number),
            "t_case_year" : str(case_year),
            "submit" : "Search+Case"
            }
        # print(payload)
        response = session.post(url ,headers=Headers1, data=payload, verify = False)
        content = response.content
        soup1 = BeautifulSoup(content ,"lxml")
        break
    else:
        print("Case details not in this case ID ")
        
details = soup1.find_all("tr",{"class":"alt"})
find_details = details[0]
# print(find_details)
data_details = find_details.find_all("td")
case_id = data_details[0].text
petition_name = data_details[1].text
respondent_name = data_details[2].text
advocate_name = data_details[3].text
status = data_details[4].text
next_date = data_details[5].text
final_dict_result["Case ID"] = case_id
final_dict_result["Petition Name"] = petition_name
final_dict_result["Respondent Name"] = respondent_name
final_dict_result["Advocate Name"] = advocate_name
final_dict_result["Status"] = status
final_dict_result["Next Date"] = next_date
final_list.append(final_dict_result)
print(final_list)
    