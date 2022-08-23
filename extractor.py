from bs4 import BeautifulSoup
from get_date import checking_dates
import requests

date = checking_dates()



print(f"We are checking for the date {date}")

response = requests.get("https://www.billboard.com/charts/hot-100/" + str(date))


# for checking whether we got the response or not
if len(response.text) >0:
    print(f"we got the response value - {len(response.text)}")
    soup = BeautifulSoup(response.text, 'html.parser')
    # song_names = soup.find_all("span", class_="chart-element__information__song")
    titles = soup.select(selector="div li ul li h3")
    title_list = []
    for i in titles:
        title_list.append(i.getText().strip())
    # print(len(title_list))
    if len(title_list) == 0:
        print("No list found")
    else:
        # print(title_list)
    
        songs_dict = {}
        
        for i in enumerate(title_list, 1):
            songs_dict[str(i[0])] = i[1]
        print(songs_dict)





    
    





