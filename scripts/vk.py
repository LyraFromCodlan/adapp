import requests
token = 'vk1.a.A1Lqq5MHfQVQmnJqAbzH5tg2F4rgy2QxVBh9kFIA6SsQ2-rEawy_CZax76kOxo_kULUJOlT7Rc6XO5oDYHlEUDYodbtNDA1dTXSZZvr6ZhGJlon1_CF08XUSaGCL1-mUvhqalaSGwAG-k08uwevGS4msdbXs3UrJ4vbdS0E5aj4RhoGGfogmQ37L-iegmNgj'
version = 5.131
# 614989038 8230390
id_rk = 8230390
campaign_ids = []
ads_ids = []
# vk1.a.A1Lqq5MHfQVQmnJqAbzH5tg2F4rgy2QxVBh9kFIA6SsQ2-rEawy_CZax76kOxo_kULUJOlT7Rc6XO5oDYHlEUDYodbtNDA1dTXSZZvr6ZhGJlon1_CF08XUSaGCL1-mUvhqalaSGwAG-k08uwevGS4msdbXs3UrJ4vbdS0E5aj4RhoGGfogmQ37L-iegmNgj
r = requests.get('https://api.vk.com/method/ads.getAds', params={
    'access_token': token,
    'v': version,
    'account_id': id_rk
})
data = r.json()#['response']
print(data)