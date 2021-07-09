import math
import uuid
import numpy
import time
import os
import requests
import json
import warnings
warnings.filterwarnings(action='ignore')
import pandas
import geopandas as gpd
from shapely.geometry import Point, LineString


null = None


def _loadJsonFile(jsonPath):
    with open(jsonPath, "rt", encoding="UTF8") as f:
        jsonData = json.load(f)
    return jsonData
def convertGeo4326To5186(lon,lat):
  '''
  :param lon: inputLon
  :param lat: inputLat
  :return: new lon,lat
  '''
  if lat>1000 and lon>1000: #이미 5186으로 들어오고 있는 경우도 있어서 그 경우 구분하려고 넣어놓은 부분입니다
    return lon,lat
  else:
    df = pandas.DataFrame({'lat': [lat], 'lon': [lon]})
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")
    gdf_5186 = gdf.to_crs(epsg=5186)
    # print("gdf_5186 :", gdf_5186.representative_point().x[0], gdf_5186.representative_point().y[0])
    return float(gdf_5186.representative_point().x[0]), float(gdf_5186.representative_point().y[0])

def getJsonData(id,password,url):
    '''
    Get Json Data from web
    안쓰고있어요~~~
    :param id: login id
    :param password: login password
    :return: json data
    '''
    jsonData=''
    if len(url)>1:
        if len(id) > 1:
            loginURL = url+'/user/login'
            access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImZpZCI6IjIzMjUzMjE1MDIiLCJqb2JfaWQiOiJPRkZJQ0UifSwiaWF0IjoxNTgyMDg0Nzg1LCJleHAiOjE1ODQ2NzY3ODV9.1_mHWNNJaagyFzXaxIDsv8qUx14G1qx71sXRduxkiHM'
            param = {"id": id, "password": password}
            data = {"param": param}
            headers = {'Content-type': 'application/json', 'x-access-token': access_token}
            res = requests.post(url=loginURL, data=json.dumps(data), headers=headers)
            loginJsonData = res.json()
            token = loginJsonData['result']['token']
            URL = url+'/monitor/ifc'
            headers1 = {'Content-type': 'application/json', 'x-access-token': token}
            res1 = requests.post(url=URL, headers=headers1)
            jsonData = res1.json()
        else:
            if len(id)>1 :
                loginURL = 'https://www.digitaltwinx.kr/data/user/login'
                access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImZpZCI6IjIzMjUzMjE1MDIiLCJqb2JfaWQiOiJPRkZJQ0UifSwiaWF0IjoxNTgyMDg0Nzg1LCJleHAiOjE1ODQ2NzY3ODV9.1_mHWNNJaagyFzXaxIDsv8qUx14G1qx71sXRduxkiHM'
                param = {"id": id, "password":password }
                data = {"param": param}
                headers = {'Content-type': 'application/json', 'x-access-token': access_token}
                res = requests.post(url=loginURL, data=json.dumps(data), headers=headers)
                loginJsonData = res.json()
                token = loginJsonData['result']['token']
                URL = 'https://www.digitaltwinx.kr/data/monitor/ifc'
                headers1 = {'Content-type': 'application/json', 'x-access-token': token}
                res1 = requests.post(url=URL, headers=headers1)
                jsonData=res1.json()
    return jsonData


def getFromJsonToDicList(jsonData):
    '''
    convert jsonData to Dictionary(전체범위 그릴때..)
    :param jsonData: json data from web
    :return: dictionary(dic pipe ,dic joint, dic hole(obstruction))
    '''
    dicListResult = []
    area = ''
    for key, value in jsonData.items():
      if key=="data":
        for i in range(len(value)):
            groupName=value[i].get('groupNo')
            type=value[i].get('type')
            diameter=value[i].get('diameter')
            category=value[i].get('category')
            shape=value[i].get('shape')
            azimuth=value[i].get('azimuth')
            geometry=value[i].get('geometry')
            for j in range(len(geometry)):
                lon=geometry[j].get('lon')
                lat=geometry[j].get('lat')
                lon_5186,lat_5186=convertGeo4326To5186(lon,lat)
                geometry[j].setdefault("lon_5186",lon_5186)
                geometry[j].setdefault("lat_5186", lat_5186)
            dic={}
            dic.setdefault("groupNo",groupName)
            dic.setdefault("type", type)
            dic.setdefault("diameter", diameter)
            dic.setdefault("category", category)
            dic.setdefault("shape", shape)
            dic.setdefault("azimuth", azimuth)
            dic.setdefault("geometry", geometry)
            dicListResult.append(dic)
    return dicListResult

def getAzimuthStandardError(lst):
    arry=[]
    for i in range(len(lst)):
        for key,value in lst[i].items():
            if key=='azimuth':
                arry.append(value)

    sum=0
    count=0
    for i in range(1,len(arry)):
        if math.fabs(arry[i]-arry[i-1])<10:
            sum=sum+math.fabs(arry[i]-arry[i-1])
            count=count+1
    return sum/count


def checkGroupNo(groupNo,lst):
    '''
    현재 파이프가 출력하려 하는 파이프인지 확인하는 함수
    :param groupNo: 현재 파이프
    :param lst: 출력하고자 하는 파이프 그룹 넘버 리스트
    :return:
    '''
    for i in range(len(lst)):
        if groupNo==lst[i]:
            return True
    return False
def getDicforCreateObjFromJson_groupNoList(json,groupNoList):
    '''
    json데이터를
    {pipe:
        {
            straight:[{..},{..}],
            curve:[{,,},{..}]
        },
    joint:{...},
    hole:
        {
            c:[{...},{..}],
            s:[{...},{..}]
        }
    }형식으로 만드는 함수
    :param json:파이프 정보 json 데이터
    :param groupNoList:출력하고자 하는 groupNo들
    :return:dic
    '''

    dic={}
    pipeDic={}
    pipe_pipeList=[]
    pipe_curveList=[]
    jointList=[]
    holeDic={}
    hole_cList=[]
    hole_sList=[]
    for key, value in json.items():
      if key=="data":
        for i in range(len(value)):
            type = value[i].get('type')
            group=value[i].get('groupNo')
            if checkGroupNo(group,groupNoList):
                diameter=0
                width=0
                height=0
                depth=0
                if value[i].get('diameter'):
                    diameter = float(value[i].get('diameter'))
                if value[i].get('width'):
                    width=value[i].get('width')
                if value[i].get('height'):
                    height=value[i].get('height')
                if type=="line":
                    geometry=value[i].get('geometry')
                    geoList=[]
                    for j in range(len(geometry)):
                        pitch=0
                        roll=0
                        lon = geometry[j].get('lon')
                        lat = geometry[j].get('lat')
                        if j==len(geometry)-1:
                            lon_2 = geometry[j].get('lon')
                            lat_2 = geometry[j].get('lat')
                            depth_2=geometry[j].get('depth')
                        else:
                            lon_2 = geometry[j+1].get('lon')
                            lat_2 = geometry[j+1].get('lat')
                            depth_2 = geometry[j + 1].get('depth')
                        lon_5186, lat_5186 = convertGeo4326To5186(lon, lat)
                        lon_5186_2, lat_5186_2 = convertGeo4326To5186(lon_2, lat_2)
                        point1=Point(lon_5186,lat_5186,depth)
                        point2=Point(lon_5186_2,lat_5186_2,depth_2)
                        depth=geometry[j].get('depth')
                        deltaDepth=depth_2-depth#매설심도차로 파이프간 거리 계산.0.5보다 크면 매설심도 적용 후 파이프 길이 계산
                        length=point1.distance(point2)#math.sqrt(((lon_5186_2 - lon_5186) ** 2) + ((lat_5186_2 - lat_5186) ** 2))
                        x=((lon_5186+lon_5186_2)/2)
                        y=((lat_5186+lat_5186_2)/2)
                        if geometry[j].get('pitch'):
                            pitch= geometry[j].get('pitch')
                        else:
                            if math.fabs(deltaDepth) > 0:
                                pitch=math.atan(deltaDepth/length)
                                pitch=pitch*180/math.pi
                                if math.fabs(pitch)>15:
                                    length=length+0.3
                                depth=(depth_2+depth)/2
                        if geometry[j].get('roll'):
                            roll= geometry[j].get('roll')
                        a=(y-lat_5186)
                        c=(x-lon_5186)
                        if a!=0 and c!=0:
                            theta=math.atan(c/a)
                        else :
                            theta=0
                        theta=theta*180/math.pi
                        geometry[j].setdefault("theta",theta)
                        geometry[j].setdefault("lon_5186", lon_5186)
                        geometry[j].setdefault("lat_5186", lat_5186)
                        geometry[j].setdefault('diameter',diameter)
                        geometry[j].setdefault('location', [x,y,depth])
                        if 90<geometry[j].get('azimuth')<270:
                            pitch=pitch*-1
                            length=length+0.1
                        geometry[j].setdefault('pitch', pitch-90)
                        geometry[j].setdefault('roll', roll)
                        geometry[j].setdefault("length", round(length,1))
                        geometry[j].setdefault('width', width)
                        geometry[j].setdefault('height', height)
                        geometry[j].setdefault('groupNo',group)
                        geoList.append(geometry[j])
                pipe_pipeList.append(geometry)
            elif type == 'curve':
                geometry = value[i].get('geometry')
                for j in range(len(geometry)):
                    lon = geometry[j].get('lon')
                    lat = geometry[j].get('lat')
                    lon_5186, lat_5186 = convertGeo4326To5186(lon, lat)
                    geometry[j].setdefault("lon_5186", lon_5186)
                    geometry[j].setdefault("lat_5186", lat_5186)
                    pipe_curveList.append(geometry[j])
            elif type == 'joint':
                geometry = value[i].get('geometry')
                for j in range(len(geometry)):
                    lon = geometry[j].get('lon')
                    lat = geometry[j].get('lat')
                    lon_5186, lat_5186 = convertGeo4326To5186(lon, lat)
                    geometry[j].setdefault("lon_5186", lon_5186)
                    geometry[j].setdefault("lat_5186", lat_5186)
                jointList.append(geometry)
            elif type == 'hole':
                if type_sub=='c':
                    geometry = value[i].get('geometry')
                    for j in range(len(geometry)):
                        lon = geometry[j].get('lon')
                        lat = geometry[j].get('lat')
                        lon_5186, lat_5186 = convertGeo4326To5186(lon, lat)
                        geometry[j].setdefault("lon_5186", lon_5186)
                        geometry[j].setdefault("lat_5186", lat_5186)
                    hole_cList.append(geometry)
                elif type_sub=='s':
                    geometry = value[i].get('geometry')
                    for j in range(len(geometry)):
                        lon = geometry[j].get('lon')
                        lat = geometry[j].get('lat')
                        lon_5186, lat_5186 = convertGeo4326To5186(lon, lat)
                        geometry[j].setdefault("lon_5186", lon_5186)
                        geometry[j].setdefault("lat_5186", lat_5186)
                    hole_sList.append(geometry)
        pipeDic.setdefault('straight',pipe_pipeList)
        pipeDic.setdefault('curve',pipe_curveList)
        dic.setdefault('pipe',pipeDic)
        return dic








def getDicforCreateObjFromJson_range(json,start,end):
    '''
    json데이터를
    {pipe:
        {
            straight:[{..},{..}],
            curve:[{,,},{..}]
        },
    joint:{...},
    hole:
        {
            c:[{...},{..}],
            s:[{...},{..}]
        }
    }형식으로 만드는 함수
    :param json:파이프 정보 json 데이터
    :param start:시작 group no
    :param end:종료 group no
    :return:dic
    '''

    dic={}
    pipeDic={}
    pipe_pipeList=[]
    pipe_curveList=[]
    jointList=[]
    holeDic={}
    hole_cList=[]
    hole_sList=[]
    for key, value in json.items():
      if key=="data":
        for i in range(len(value)):
            type = value[i].get('type')
            group=value[i].get('groupNo')
            if start<=group<=end:
                diameter=0
                width=0
                height=0
                if value[i].get('diameter'):
                    diameter = float(value[i].get('diameter'))
                if value[i].get('width'):
                    width=value[i].get('width')
                if value[i].get('height'):
                    height=value[i].get('height')
                if type=="line":
                    geometry=value[i].get('geometry')
                    geoList=[]
                    for j in range(len(geometry)):
                        pitch = 0
                        roll = 0
                        lon = geometry[j].get('lon')
                        lat = geometry[j].get('lat')
                        depth=geometry[j].get('depth')
                        if j == len(geometry) - 1:
                            lon_2 = geometry[j].get('lon')
                            lat_2 = geometry[j].get('lat')
                            depth_2 = geometry[j].get('depth')
                        else:
                            lon_2 = geometry[j + 1].get('lon')
                            lat_2 = geometry[j + 1].get('lat')
                            depth_2 = geometry[j + 1].get('depth')
                        lon_5186, lat_5186 = convertGeo4326To5186(lon, lat)
                        lon_5186_2, lat_5186_2 = convertGeo4326To5186(lon_2, lat_2)
                        point1 = Point(lon_5186, lat_5186, depth)
                        point2 = Point(lon_5186_2, lat_5186_2, depth_2)
                        depth = geometry[j].get('depth')
                        deltaDepth = depth_2 - depth  # 매설심도차로 파이프간 거리 계산.0.5보다 크면 매설심도 적용 후 파이프 길이 계산
                        length = point1.distance(
                            point2)  # math.sqrt(((lon_5186_2 - lon_5186) ** 2) + ((lat_5186_2 - lat_5186) ** 2))
                        x = ((lon_5186 + lon_5186_2) / 2)
                        y = ((lat_5186 + lat_5186_2) / 2)
                        if geometry[j].get('pitch'):
                            pitch = geometry[j].get('pitch')
                        else:
                            if math.fabs(deltaDepth) > 0:
                                pitch = math.atan(deltaDepth / length)
                                pitch = pitch * 180 / math.pi
                                if math.fabs(pitch) > 15:
                                    length = length + 0.3
                                depth = (depth_2 + depth) / 2
                        if geometry[j].get('roll'):
                            roll = geometry[j].get('roll')
                        a = (y - lat_5186)
                        c = (x - lon_5186)
                        if a != 0 and c != 0:
                            theta = math.atan(c / a)
                        else:
                            theta = 0
                        theta = theta * 180 / math.pi
                        geometry[j].setdefault("theta", theta)
                        geometry[j].setdefault("lon_5186", lon_5186)
                        geometry[j].setdefault("lat_5186", lat_5186)
                        geometry[j].setdefault('diameter', diameter)
                        geometry[j].setdefault('location', [x, y, depth])
                        if 90 < geometry[j].get('azimuth') < 270:
                            pitch = pitch * -1
                            length = length + 0.1
                        geometry[j].setdefault('pitch', pitch - 90)
                        geometry[j].setdefault('roll', roll)
                        geometry[j].setdefault("length", round(length, 1))
                        geometry[j].setdefault('width', width)
                        geometry[j].setdefault('height', height)
                        geometry[j].setdefault('groupNo', group)
                        geoList.append(geometry[j])
                pipe_pipeList.append(geometry)
        pipeDic.setdefault('straight',pipe_pipeList)
        dic.setdefault('pipe',pipeDic)
        return dic









