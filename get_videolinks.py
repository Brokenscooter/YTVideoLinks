import urllib.request 
import json
import pandas as pd

channel_id='CHANNELID'


def get_all_video_in_channel(channel_id):
    api_key ='APIKEY'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links
	
channel_id='CHANNELID'

array=get_all_video_in_channel(channel_id)


#save links to an excel file
pd.DataFrame(array).to_excel(r'<path to xlsx file', header=False, index=False)