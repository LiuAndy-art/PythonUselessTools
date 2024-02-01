# 地理编码正向查询——通过名称查询经纬度或者具体地址
# 地理编码逆向查询——通过经纬度查询具体地址
import requests
from geopy.geocoders import Nominatim


# 使用Nominatim免费查询
def nominatim_map_positive(addr):
    # 创建 Nominatim 地理编码器
    geolocator = Nominatim(user_agent="myGeocoder")
    # 要查询的地址
    location = geolocator.geocode(addr)
    print("详细地址：", location.address)
    print("经纬度：{}, {}".format(location.longitude, location.latitude))
    return location.address, location.longitude, location.latitude

# 高德地图API，通过地址查询对应的省市


def gd_map(addr):
    para = {'key': '02c9ba29014a640141db065e4a86c429',  # 高德Key
            'address': addr}  # 地址参数
    url = 'https://restapi.amap.com/v3/geocode/geo?'  # 高德地图地理编码API服务地址
    result = requests.get(url, para)  # GET方式请求
    result = result.json()
    try:
        prov = result['geocodes'][0]['province']  # 获取返回参数geocodes中的province
        city = result['geocodes'][0]['city']  # 获取返回参数geocodes中的city
        return prov + "," + city
    except BaseException:
        return ","

# 使用Nominatim免费逆向查询


def nominatim_map_reverse(latitude, longitude):
    """
    latitude: 纬度
    longitude: 经度
    """
    # 创建 Nominatim 地理编码器
    geolocator = Nominatim(user_agent="myGeocoder")
    # 要查询的地址
    location = geolocator.reverse("{}, {}".format(latitude, longitude))
    print("详细地址：", location.address)
    return location.address
