import pandas as pd
import requests
import geohash2

def oneroom(addr):
    url = f'https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸'
    response = requests.get(url)
    data = response.json()['items'][0]
    lat, lng = data['lat'], data['lng']
    geohash = geohash2.encode(lat, lng, precision=5)
    
    
    url = f'https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={geohash}&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸'
    response = requests.get(url)
    
    items = response.json()['items']
    ids = [item['item_id'] for item in items]
    url = f'https://apis.zigbang.com/v2/items/list'
    params = {
        'domain' : 'zigbang',
        'item_ids' : ids}
    response = requests.post(url, params)
    data = response.json()['items']
    df = pd.DataFrame(data)
    columns = ['item_id','sales_type', 'deposit', 'rent', 'size_m2', 
               'floor', 'floor_string','building_floor','title',
               'service_type','manage_cost','address1']

    df = df[columns]
    result = df[df['address1'].str.contains(addr)].reset_index(drop=True)
    return result
