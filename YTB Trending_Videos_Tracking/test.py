import os
import re
import pandas as pd
import numpy as np
from googleapiclient.discovery import build
import datetime
import time

api_keys = 'AIzaSyCORgFgWCwj0VyLo5Erd8Z6od7LwNYxWXQ'
youtube = build('youtube', 'v3', developerKey=api_keys)

# start time
t1 = datetime.datetime.now()
print("now >> {}".format(t1))
year = str(time.strftime('%Y', time.localtime()))
month = str(time.strftime('%m', time.localtime()))
day = str(time.strftime('%d', time.localtime()))
t = [year,month,day]

#%%
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

# request
request1 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "US",
    maxResults = 200
)
request2 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "CA",
    maxResults = 200
)
request3 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "BR",
    maxResults = 200
)
request4 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "DE",
    maxResults = 200
)
request5 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "GB",
    maxResults = 200
)
request6 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "IN",
    maxResults = 200
)
request7 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "JP",
    maxResults = 200
)
request8 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "KR",
    maxResults = 200
)
request9 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "MX",
    maxResults = 200
)
request10 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "RU",
    maxResults = 200
)
request11 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "SG",
    maxResults = 200
)
request12 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "HK",
    maxResults = 200
)
request13 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "TW",
    maxResults = 200
)
request14 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "ZA",
    maxResults = 200
)
request15= youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "ES",
    maxResults = 200
)
request16 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "FR",
    maxResults = 200
)
request17 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "IE",
    maxResults = 200
)
request18 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "IT",
    maxResults = 200
)
request19 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "PL",
    maxResults = 200
)
request20 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "NL",
    maxResults = 200
)
request21 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "AU",
    maxResults = 200
)
request22 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "NZ",
    maxResults = 200
)
request23 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "CZ",
    maxResults = 200
)
request24 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "IL",
    maxResults = 200
)
request25 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "SE",
    maxResults = 200
)
request26 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "SA",
    maxResults = 200
)
request27 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "KE",
    maxResults = 200
)
request28 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "PH",
    maxResults = 200
)
request29 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "BE",
    maxResults = 200
)
request30 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "CO",
    maxResults = 200
)
request31 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "UG",
    maxResults = 200
)
request32 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "CL",
    maxResults = 200
)
request33 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "HU",
    maxResults = 200
)
request34 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "MY",
    maxResults = 200
)
request35 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "PE",
    maxResults = 200
)
request36 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "AE",
    maxResults = 200
)
request37 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "GR",
    maxResults = 200
)
request38 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "ID",
    maxResults = 200
)
request39 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "GH",
    maxResults = 200
)
request40 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "SN",
    maxResults = 200
)
request41 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "TR",
    maxResults = 200
)
request42 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "UA",
    maxResults = 200
)
request43 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "DK",
    maxResults = 200
)
request44 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "FL",
    maxResults = 200
)
request45 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "NO",
    maxResults = 200
)
request46 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "CH",
    maxResults = 200
)
request47 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "AT",
    maxResults = 200
)
request48 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "RO",
    maxResults = 200
)
request49 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "PT",
    maxResults = 200
)
request50 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "SK",
    maxResults = 200
)
request51 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "KW",
    maxResults = 200
)
request52 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "BA",
    maxResults = 200
)
request53 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "BG",
    maxResults = 200
)
request54 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "EE",
    maxResults = 200
)
request55 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "HR",
    maxResults = 200
)
request56 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "LT",
    maxResults = 200
)
request57 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "ME",
    maxResults = 200
)
request58 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "MK",
    maxResults = 200
)
request59 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "RS",
    maxResults = 200
)
request60 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "SI",
    maxResults = 200
)
request61 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "TH",
    maxResults = 200
)
request62 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "LB",
    maxResults = 200
)
request63 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "PR",
    maxResults = 200
)
request64 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "IS",
    maxResults = 200)
request65 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "LU",
    maxResults = 200)
request66 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "VN",
    maxResults = 200)
request67 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "LY",
    maxResults = 200)
request68 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "TZ",
    maxResults = 200
)
request69 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "ZW",
    maxResults = 200
)
request70 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "AZ",
    maxResults = 200
)
request71 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "BL",
    maxResults = 200
)
request72 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "GE",
    maxResults = 200
)
request73 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "KA",
    maxResults = 200
)
request74 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "NE",
    maxResults = 200
)
request75 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "PA",
    maxResults = 200
)
request76 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "LK",
    maxResults = 200
)
request77 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "IR",
    maxResults = 200
)
request78 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "JA",
    maxResults = 200
)
request79 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "DZ",
    maxResults = 200
)
request80 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "EG",
    maxResults = 200
)
request81 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "TN",
    maxResults = 200
)
request82 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "JO",
    maxResults = 200
)
request83 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "MA",
    maxResults = 200
)
request84 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "YE",
    maxResults = 200
)
request85 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "BH",
    maxResults = 200
)
request86 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "OM",
    maxResults = 200
)
request87 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "QA",
    maxResults = 200
)
request88 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "IE",
    maxResults = 200
)
request89 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "KL",
    maxResults = 200
)
request90 = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode= "LV",
    maxResults = 200
)

# response
# NO DATA FOR {44:FL(芬兰),71:BL(白俄罗斯),
              #73:KA(哈萨克斯坦),74:NE(尼泊尔),
              #77:IR(伊拉克),78:JA(牙买加),89:KL(苏格兰)}
response1 = request1.execute()
response2 = request2.execute()
response3 = request3.execute()
response4 = request4.execute()
response5 = request5.execute()
response6 = request6.execute()
response7 = request7.execute()
response8 = request8.execute()
response9 = request9.execute()
response10 = request10.execute()
response11 = request11.execute()
response12 = request12.execute()
response13 = request13.execute()
response14 = request14.execute()
response15 = request15.execute()
response16 = request16.execute()
response17 = request17.execute()
response18 = request18.execute()
response19 = request19.execute()
response20 = request20.execute()
response21 = request21.execute()
response22 = request22.execute()
response23 = request23.execute()
response24 = request24.execute()
response25 = request25.execute()
response26 = request26.execute()
response27 = request27.execute()
response28 = request28.execute()
response29 = request29.execute()
response30 = request30.execute()
response31 = request31.execute()
response32 = request32.execute()
response33 = request33.execute()
response34 = request34.execute()
response35 = request35.execute()
response36 = request36.execute()
response37 = request37.execute()
response38 = request38.execute()
response39 = request39.execute()
response40 = request40.execute()
response41 = request41.execute()
response42 = request42.execute()
response43 = request43.execute()
# response44 = request44.execute()
response45 = request45.execute()
response46 = request46.execute()
response47 = request47.execute()
response48 = request48.execute()
response49 = request49.execute()
response50 = request50.execute()
response51 = request51.execute()
response52 = request52.execute()
response53 = request53.execute()
response54 = request54.execute()
response55 = request55.execute()
response56 = request56.execute()
response57 = request57.execute()
response58 = request58.execute()
response59 = request59.execute()
response60 = request60.execute()
response61 = request61.execute()
response62 = request62.execute()
response63 = request63.execute()
response64 = request64.execute()
response65 = request65.execute()
response66 = request66.execute()
response67 = request67.execute()
response68 = request68.execute()
response69 = request69.execute()
response70 = request70.execute()
# response71 = request71.execute()
response72 = request72.execute()
# response73 = request73.execute()
# response74 = request74.execute()
response75 = request75.execute()
response76 = request76.execute()
# response77 = request77.execute()
# response78 = request78.execute()
response79 = request79.execute()
response80 = request80.execute()
response81 = request81.execute()
response82 = request82.execute()
response83 = request83.execute()
response84 = request84.execute()
response85 = request85.execute()
response86 = request86.execute()
response87 = request87.execute()
response88 = request88.execute()
# response89 = request89.execute()
response90 = request90.execute()

# 1.US
# vid_url
vid_ids1 = []
for item in response1['items']:
    vid_ids1.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids1)
)
vid_response = vid_request.execute()
vid_id1 = []
for item in vid_response['items']:
        vid_id = item['id']
        yt_link = f'https://youtu.be/{vid_id}'
        vid_id1.append(yt_link)
# other items
for item in response1['items']:
        vid_title = []
        for item in response1['items']:
            vid_title.append(item['snippet']['title'])

        vid_publishedAt = []
        for item in response1['items']:
            vid_publishedAt.append(item['snippet']['publishedAt'])

        vid_channeltitle = []
        for item in response1['items']:
            vid_channeltitle.append(item['snippet']['channelTitle'])

        vid_viewCount = []
        for item in response1['items']:
            vid_viewCount.append(item['statistics']['viewCount'])

        # vid_likeCount = []
        # for item in response1['items']:
        #     vid_likeCount.append(item['statistics']['likeCount'])

        # vid_commentCount = []
        # for item in response1['items']:
        #     vid_commentCount.append(item['statistics']['commentCount'])

        vid_channelId = []
        for item in response1['items']:
            vid_channelId.append(item['snippet']['channelId'])

        vid_categoryId = []
        for item in response1['items']:
            vid_categoryId.append(item['snippet']['categoryId'])

        # vid_tags = []
        # for item in response1['items']:
        #     vid_tags.append(item['snippet']['tags'])

        vid_duration = []
        for item in response1['items']:
            duration = item['contentDetails']['duration']
            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = seconds_pattern.search(duration)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0

            duration2 = f'{hours}:{minutes}:{seconds}'
            vid_duration.append(duration2)

        dict1 = {'地区': 'US(美国)', 'URL': vid_id1, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration,
                 '浏览量': vid_viewCount,'频道标题': vid_channeltitle, '频道ID': vid_channelId, '分类ID': vid_categoryId}
df1 = pd.DataFrame(dict1)

# 2.CA
# vid_url
vid_ids2 = []
for item in response2['items']:
    vid_ids2.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids2)
)
vid_response = vid_request.execute()
vid_id2 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id2.append(yt_link)
# other items
for item in response2['items']:

    vid_title = []
    for item in response2['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response2['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response2['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response2['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response2['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response2['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response2['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response2['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response2['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict2 = {'地区': 'CA(加拿大)', 'URL': vid_id2, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId, '分类ID': vid_categoryId}
df2 = pd.DataFrame(dict2)
df = pd.concat([df1,df2])

# 3.BR
# vid_url
vid_ids3 = []
for item in response3['items']:
    vid_ids3.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids3)
)
vid_response = vid_request.execute()
vid_id3 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id3.append(yt_link)
# other items
for item in response3['items']:

    vid_title = []
    for item in response3['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response3['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response3['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response3['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response3['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response3['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response3['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response3['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response3['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict3 = {'地区': 'BR(巴西)', 'URL': vid_id3, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
            '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df3 = pd.DataFrame(dict3)
df = pd.concat([df,df3])

# 4.DE
# vid_url
vid_ids4 = []
for item in response4['items']:
    vid_ids4.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids4)
)
vid_response = vid_request.execute()
vid_id4 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id4.append(yt_link)
# other items
for item in response4['items']:

    vid_title = []
    for item in response4['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response4['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response4['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response4['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response4['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response4['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response4['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response4['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response4['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict4 = {'地区': 'DE(德国)', 'URL': vid_id4, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df4 = pd.DataFrame(dict4)
df = pd.concat([df,df4])

# 5.GB
# vid_url
vid_ids5 = []
for item in response5['items']:
    vid_ids5.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids5)
)
vid_response = vid_request.execute()
vid_id5 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id5.append(yt_link)
# other items
for item in response5['items']:

    vid_title = []
    for item in response5['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response5['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response5['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response5['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response5['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response5['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response5['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response5['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response5['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict5 = {'地区': 'GB(英国)', 'URL': vid_id5, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df5 = pd.DataFrame(dict5)
df = pd.concat([df,df5])

# 6.IN
# vid_url
vid_ids6 = []
for item in response6['items']:
    vid_ids6.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids6)
)
vid_response = vid_request.execute()
vid_id6 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id6.append(yt_link)
# other items
for item in response6['items']:

    vid_title = []
    for item in response6['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response6['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response6['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response6['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response6['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response6['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response6['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response6['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response6['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict6 = {'地区': 'IN(印度)', 'URL': vid_id6, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df6 = pd.DataFrame(dict6)
df = pd.concat([df,df6])

# 7.JB
# vid_url
vid_ids7 = []
for item in response7['items']:
    vid_ids7.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids7)
)
vid_response = vid_request.execute()
vid_id7 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id7.append(yt_link)
# other items
for item in response7['items']:

    vid_title = []
    for item in response7['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response7['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response7['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response7['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response7['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response7['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response7['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response7['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response7['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict7 = {'地区': 'JP(日本)', 'URL': vid_id7, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df7 = pd.DataFrame(dict7)
df = pd.concat([df,df7])

# 8.KR
# vid_url
vid_ids8 = []
for item in response8['items']:
    vid_ids8.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids8)
)
vid_response = vid_request.execute()
vid_id8 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id8.append(yt_link)
# other items
for item in response8['items']:

    vid_title = []
    for item in response8['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response8['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response8['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response8['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response8['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response8['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response8['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response8['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response8['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict8 = {'地区': 'KR(韩国)', 'URL': vid_id8, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df8 = pd.DataFrame(dict8)
df = pd.concat([df,df8])

# 9.MX
# vid_url
vid_ids9 = []
for item in response9['items']:
    vid_ids9.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids9)
)
vid_response = vid_request.execute()
vid_id9 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id9.append(yt_link)
# other items
for item in response9['items']:

    vid_title = []
    for item in response9['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response9['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response9['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response9['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response9['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response9['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response9['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response9['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response9['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict9 = {'地区': 'MX(墨西哥)', 'URL': vid_id9 ,'视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df9 = pd.DataFrame(dict9)
df = pd.concat([df,df9])

# 10.RU
# vid_url
vid_ids10 = []
for item in response10['items']:
    vid_ids10.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids10)
)
vid_response = vid_request.execute()
vid_id10 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id10.append(yt_link)
# other items
for item in response10['items']:

    vid_title = []
    for item in response10['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response10['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response10['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response10['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response10['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response10['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response10['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response10['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response10['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict10 = {'地区': 'RU(俄罗斯)', 'URL': vid_id10, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df10 = pd.DataFrame(dict10)
df = pd.concat([df,df10])

# 11.SG
# vid_url
vid_ids11 = []
for item in response11['items']:
    vid_ids11.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids11)
)
vid_response = vid_request.execute()
vid_id11 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id11.append(yt_link)
# other items
for item in response11['items']:

    vid_title = []
    for item in response11['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response11['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response11['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response11['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response11['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response11['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response11['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response11['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response11['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict11 = {'地区': 'SG(新加坡)', 'URL': vid_id11,'视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df11 = pd.DataFrame(dict11)
df = pd.concat([df,df11])

# 12.HK
# vid_url
vid_ids12 = []
for item in response12['items']:
    vid_ids12.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids12)
)
vid_response = vid_request.execute()
vid_id12 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id12.append(yt_link)
# other items
for item in response12['items']:

    vid_title = []
    for item in response12['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response12['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response12['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response12['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response12['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response12['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response12['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response12['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response12['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict12 = {'地区': 'HK(香港)', 'URL': vid_id12, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df12 = pd.DataFrame(dict12)
df = pd.concat([df,df12])

# 13.TW
# vid_url
vid_ids13 = []
for item in response13['items']:
    vid_ids13.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids13)
)
vid_response = vid_request.execute()
vid_id13 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id13.append(yt_link)
# other items
for item in response13['items']:

    vid_title = []
    for item in response13['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response13['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response13['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response13['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response13['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # # vid_commentCount = []
    # for item in response13['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response13['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response13['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response13['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict13 = {'地区': 'TW(台湾)', 'URL': vid_id13, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df13 = pd.DataFrame(dict13)
df = pd.concat([df,df13])

# 14.ZA
# vid_url
vid_ids14 = []
for item in response14['items']:
    vid_ids14.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids14)
)
vid_response = vid_request.execute()
vid_id14 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id14.append(yt_link)
# other items
for item in response14['items']:

    vid_title = []
    for item in response14['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response14['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response14['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response14['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response14['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response14['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response14['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response14['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response14['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict14 = {'地区': 'ZA(南非)', 'URL': vid_id14, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df14 = pd.DataFrame(dict14)
df = pd.concat([df,df14])

# 15.ES
# vid_url
vid_ids15 = []
for item in response15['items']:
    vid_ids15.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids15)
)
vid_response = vid_request.execute()
vid_id15 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id15.append(yt_link)
# other items
for item in response15['items']:

    vid_title = []
    for item in response15['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response15['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response15['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response15['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response15['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response15['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response15['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response15['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response15['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict15 = {'地区': 'ES(西班牙)', 'URL': vid_id15, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df15 = pd.DataFrame(dict15)
df = pd.concat([df,df15])

# 16.FR
# vid_url
vid_ids16 = []
for item in response16['items']:
    vid_ids16.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids16)
)
vid_response = vid_request.execute()
vid_id16 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id16.append(yt_link)
# other items
for item in response16['items']:

    vid_title = []
    for item in response16['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response16['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response16['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response16['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response16['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response16['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response16['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response16['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response16['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict16 = {'地区': 'FR(法国)', 'URL': vid_id16, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df16 = pd.DataFrame(dict16)
df = pd.concat([df,df16])

# 17.IE
# vid_url
vid_ids17 = []
for item in response17['items']:
    vid_ids17.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids17)
)
vid_response = vid_request.execute()
vid_id17 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id17.append(yt_link)
# other items
for item in response17['items']:

    vid_title = []
    for item in response17['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response17['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response17['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response17['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response17['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response17['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response17['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response17['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response17['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict17 = {'地区': 'IE(爱尔兰)', 'URL': vid_id17, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df17 = pd.DataFrame(dict17)
df = pd.concat([df,df17])

# 18.IT
# vid_url
vid_ids18 = []
for item in response18['items']:
    vid_ids18.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids18)
)
vid_response = vid_request.execute()
vid_id18 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id18.append(yt_link)
# other items
for item in response18['items']:

    vid_title = []
    for item in response18['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response18['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response18['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response18['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response18['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response18['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response18['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response18['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response18['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict18 = {'地区': 'IT(意大利)', 'URL': vid_id18, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df18 = pd.DataFrame(dict18)
df = pd.concat([df,df18])

# 19.PL
# vid_url
vid_ids19 = []
for item in response19['items']:
    vid_ids19.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids19)
)
vid_response = vid_request.execute()
vid_id19 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id19.append(yt_link)
# other items
for item in response19['items']:

    vid_title = []
    for item in response19['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response19['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response19['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response19['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response19['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response19['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response19['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response19['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response19['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict19 = {'地区': 'PL(波兰)', 'URL': vid_id19, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df19 = pd.DataFrame(dict19)
df = pd.concat([df,df19])

# 20.NL
# vid_url
vid_ids20 = []
for item in response20['items']:
    vid_ids20.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids20)
)
vid_response = vid_request.execute()
vid_id20 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id20.append(yt_link)
# other items
for item in response20['items']:

    vid_title = []
    for item in response20['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response20['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response20['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response20['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response20['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response20['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response20['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response20['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response20['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict20 = {'地区': 'NL(尼日利亚)', 'URL': vid_id20, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df20 = pd.DataFrame(dict20)
df = pd.concat([df,df20])

# 21.AU
# vid_url
vid_ids21 = []
for item in response21['items']:
    vid_ids21.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids21)
)
vid_response = vid_request.execute()
vid_id21 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id21.append(yt_link)
# other items
for item in response21['items']:

    vid_title = []
    for item in response21['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response21['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response21['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response21['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response21['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response21['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response21['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response21['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response21['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict21 = {'地区': 'AU(澳大利亚)', 'URL': vid_id21, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df21 = pd.DataFrame(dict21)
df = pd.concat([df,df21])

# 22.NZ
# vid_url
vid_ids22 = []
for item in response22['items']:
    vid_ids22.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids22)
)
vid_response = vid_request.execute()
vid_id22 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id22.append(yt_link)
# other items
for item in response22['items']:

    vid_title = []
    for item in response22['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response22['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response22['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response22['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response22['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response22['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response22['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response22['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response22['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict22 = {'地区': 'NZ(新西兰)', 'URL': vid_id22, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df22 = pd.DataFrame(dict22)
df = pd.concat([df,df22])

# 23.CZ
# vid_url
vid_ids23 = []
for item in response23['items']:
    vid_ids23.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids23)
)
vid_response = vid_request.execute()
vid_id23 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id23.append(yt_link)
# other items
for item in response23['items']:

    vid_title = []
    for item in response23['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response23['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response23['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response23['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response23['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response23['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response23['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response23['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response23['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict23 = {'地区': 'CZ(捷克)', 'URL': vid_id23, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df23 = pd.DataFrame(dict23)
df = pd.concat([df,df23])

# 24.IL
# vid_url
vid_ids24 = []
for item in response2['items']:
    vid_ids24.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids24)
)
vid_response = vid_request.execute()
vid_id24 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id24.append(yt_link)
# other items
for item in response24['items']:

    vid_title = []
    for item in response24['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response24['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response24['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response24['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response24['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response24['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response24['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response24['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response24['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict24 = {'地区': 'IL(以色列)', 'URL': vid_id24, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df24 = pd.DataFrame(dict24)
df = pd.concat([df,df24])

# 25.SE
# vid_url
vid_ids25 = []
for item in response25['items']:
    vid_ids25.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids25)
)
vid_response = vid_request.execute()
vid_id25 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id25.append(yt_link)
# other items
for item in response25['items']:

    vid_title = []
    for item in response25['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response25['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response25['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response25['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response25['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response25['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response25['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response25['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response25['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict25 = {'地区': 'SE(瑞典)', 'URL': vid_id25, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df25 = pd.DataFrame(dict25)
df = pd.concat([df,df25])

# 26.SA
# vid_url
vid_ids26 = []
for item in response26['items']:
    vid_ids26.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids26)
)
vid_response = vid_request.execute()
vid_id26 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id26.append(yt_link)
# other items
for item in response26['items']:

    vid_title = []
    for item in response26['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response26['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response26['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response26['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response26['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response26['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response26['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response26['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response26['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict26 = {'地区': 'SA(沙特阿拉伯)', 'URL': vid_id26, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df26 = pd.DataFrame(dict26)
df = pd.concat([df,df26])

# 27.KE
# vid_url
vid_ids27 = []
for item in response27['items']:
    vid_ids27.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids27)
)
vid_response = vid_request.execute()
vid_id27 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id27.append(yt_link)
# other items
for item in response27['items']:

    vid_title = []
    for item in response27['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response27['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response27['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response27['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response27['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response27['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response27['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response27['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response27['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict27 = {'地区': 'KE(肯尼亚)', 'URL': vid_id27, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df27 = pd.DataFrame(dict27)
df = pd.concat([df,df27])

# 28.PH
# vid_url
vid_ids28 = []
for item in response28['items']:
    vid_ids28.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids28)
)
vid_response = vid_request.execute()
vid_id28 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id28.append(yt_link)
# other items
for item in response28['items']:

    vid_title = []
    for item in response28['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response28['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response28['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response28['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response28['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response28['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response28['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response28['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response28['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict28 = {'地区': 'PH(菲律宾)', 'URL': vid_id28, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df28 = pd.DataFrame(dict28)
df = pd.concat([df,df28])

# 29.BE
# vid_url
vid_ids29 = []
for item in response29['items']:
    vid_ids29.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids29)
)
vid_response = vid_request.execute()
vid_id29 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id29.append(yt_link)
# other items
for item in response29['items']:

    vid_title = []
    for item in response29['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response29['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response29['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response29['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response29['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response29['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response29['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response29['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response29['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict29 = {'地区': 'BE(比利时)', 'URL': vid_id29, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df29 = pd.DataFrame(dict29)
df = pd.concat([df,df29])

# 30.CO
# vid_url
vid_ids30 = []
for item in response30['items']:
    vid_ids30.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids30)
)
vid_response = vid_request.execute()
vid_id30 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id30.append(yt_link)
# other items
for item in response30['items']:

    vid_title = []
    for item in response30['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response30['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response30['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response30['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response30['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response30['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response30['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response30['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response30['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict30 = {'地区': 'CO(哥伦比亚)', 'URL': vid_id30, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df30 = pd.DataFrame(dict30)
df = pd.concat([df,df30])

# 31.UG
# vid_url
vid_ids31 = []
for item in response31['items']:
    vid_ids31.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids31)
)
vid_response = vid_request.execute()
vid_id31 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id31.append(yt_link)
# other items
for item in response31['items']:

    vid_title = []
    for item in response31['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response31['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response31['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response31['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response31['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response31['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response31['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response31['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response31['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict31 = {'地区': 'UG(乌干达)', 'URL': vid_id31, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df31 = pd.DataFrame(dict31)
df = pd.concat([df,df31])

# 32.CL
# vid_url
vid_ids32 = []
for item in response32['items']:
    vid_ids32.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids32)
)
vid_response = vid_request.execute()
vid_id32 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id32.append(yt_link)
# other items
for item in response32['items']:

    vid_title = []
    for item in response32['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response32['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response32['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response32['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response32['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response32['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response32['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response32['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response32['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict32 = {'地区': 'CL(智利)', 'URL': vid_id32, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df32 = pd.DataFrame(dict32)
df = pd.concat([df,df32])

# 33.HU
# vid_url
vid_ids33 = []
for item in response33['items']:
    vid_ids33.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids33)
)
vid_response = vid_request.execute()
vid_id33 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id33.append(yt_link)
# other items
for item in response33['items']:

    vid_title = []
    for item in response33['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response33['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response33['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response33['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response33['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response33['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response33['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response33['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response33['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict33 = {'地区': 'HU(匈牙利)', 'URL': vid_id33, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df33 = pd.DataFrame(dict33)
df = pd.concat([df,df33])

# 34.MY
# vid_url
vid_ids34 = []
for item in response34['items']:
    vid_ids34.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids34)
)
vid_response = vid_request.execute()
vid_id34 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id34.append(yt_link)
# other items
for item in response34['items']:

    vid_title = []
    for item in response34['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response34['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response34['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response34['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response34['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response34['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response34['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response34['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response34['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict34 = {'地区': 'MY(马来西亚)', 'URL': vid_id34, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df34 = pd.DataFrame(dict34)
df = pd.concat([df,df34])

# 35.PE
# vid_url
vid_ids35 = []
for item in response35['items']:
    vid_ids35.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids35)
)
vid_response = vid_request.execute()
vid_id35 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id35.append(yt_link)
# other items
for item in response35['items']:

    vid_title = []
    for item in response35['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response35['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response35['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response35['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response35['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response35['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response35['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response35['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response35['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict35 = {'地区': 'PE(秘鲁)', 'URL': vid_id35, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df35 = pd.DataFrame(dict35)
df = pd.concat([df,df35])

# 36.AE
# vid_url
vid_ids36 = []
for item in response36['items']:
    vid_ids36.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids36)
)
vid_response = vid_request.execute()
vid_id36 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id36.append(yt_link)
# other items
for item in response36['items']:

    vid_title = []
    for item in response36['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response36['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response36['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response36['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response36['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response36['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response36['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response36['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response36['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict36 = {'地区': 'AE(阿联酋)', 'URL': vid_id36, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df36 = pd.DataFrame(dict36)
df = pd.concat([df,df36])

# 37.GR
# vid_url
vid_ids37 = []
for item in response37['items']:
    vid_ids37.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids37)
)
vid_response = vid_request.execute()
vid_id37 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id37.append(yt_link)
# other items
for item in response37['items']:

    vid_title = []
    for item in response37['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response37['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response37['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response37['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response37['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response37['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response37['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response37['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response37['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict37 = {'地区': 'GR(希腊)', 'URL': vid_id37, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df37 = pd.DataFrame(dict37)
df = pd.concat([df,df37])

# 38.ID
# vid_url
vid_ids38 = []
for item in response38['items']:
    vid_ids38.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids38)
)
vid_response = vid_request.execute()
vid_id38 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id38.append(yt_link)
# other items
for item in response38['items']:

    vid_title = []
    for item in response38['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response38['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response38['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response38['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response38['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response38['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response38['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response38['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response38['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict38 = {'地区': 'ID(印度尼西亚)', 'URL': vid_id38, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df38 = pd.DataFrame(dict38)
df = pd.concat([df,df38])

# 39.GH
# vid_url
vid_ids39 = []
for item in response39['items']:
    vid_ids39.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids39)
)
vid_response = vid_request.execute()
vid_id39 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id39.append(yt_link)
# other items
for item in response39['items']:

    vid_title = []
    for item in response39['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response39['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response39['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response39['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response39['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response39['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response39['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response39['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response39['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict39 = {'地区': 'GH(加纳)', 'URL': vid_id39, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df39 = pd.DataFrame(dict39)
df = pd.concat([df,df39])

# 40.SN
# vid_url
vid_ids40 = []
for item in response40['items']:
    vid_ids40.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids40)
)
vid_response = vid_request.execute()
vid_id40 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id40.append(yt_link)
# other items
for item in response40['items']:

    vid_title = []
    for item in response40['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response40['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response40['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response40['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response40['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response40['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response40['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response40['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response40['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict40 = {'地区': 'SN(塞内加尔)', 'URL': vid_id40, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df40 = pd.DataFrame(dict40)
df = pd.concat([df,df40])

# 41.TR
# vid_url
vid_ids41 = []
for item in response41['items']:
    vid_ids41.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids41)
)
vid_response = vid_request.execute()
vid_id41 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id41.append(yt_link)
# other items
for item in response41['items']:

    vid_title = []
    for item in response41['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response41['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response41['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response41['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response41['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response41['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response41['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response41['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response41['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict41 = {'地区': 'TR(土耳其)', 'URL': vid_id41, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df41 = pd.DataFrame(dict41)
df = pd.concat([df,df41])

# 42.UA
# vid_url
vid_ids42 = []
for item in response42['items']:
    vid_ids42.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids42)
)
vid_response = vid_request.execute()
vid_id42 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id42.append(yt_link)
# other items
for item in response42['items']:

    vid_title = []
    for item in response42['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response42['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response42['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response42['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response42['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response42['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response42['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response42['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response42['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict42 = {'地区': 'UA(乌克兰)', 'URL': vid_id42, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df42 = pd.DataFrame(dict42)
df = pd.concat([df,df42])

# 43.DK
# vid_url
vid_ids43 = []
for item in response43['items']:
    vid_ids43.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids43)
)
vid_response = vid_request.execute()
vid_id43 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id43.append(yt_link)
# other items
for item in response43['items']:

    vid_title = []
    for item in response43['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response43['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response43['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response43['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response43['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response43['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response43['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response43['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response43['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict43 = {'地区': 'DK(丹麦)', 'URL': vid_id43, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df43 = pd.DataFrame(dict43)
df = pd.concat([df,df43])

# # 44.FL
# # vid_url
# vid_ids44 = []
# for item in response44['items']:
#     vid_ids44.append(item['id'])
# vid_request = youtube.videos().list(
#     part="statistics",
#     id=','.join(vid_ids44)
# )
# vid_response = vid_request.execute()
# vid_id44 = []
# for item in vid_response['items']:
#     vid_id = item['id']
#     yt_link = f'https://youtu.be/{vid_id}'
#     vid_id44.append(yt_link)
# # other items
# for item in response44['items']:
#
#     vid_title = []
#     for item in response44['items']:
#         vid_title.append(item['snippet']['title'])
#
#     vid_publishedAt = []
#     for item in response44['items']:
#         vid_publishedAt.append(item['snippet']['publishedAt'])
#
#     vid_channeltitle = []
#     for item in response44['items']:
#         vid_channeltitle.append(item['snippet']['channelTitle'])
#
#     vid_viewCount = []
#     for item in response44['items']:
#         vid_viewCount.append(item['statistics']['viewCount'])
#
#     # vid_likeCount = []
#     # for item in response44['items']:
#     #     vid_likeCount.append(item['statistics']['likeCount'])
#
#     # vid_commentCount = []
#     # for item in response44['items']:
#     #     vid_commentCount.append(item['statistics']['commentCount'])
#
#     vid_channelId = []
#     for item in response44['items']:
#         vid_channelId.append(item['snippet']['channelId'])
#
#     vid_categoryId = []
#     for item in response44['items']:
#         vid_categoryId.append(item['snippet']['categoryId'])
#
#     vid_duration = []
#     for item in response44['items']:
#
#         duration = item['contentDetails']['duration']
#         hours = hours_pattern.search(duration)
#         minutes = minutes_pattern.search(duration)
#         seconds = seconds_pattern.search(duration)
#
#         hours = int(hours.group(1)) if hours else 0
#         minutes = int(minutes.group(1)) if minutes else 0
#         seconds = int(seconds.group(1)) if seconds else 0
#
#         duration2 = f'{hours}:{minutes}:{seconds}'
#         vid_duration.append(duration2)
#
#     dict44 = {'地区': 'FL(芬兰)', 'URL': vid_id44, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
#              '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
# df44 = pd.DataFrame(dict44)
# df = pd.concat([df,df44])

# 45.NO
# vid_url
vid_ids45 = []
for item in response25['items']:
    vid_ids45.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids45)
)
vid_response = vid_request.execute()
vid_id45 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id45.append(yt_link)
# other items
for item in response45['items']:

    vid_title = []
    for item in response45['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response45['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response45['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response45['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response45['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response45['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response45['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response45['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response45['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict45 = {'地区': 'NO(挪威)', 'URL': vid_id45, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df45 = pd.DataFrame(dict45)
df = pd.concat([df,df45])

# 46.CH
# vid_url
vid_ids46 = []
for item in response46['items']:
    vid_ids46.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids46)
)
vid_response = vid_request.execute()
vid_id46 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id46.append(yt_link)
# other items
for item in response46['items']:

    vid_title = []
    for item in response46['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response46['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response46['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response46['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response46['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response46['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response46['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response46['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response46['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict46 = {'地区': 'CH(瑞士)', 'URL': vid_id46, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df46 = pd.DataFrame(dict46)
df = pd.concat([df,df46])

# 47.AT
# vid_url
vid_ids47 = []
for item in response47['items']:
    vid_ids47.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids47)
)
vid_response = vid_request.execute()
vid_id47 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id47.append(yt_link)
# other items
for item in response47['items']:

    vid_title = []
    for item in response47['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response47['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response47['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response47['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response47['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response47['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response47['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response47['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response47['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict47 = {'地区': 'AT(奥地利)', 'URL': vid_id47, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df47 = pd.DataFrame(dict47)
df = pd.concat([df,df47])

# 48.RO
# vid_url
vid_ids48 = []
for item in response48['items']:
    vid_ids48.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids48)
)
vid_response = vid_request.execute()
vid_id48 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id48.append(yt_link)
# other items
for item in response48['items']:

    vid_title = []
    for item in response48['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response48['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response48['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response48['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response48['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response48['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response48['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response48['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response48['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict48 = {'地区': 'RO(罗马尼亚)', 'URL': vid_id48, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df48 = pd.DataFrame(dict48)
df = pd.concat([df,df48])

# 49.PT
# vid_url
vid_ids49 = []
for item in response49['items']:
    vid_ids49.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids49)
)
vid_response = vid_request.execute()
vid_id49 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id49.append(yt_link)
# other items
for item in response49['items']:

    vid_title = []
    for item in response49['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response49['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response49['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response49['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response49['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response49['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response49['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response49['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response49['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict49 = {'地区': 'PT(葡萄牙)', 'URL': vid_id49, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df49 = pd.DataFrame(dict49)
df = pd.concat([df,df49])

# 50.SK
# vid_url
vid_ids50 = []
for item in response50['items']:
    vid_ids50.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids50)
)
vid_response = vid_request.execute()
vid_id50 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id50.append(yt_link)
# other items
for item in response50['items']:

    vid_title = []
    for item in response50['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response50['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response50['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response50['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response50['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response50['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response50['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response50['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response50['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict50 = {'地区': 'SK(斯洛伐克)', 'URL': vid_id50, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df50 = pd.DataFrame(dict50)
df = pd.concat([df,df50])

# 51.KW
# vid_url
vid_ids51 = []
for item in response51['items']:
    vid_ids51.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids51)
)
vid_response = vid_request.execute()
vid_id51 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id51.append(yt_link)
# other items
for item in response51['items']:

    vid_title = []
    for item in response51['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response51['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response51['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response51['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response51['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response51['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response51['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response51['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response51['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict51 = {'地区': 'KW(科威特)', 'URL': vid_id51, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df51 = pd.DataFrame(dict51)
df = pd.concat([df,df51])

# 52.BA
# vid_url
vid_ids52 = []
for item in response52['items']:
    vid_ids52.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids52)
)
vid_response = vid_request.execute()
vid_id52 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id52.append(yt_link)
# other items
for item in response52['items']:

    vid_title = []
    for item in response52['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response52['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response52['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response52['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response52['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response52['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response52['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response52['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response52['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict52 = {'地区': 'BA(波黑)', 'URL': vid_id52, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df52 = pd.DataFrame(dict52)
df = pd.concat([df,df52])

# 53.BG
# vid_url
vid_ids53 = []
for item in response53['items']:
    vid_ids53.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids53)
)
vid_response = vid_request.execute()
vid_id53 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id53.append(yt_link)
# other items
for item in response53['items']:

    vid_title = []
    for item in response53['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response53['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response53['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response53['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response53['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response53['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response53['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response53['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response53['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict53 = {'地区': 'BG(保加利亚)', 'URL': vid_id53, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df53 = pd.DataFrame(dict53)
df = pd.concat([df,df53])

# 54.EE
# vid_url
vid_ids54 = []
for item in response54['items']:
    vid_ids54.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids54)
)
vid_response = vid_request.execute()
vid_id54 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id54.append(yt_link)
# other items
for item in response54['items']:

    vid_title = []
    for item in response54['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response54['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response54['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response54['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response54['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response54['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response54['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response54['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response54['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict54 = {'地区': 'EE(爱沙尼亚)', 'URL': vid_id54, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df54 = pd.DataFrame(dict54)
df = pd.concat([df,df54])

# 55.HR
# vid_url
vid_ids55 = []
for item in response55['items']:
    vid_ids55.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids55)
)
vid_response = vid_request.execute()
vid_id55 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id55.append(yt_link)
# other items
for item in response55['items']:

    vid_title = []
    for item in response55['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response55['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response55['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response55['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response55['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response55['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response55['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response55['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response55['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict55 = {'地区': 'HR(克罗地亚)', 'URL': vid_id55, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df55 = pd.DataFrame(dict55)
df = pd.concat([df,df55])

# 56.LT
# vid_url
vid_ids56 = []
for item in response56['items']:
    vid_ids56.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids56)
)
vid_response = vid_request.execute()
vid_id56 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id56.append(yt_link)
# other items
for item in response56['items']:

    vid_title = []
    for item in response56['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response56['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response56['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response56['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response56['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response56['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response56['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response56['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response56['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict56 = {'地区': 'LT(立陶宛)', 'URL': vid_id56, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df56 = pd.DataFrame(dict56)
df = pd.concat([df,df56])

# 57.ME
# vid_url
vid_ids57 = []
for item in response57['items']:
    vid_ids57.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids57)
)
vid_response = vid_request.execute()
vid_id57 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id57.append(yt_link)
# other items
for item in response57['items']:

    vid_title = []
    for item in response57['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response57['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response57['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response57['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response57['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response57['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response57['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response57['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response57['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict57 = {'地区': 'ME(黑山)', 'URL': vid_id57, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df57 = pd.DataFrame(dict57)
df = pd.concat([df,df57])

# 58.MK
# vid_url
vid_ids58 = []
for item in response58['items']:
    vid_ids58.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids58)
)
vid_response = vid_request.execute()
vid_id58 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id58.append(yt_link)
# other items
for item in response58['items']:

    vid_title = []
    for item in response58['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response58['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response58['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response58['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response58['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response58['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response58['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response58['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response58['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict58 = {'地区': 'MK(北马其顿)', 'URL': vid_id58, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df58 = pd.DataFrame(dict58)
df = pd.concat([df,df58])

# 59.RS
# vid_url
vid_ids59 = []
for item in response58['items']:
    vid_ids59.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids59)
)
vid_response = vid_request.execute()
vid_id59 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id59.append(yt_link)
# other items
for item in response59['items']:

    vid_title = []
    for item in response59['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response59['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response59['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response59['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response59['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response59['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response59['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response59['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response59['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict59 = {'地区': 'RS(塞尔维亚)', 'URL': vid_id59, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df59 = pd.DataFrame(dict59)
df = pd.concat([df,df59])

# 60.SI
# vid_url
vid_ids60 = []
for item in response60['items']:
    vid_ids60.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids60)
)
vid_response = vid_request.execute()
vid_id60 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id60.append(yt_link)
# other items
for item in response60['items']:

    vid_title = []
    for item in response60['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response60['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response60['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response60['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response60['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response60['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response60['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response60['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response60['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict60 = {'地区': 'SI(斯洛文尼亚)', 'URL': vid_id60, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df60 = pd.DataFrame(dict60)
df = pd.concat([df,df60])

# 61.TH
# vid_url
vid_ids61 = []
for item in response61['items']:
    vid_ids61.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids61)
)
vid_response = vid_request.execute()
vid_id61 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id61.append(yt_link)
# other items
for item in response61['items']:

    vid_title = []
    for item in response61['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response61['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response61['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response61['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response61['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response61['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response61['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response61['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response61['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict61 = {'地区': 'TH(泰国)', 'URL': vid_id61, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df61 = pd.DataFrame(dict61)
df = pd.concat([df,df61])

# 62.LB
# vid_url
vid_ids62 = []
for item in response62['items']:
    vid_ids62.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids62)
)
vid_response = vid_request.execute()
vid_id62 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id62.append(yt_link)
# other items
for item in response62['items']:

    vid_title = []
    for item in response62['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response62['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response62['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response62['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response62['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response62['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response62['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response62['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response62['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict62 = {'地区': 'LB(黎巴嫩)', 'URL': vid_id62, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df62 = pd.DataFrame(dict62)
df = pd.concat([df,df62])

# 63.PR
# vid_url
vid_ids63 = []
for item in response63['items']:
    vid_ids63.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids63)
)
vid_response = vid_request.execute()
vid_id63 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id63.append(yt_link)
# other items
for item in response63['items']:

    vid_title = []
    for item in response63['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response63['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response63['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response63['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response63['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response63['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response63['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response63['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response63['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict63 = {'地区': 'PR(波多黎各)', 'URL': vid_id63, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df63 = pd.DataFrame(dict63)
df = pd.concat([df,df63])

# 64.IS
# vid_url
vid_ids64 = []
for item in response64['items']:
    vid_ids64.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids64)
)
vid_response = vid_request.execute()
vid_id64 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id64.append(yt_link)
# other items
for item in response64['items']:

    vid_title = []
    for item in response64['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response64['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response64['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response64['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response64['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response64['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response64['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response64['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response64['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict64 = {'地区': 'IS(冰岛)', 'URL': vid_id64, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df64 = pd.DataFrame(dict64)
df = pd.concat([df,df64])

# 65.LU
# vid_url
vid_ids65 = []
for item in response65['items']:
    vid_ids65.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids65)
)
vid_response = vid_request.execute()
vid_id65 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id65.append(yt_link)
# other items
for item in response65['items']:

    vid_title = []
    for item in response65['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response65['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response65['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response65['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response65['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response65['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response65['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response65['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response65['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict65 = {'地区': 'LU(卢森堡)', 'URL': vid_id65, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df65 = pd.DataFrame(dict65)
df = pd.concat([df,df65])

# 66.VN
# vid_url
vid_ids66 = []
for item in response66['items']:
    vid_ids66.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids66)
)
vid_response = vid_request.execute()
vid_id66 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id66.append(yt_link)
# other items
for item in response66['items']:

    vid_title = []
    for item in response66['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response66['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response66['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response66['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response66['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response66['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response66['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response66['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response66['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict66 = {'地区': 'VN(越南)', 'URL': vid_id66, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df66 = pd.DataFrame(dict66)
df = pd.concat([df,df66])

# 67.LY
# vid_url
vid_ids67 = []
for item in response67['items']:
    vid_ids67.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids67)
)
vid_response = vid_request.execute()
vid_id67 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id67.append(yt_link)
# other items
for item in response67['items']:

    vid_title = []
    for item in response67['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response67['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response67['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response67['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response67['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response67['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response67['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response67['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response67['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict67 = {'地区': 'LY(利比亚)', 'URL': vid_id67, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df67 = pd.DataFrame(dict67)
df = pd.concat([df,df67])

# 68.TZ
# vid_url
vid_ids68 = []
for item in response68['items']:
    vid_ids68.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids68)
)
vid_response = vid_request.execute()
vid_id68 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id68.append(yt_link)
# other items
for item in response68['items']:

    vid_title = []
    for item in response68['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response68['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response68['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response68['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response68['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response68['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response68['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response68['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response68['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict68 = {'地区': 'TZ(坦桑尼亚)', 'URL': vid_id68, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df68 = pd.DataFrame(dict68)
df = pd.concat([df,df68])

# 69.ZW
# vid_url
vid_ids69 = []
for item in response69['items']:
    vid_ids69.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids69)
)
vid_response = vid_request.execute()
vid_id69 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id69.append(yt_link)
# other items
for item in response69['items']:

    vid_title = []
    for item in response69['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response69['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response69['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response69['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response69['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response69['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response69['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response69['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response69['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict69 = {'地区': 'ZW(津巴布韦)', 'URL': vid_id69, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df69 = pd.DataFrame(dict69)
df = pd.concat([df,df69])

# 70.AZ
# vid_url
vid_ids70 = []
for item in response70['items']:
    vid_ids70.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids70)
)
vid_response = vid_request.execute()
vid_id70 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id70.append(yt_link)
# other items
for item in response70['items']:

    vid_title = []
    for item in response70['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response70['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response70['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response70['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response70['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response70['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response70['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response70['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response70['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict70 = {'地区': 'AZ(阿塞拜疆)', 'URL': vid_id70, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df70 = pd.DataFrame(dict70)
df = pd.concat([df,df70])

# # 71.BL
# # vid_url
# vid_ids71 = []
# for item in response71['items']:
#     vid_ids71.append(item['id'])
# vid_request = youtube.videos().list(
#     part="statistics",
#     id=','.join(vid_ids71)
# )
# vid_response = vid_request.execute()
# vid_id71 = []
# for item in vid_response['items']:
#     vid_id = item['id']
#     yt_link = f'https://youtu.be/{vid_id}'
#     vid_id71.append(yt_link)
# # other items
# for item in response71['items']:
#
#     vid_title = []
#     for item in response71['items']:
#         vid_title.append(item['snippet']['title'])
#
#     vid_publishedAt = []
#     for item in response71['items']:
#         vid_publishedAt.append(item['snippet']['publishedAt'])
#
#     vid_channeltitle = []
#     for item in response71['items']:
#         vid_channeltitle.append(item['snippet']['channelTitle'])
#
#     vid_viewCount = []
#     for item in response71['items']:
#         vid_viewCount.append(item['statistics']['viewCount'])
#
#     # vid_likeCount = []
#     # for item in response71['items']:
#     #     vid_likeCount.append(item['statistics']['likeCount'])
#
#     # vid_commentCount = []
#     # for item in response71['items']:
#     #     vid_commentCount.append(item['statistics']['commentCount'])
#
#     vid_channelId = []
#     for item in response71['items']:
#         vid_channelId.append(item['snippet']['channelId'])
#
#     vid_categoryId = []
#     for item in response71['items']:
#         vid_categoryId.append(item['snippet']['categoryId'])
#
#     vid_duration = []
#     for item in response71['items']:
#
#         duration = item['contentDetails']['duration']
#         hours = hours_pattern.search(duration)
#         minutes = minutes_pattern.search(duration)
#         seconds = seconds_pattern.search(duration)
#
#         hours = int(hours.group(1)) if hours else 0
#         minutes = int(minutes.group(1)) if minutes else 0
#         seconds = int(seconds.group(1)) if seconds else 0
#
#         duration2 = f'{hours}:{minutes}:{seconds}'
#         vid_duration.append(duration2)
#
#     dict71 = {'地区': 'BL(白俄罗斯)', 'URL': vid_id71, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
#              '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
# df71 = pd.DataFrame(dict71)
# df = pd.concat([df,df71])

# 72.GE
# vid_url
vid_ids72 = []
for item in response72['items']:
    vid_ids72.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids72)
)
vid_response = vid_request.execute()
vid_id72 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id72.append(yt_link)
# other items
for item in response72['items']:

    vid_title = []
    for item in response72['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response72['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response72['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response72['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response72['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response72['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response72['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response72['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response72['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict72 = {'地区': 'GE(格鲁吉亚)', 'URL': vid_id72, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df72 = pd.DataFrame(dict72)
df = pd.concat([df,df72])

# # 73.KA
# # vid_url
# vid_ids73 = []
# for item in response73['items']:
#     vid_ids73.append(item['id'])
# vid_request = youtube.videos().list(
#     part="statistics",
#     id=','.join(vid_ids73)
# )
# vid_response = vid_request.execute()
# vid_id73 = []
# for item in vid_response['items']:
#     vid_id = item['id']
#     yt_link = f'https://youtu.be/{vid_id}'
#     vid_id73.append(yt_link)
# # other items
# for item in response73['items']:
#
#     vid_title = []
#     for item in response73['items']:
#         vid_title.append(item['snippet']['title'])
#
#     vid_publishedAt = []
#     for item in response73['items']:
#         vid_publishedAt.append(item['snippet']['publishedAt'])
#
#     vid_channeltitle = []
#     for item in response73['items']:
#         vid_channeltitle.append(item['snippet']['channelTitle'])
#
#     vid_viewCount = []
#     for item in response73['items']:
#         vid_viewCount.append(item['statistics']['viewCount'])
#
#     # vid_likeCount = []
#     # for item in response73['items']:
#     #     vid_likeCount.append(item['statistics']['likeCount'])
#
#     # vid_commentCount = []
#     # for item in response73['items']:
#     #     vid_commentCount.append(item['statistics']['commentCount'])
#
#     vid_channelId = []
#     for item in response73['items']:
#         vid_channelId.append(item['snippet']['channelId'])
#
#     vid_categoryId = []
#     for item in response73['items']:
#         vid_categoryId.append(item['snippet']['categoryId'])
#
#     vid_duration = []
#     for item in response73['items']:
#
#         duration = item['contentDetails']['duration']
#         hours = hours_pattern.search(duration)
#         minutes = minutes_pattern.search(duration)
#         seconds = seconds_pattern.search(duration)
#
#         hours = int(hours.group(1)) if hours else 0
#         minutes = int(minutes.group(1)) if minutes else 0
#         seconds = int(seconds.group(1)) if seconds else 0
#
#         duration2 = f'{hours}:{minutes}:{seconds}'
#         vid_duration.append(duration2)
#
#     dict73 = {'地区': 'KA(哈萨克斯坦)', 'URL': vid_id73, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
#              '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
# df73 = pd.DataFrame(dict73)
# df = pd.concat([df,df73])
#
# # 74.NE
# # vid_url
# vid_ids74 = []
# for item in response74['items']:
#     vid_ids74.append(item['id'])
# vid_request = youtube.videos().list(
#     part="statistics",
#     id=','.join(vid_ids74)
# )
# vid_response = vid_request.execute()
# vid_id74 = []
# for item in vid_response['items']:
#     vid_id = item['id']
#     yt_link = f'https://youtu.be/{vid_id}'
#     vid_id74.append(yt_link)
# # other items
# for item in response74['items']:
#
#     vid_title = []
#     for item in response74['items']:
#         vid_title.append(item['snippet']['title'])
#
#     vid_publishedAt = []
#     for item in response74['items']:
#         vid_publishedAt.append(item['snippet']['publishedAt'])
#
#     vid_channeltitle = []
#     for item in response74['items']:
#         vid_channeltitle.append(item['snippet']['channelTitle'])
#
#     vid_viewCount = []
#     for item in response74['items']:
#         vid_viewCount.append(item['statistics']['viewCount'])
#
#     # vid_likeCount = []
#     # for item in response74['items']:
#     #     vid_likeCount.append(item['statistics']['likeCount'])
#
#     # vid_commentCount = []
#     # for item in response74['items']:
#     #     vid_commentCount.append(item['statistics']['commentCount'])
#
#     vid_channelId = []
#     for item in response74['items']:
#         vid_channelId.append(item['snippet']['channelId'])
#
#     vid_categoryId = []
#     for item in response74['items']:
#         vid_categoryId.append(item['snippet']['categoryId'])
#
#     vid_duration = []
#     for item in response74['items']:
#
#         duration = item['contentDetails']['duration']
#         hours = hours_pattern.search(duration)
#         minutes = minutes_pattern.search(duration)
#         seconds = seconds_pattern.search(duration)
#
#         hours = int(hours.group(1)) if hours else 0
#         minutes = int(minutes.group(1)) if minutes else 0
#         seconds = int(seconds.group(1)) if seconds else 0
#
#         duration2 = f'{hours}:{minutes}:{seconds}'
#         vid_duration.append(duration2)
#
#     dict74 = {'地区': 'NE(尼泊尔)', 'URL': vid_id74, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
#              '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
# df74 = pd.DataFrame(dict74)
# df = pd.concat([df,df74])

# 75.PA
# vid_url
vid_ids75 = []
for item in response75['items']:
    vid_ids75.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids75)
)
vid_response = vid_request.execute()
vid_id75 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id75.append(yt_link)
# other items
for item in response75['items']:

    vid_title = []
    for item in response75['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response75['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response75['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response75['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response75['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response75['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response75['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response75['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response75['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict75 = {'地区': 'PA(巴基斯坦)', 'URL': vid_id75, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df75 = pd.DataFrame(dict75)
df = pd.concat([df,df75])

# 76.LK
# vid_url
vid_ids76 = []
for item in response76['items']:
    vid_ids76.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids76)
)
vid_response = vid_request.execute()
vid_id76 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id76.append(yt_link)
# other items
for item in response76['items']:

    vid_title = []
    for item in response76['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response76['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response76['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response76['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response76['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response76['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response76['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response76['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response76['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict76 = {'地区': 'LK(斯里兰卡)', 'URL': vid_id76, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df76 = pd.DataFrame(dict76)
df = pd.concat([df,df76])

# # 77.IR
# # vid_url
# vid_ids77 = []
# for item in response77['items']:
#     vid_ids77.append(item['id'])
# vid_request = youtube.videos().list(
#     part="statistics",
#     id=','.join(vid_ids77)
# )
# vid_response = vid_request.execute()
# vid_id77 = []
# for item in vid_response['items']:
#     vid_id = item['id']
#     yt_link = f'https://youtu.be/{vid_id}'
#     vid_id77.append(yt_link)
# # other items
# for item in response77['items']:
#
#     vid_title = []
#     for item in response77['items']:
#         vid_title.append(item['snippet']['title'])
#
#     vid_publishedAt = []
#     for item in response77['items']:
#         vid_publishedAt.append(item['snippet']['publishedAt'])
#
#     vid_channeltitle = []
#     for item in response77['items']:
#         vid_channeltitle.append(item['snippet']['channelTitle'])
#
#     vid_viewCount = []
#     for item in response77['items']:
#         vid_viewCount.append(item['statistics']['viewCount'])
#
#     # vid_likeCount = []
#     # for item in response77['items']:
#     #     vid_likeCount.append(item['statistics']['likeCount'])
#
#     # vid_commentCount = []
#     # for item in response77['items']:
#     #     vid_commentCount.append(item['statistics']['commentCount'])
#
#     vid_channelId = []
#     for item in response77['items']:
#         vid_channelId.append(item['snippet']['channelId'])
#
#     vid_categoryId = []
#     for item in response77['items']:
#         vid_categoryId.append(item['snippet']['categoryId'])
#
#     vid_duration = []
#     for item in response77['items']:
#
#         duration = item['contentDetails']['duration']
#         hours = hours_pattern.search(duration)
#         minutes = minutes_pattern.search(duration)
#         seconds = seconds_pattern.search(duration)
#
#         hours = int(hours.group(1)) if hours else 0
#         minutes = int(minutes.group(1)) if minutes else 0
#         seconds = int(seconds.group(1)) if seconds else 0
#
#         duration2 = f'{hours}:{minutes}:{seconds}'
#         vid_duration.append(duration2)
#
#     dict77 = {'地区': 'IR(伊拉克)', 'URL': vid_id77, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
#              '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
# df77 = pd.DataFrame(dict77)
# df = pd.concat([df,df77])
#
# # 78.JA
# # vid_url
# vid_ids78 = []
# for item in response78['items']:
#     vid_ids78.append(item['id'])
# vid_request = youtube.videos().list(
#     part="statistics",
#     id=','.join(vid_ids78)
# )
# vid_response = vid_request.execute()
# vid_id78 = []
# for item in vid_response['items']:
#     vid_id = item['id']
#     yt_link = f'https://youtu.be/{vid_id}'
#     vid_id78.append(yt_link)
# # other items
# for item in response78['items']:
#
#     vid_title = []
#     for item in response78['items']:
#         vid_title.append(item['snippet']['title'])
#
#     vid_publishedAt = []
#     for item in response78['items']:
#         vid_publishedAt.append(item['snippet']['publishedAt'])
#
#     vid_channeltitle = []
#     for item in response78['items']:
#         vid_channeltitle.append(item['snippet']['channelTitle'])
#
#     vid_viewCount = []
#     for item in response78['items']:
#         vid_viewCount.append(item['statistics']['viewCount'])
#
#     # vid_likeCount = []
#     # for item in response78['items']:
#     #     vid_likeCount.append(item['statistics']['likeCount'])
#
#     # vid_commentCount = []
#     # for item in response78['items']:
#     #     vid_commentCount.append(item['statistics']['commentCount'])
#
#     vid_channelId = []
#     for item in response78['items']:
#         vid_channelId.append(item['snippet']['channelId'])
#
#     vid_categoryId = []
#     for item in response78['items']:
#         vid_categoryId.append(item['snippet']['categoryId'])
#
#     vid_duration = []
#     for item in response78['items']:
#
#         duration = item['contentDetails']['duration']
#         hours = hours_pattern.search(duration)
#         minutes = minutes_pattern.search(duration)
#         seconds = seconds_pattern.search(duration)
#
#         hours = int(hours.group(1)) if hours else 0
#         minutes = int(minutes.group(1)) if minutes else 0
#         seconds = int(seconds.group(1)) if seconds else 0
#
#         duration2 = f'{hours}:{minutes}:{seconds}'
#         vid_duration.append(duration2)
#
#     dict78 = {'地区': 'JA(牙买加)', 'URL': vid_id78, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
#              '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
# df78 = pd.DataFrame(dict78)
# df = pd.concat([df,df78])

# 79.DZ
# vid_url
vid_ids79 = []
for item in response79['items']:
    vid_ids79.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids79)
)
vid_response = vid_request.execute()
vid_id79 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id79.append(yt_link)
# other items
for item in response79['items']:

    vid_title = []
    for item in response79['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response79['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response79['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response79['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response79['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response79['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response79['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response79['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response79['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict79 = {'地区': 'JA(阿尔及利亚)', 'URL': vid_id79, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df79 = pd.DataFrame(dict79)
df = pd.concat([df,df79])

# 79.DZ
# vid_url
vid_ids79 = []
for item in response79['items']:
    vid_ids79.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids79)
)
vid_response = vid_request.execute()
vid_id79 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id79.append(yt_link)
# other items
for item in response79['items']:

    vid_title = []
    for item in response79['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response79['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response79['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response79['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response79['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response79['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response79['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response79['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response79['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict79 = {'地区': 'JA(阿尔及利亚)', 'URL': vid_id79, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df79 = pd.DataFrame(dict79)
df = pd.concat([df,df79])

# 80.EG
# vid_url
vid_ids80 = []
for item in response80['items']:
    vid_ids80.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids80)
)
vid_response = vid_request.execute()
vid_id80 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id80.append(yt_link)
# other items
for item in response80['items']:

    vid_title = []
    for item in response80['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response80['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response80['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response80['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response80['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response80['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response80['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response80['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response80['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict80 = {'地区': 'EG(埃及)', 'URL': vid_id80, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df80 = pd.DataFrame(dict80)
df = pd.concat([df,df80])

# 79.TN
# vid_url
vid_ids79 = []
for item in response79['items']:
    vid_ids79.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids79)
)
vid_response = vid_request.execute()
vid_id79 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id79.append(yt_link)
# other items
for item in response79['items']:

    vid_title = []
    for item in response79['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response79['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response79['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response79['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response79['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response79['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response79['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response79['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response79['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict79 = {'地区': 'TN(突尼斯)', 'URL': vid_id79, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df79 = pd.DataFrame(dict79)
df = pd.concat([df,df79])

# 82.JO
# vid_url
vid_ids82 = []
for item in response82['items']:
    vid_ids82.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids82)
)
vid_response = vid_request.execute()
vid_id82 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id82.append(yt_link)
# other items
for item in response82['items']:

    vid_title = []
    for item in response82['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response82['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response82['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response82['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response82['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response82['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response82['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response82['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response82['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict82 = {'地区': 'JO(约旦)', 'URL': vid_id82, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df82 = pd.DataFrame(dict82)
df = pd.concat([df,df82])

# 83.MA
# vid_url
vid_ids83 = []
for item in response83['items']:
    vid_ids83.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids83)
)
vid_response = vid_request.execute()
vid_id83 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id83.append(yt_link)
# other items
for item in response83['items']:

    vid_title = []
    for item in response83['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response83['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response83['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response83['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response83['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response83['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response83['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response83['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response83['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict83 = {'地区': 'MA(摩洛哥)', 'URL': vid_id83, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df83 = pd.DataFrame(dict83)
df = pd.concat([df,df83])

# 84.YE
# vid_url
vid_ids84 = []
for item in response84['items']:
    vid_ids84.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids84)
)
vid_response = vid_request.execute()
vid_id84 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id84.append(yt_link)
# other items
for item in response84['items']:

    vid_title = []
    for item in response84['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response84['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response84['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response84['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response84['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response84['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response84['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response84['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response84['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict84 = {'地区': 'YE(也门)', 'URL': vid_id84, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df84 = pd.DataFrame(dict84)
df = pd.concat([df,df84])

# 85.BH
# vid_url
vid_ids85 = []
for item in response85['items']:
    vid_ids85.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids85)
)
vid_response = vid_request.execute()
vid_id85 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id85.append(yt_link)
# other items
for item in response85['items']:

    vid_title = []
    for item in response85['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response85['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response85['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response85['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response85['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response85['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response85['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response85['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response85['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict85 = {'地区': 'BH(巴林)', 'URL': vid_id85, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df85 = pd.DataFrame(dict85)
df = pd.concat([df,df85])

# 86.OM
# vid_url
vid_ids86 = []
for item in response86['items']:
    vid_ids86.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids86)
)
vid_response = vid_request.execute()
vid_id86 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id86.append(yt_link)
# other items
for item in response86['items']:

    vid_title = []
    for item in response86['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response86['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response86['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response86['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response86['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response86['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response86['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response86['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response86['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict86 = {'地区': 'OM(阿曼)', 'URL': vid_id86, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df86 = pd.DataFrame(dict86)
df = pd.concat([df,df86])

# 87.QA
# vid_url
vid_ids87 = []
for item in response87['items']:
    vid_ids87.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids87)
)
vid_response = vid_request.execute()
vid_id87 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id87.append(yt_link)
# other items
for item in response87['items']:

    vid_title = []
    for item in response87['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response87['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response87['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response87['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response87['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response87['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response87['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response87['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response87['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict87 = {'地区': 'QA(卡塔尔)', 'URL': vid_id87, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df87 = pd.DataFrame(dict87)
df = pd.concat([df,df87])

# 88.IE
# vid_url
vid_ids88 = []
for item in response88['items']:
    vid_ids88.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids88)
)
vid_response = vid_request.execute()
vid_id88 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id88.append(yt_link)
# other items
for item in response88['items']:

    vid_title = []
    for item in response88['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response88['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response88['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response88['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response88['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response88['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response88['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response88['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response88['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict88 = {'地区': 'IE(爱尔兰)', 'URL': vid_id88, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df88 = pd.DataFrame(dict88)
df = pd.concat([df,df88])

# # 89.KL
# # vid_url
# vid_ids89 = []
# for item in response89['items']:
#     vid_ids89.append(item['id'])
# vid_request = youtube.videos().list(
#     part="statistics",
#     id=','.join(vid_ids89)
# )
# vid_response = vid_request.execute()
# vid_id89 = []
# for item in vid_response['items']:
#     vid_id = item['id']
#     yt_link = f'https://youtu.be/{vid_id}'
#     vid_id89.append(yt_link)
# # other items
# for item in response89['items']:
#
#     vid_title = []
#     for item in response89['items']:
#         vid_title.append(item['snippet']['title'])
#
#     vid_publishedAt = []
#     for item in response89['items']:
#         vid_publishedAt.append(item['snippet']['publishedAt'])
#
#     vid_channeltitle = []
#     for item in response89['items']:
#         vid_channeltitle.append(item['snippet']['channelTitle'])
#
#     vid_viewCount = []
#     for item in response89['items']:
#         vid_viewCount.append(item['statistics']['viewCount'])
#
#     # vid_likeCount = []
#     # for item in response89['items']:
#     #     vid_likeCount.append(item['statistics']['likeCount'])
#
#     # vid_commentCount = []
#     # for item in response89['items']:
#     #     vid_commentCount.append(item['statistics']['commentCount'])
#
#     vid_channelId = []
#     for item in response89['items']:
#         vid_channelId.append(item['snippet']['channelId'])
#
#     vid_categoryId = []
#     for item in response89['items']:
#         vid_categoryId.append(item['snippet']['categoryId'])
#
#     vid_duration = []
#     for item in response89['items']:
#
#         duration = item['contentDetails']['duration']
#         hours = hours_pattern.search(duration)
#         minutes = minutes_pattern.search(duration)
#         seconds = seconds_pattern.search(duration)
#
#         hours = int(hours.group(1)) if hours else 0
#         minutes = int(minutes.group(1)) if minutes else 0
#         seconds = int(seconds.group(1)) if seconds else 0
#
#         duration2 = f'{hours}:{minutes}:{seconds}'
#         vid_duration.append(duration2)
#
#     dict89 = {'地区': 'KL(苏格兰)', 'URL': vid_id89, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
#              '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
# df89 = pd.DataFrame(dict89)
# df = pd.concat([df,df89])

# 90.LV
# vid_url
vid_ids90 = []
for item in response90['items']:
    vid_ids90.append(item['id'])
vid_request = youtube.videos().list(
    part="statistics",
    id=','.join(vid_ids90)
)
vid_response = vid_request.execute()
vid_id90 = []
for item in vid_response['items']:
    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'
    vid_id90.append(yt_link)
# other items
for item in response90['items']:

    vid_title = []
    for item in response90['items']:
        vid_title.append(item['snippet']['title'])

    vid_publishedAt = []
    for item in response90['items']:
        vid_publishedAt.append(item['snippet']['publishedAt'])

    vid_channeltitle = []
    for item in response90['items']:
        vid_channeltitle.append(item['snippet']['channelTitle'])

    vid_viewCount = []
    for item in response90['items']:
        vid_viewCount.append(item['statistics']['viewCount'])

    # vid_likeCount = []
    # for item in response90['items']:
    #     vid_likeCount.append(item['statistics']['likeCount'])

    # vid_commentCount = []
    # for item in response90['items']:
    #     vid_commentCount.append(item['statistics']['commentCount'])

    vid_channelId = []
    for item in response90['items']:
        vid_channelId.append(item['snippet']['channelId'])

    vid_categoryId = []
    for item in response90['items']:
        vid_categoryId.append(item['snippet']['categoryId'])

    vid_duration = []
    for item in response90['items']:

        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        duration2 = f'{hours}:{minutes}:{seconds}'
        vid_duration.append(duration2)

    dict90 = {'地区': 'LV(拉脱维亚)', 'URL': vid_id90, '视频标题': vid_title, '发布日期': vid_publishedAt, '时长': vid_duration, '浏览量': vid_viewCount,
             '频道标题': vid_channeltitle, '频道ID': vid_channelId,'分类ID': vid_categoryId}
df90 = pd.DataFrame(dict90)
df = pd.concat([df,df90])

# to csv

# dff = pd.read_csv('AAA.csv')
# df = pd.concat([df,dff])
# pd.merge(df, dff, on = '地区', how ='outer')
total = str('总计:' + str((df['视频标题'].count())))
# print(total)
df.loc[total,:]=['','','','','','','','','']
path = os.path.abspath('G:/Branche/TVT CODE/row_data')
df.to_csv(path+ '/'+ year+ '-'+ month+'-' +day +'.csv', encoding='utf_8_sig')

print(f'运行完成')

# endtime & runtime
t2 = datetime.datetime.now()
print("end >> {}".format(t2))
print("runtime >> {}".format(t2-t1))