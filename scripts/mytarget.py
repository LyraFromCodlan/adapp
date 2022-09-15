import requests
r=requests.get('https://target.my.com/api/v2/statistics/campaigns/day.json?id=857683&date_from=2017-09-20&date_to=2017-09-21&metrics=all',params={
    
})
print(r.json())