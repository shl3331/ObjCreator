import pandas
import geopandas as gpd
import obj_editor
import math
def convertGeo4326To5186(lon,lat):
  '''
  :param lon: inputLon
  :param lat: inputLat
  :return: new lon,lat
  '''
  if lat>1000 and lon>1000:
    return lon,lat
  else:
    df = pandas.DataFrame({'lat': [lat], 'lon': [lon]})
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")
    gdf_5186 = gdf.to_crs(epsg=5186)
    return float(gdf_5186.representative_point().x[0]), float(gdf_5186.representative_point().y[0])
json={
  "code": 1,
  "message": "success",
  "data": [
    {
      "groupNo": 1,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60243676,
          "lon": 126.7000258,
          "depth": 1.306,
          "azimuth": 0
        },
        {
          "lat": 37.60243824,
          "lon": 126.7000258,
          "depth": 1.306,
          "azimuth": 0
        },
        {
          "lat": 37.60244946,
          "lon": 126.7000258,
          "depth": 2.53,
          "azimuth": 0
        },
        {
          "lat": 37.60247379,
          "lon": 126.7000257,
          "depth": 2.483,
          "azimuth": 359.81
        },
        {
          "lat": 37.60248458,
          "lon": 126.7000256,
          "depth": 1.306,
          "azimuth": 359.58
        },
        {
          "lat": 37.60255783,
          "lon": 126.7000253,
          "depth": 1.306,
          "azimuth": 359.81
        },
        {
          "lat": 37.60258846,
          "lon": 126.7000252,
          "depth": 1.306,
          "azimuth": 359.85
        },
        {
          "lat": 37.60261133,
          "lon": 126.7000251,
          "depth": 1.306,
          "azimuth": 359.8
        },
        {
          "lat": 37.60266326,
          "lon": 126.7000249,
          "depth": 1.306,
          "azimuth": 359.83
        },
        {
          "lat": 37.60267381,
          "lon": 126.7000249,
          "depth": 2.737,
          "azimuth": 0
        },
        {
          "lat": 37.60269333,
          "lon": 126.7000248,
          "depth": 2.683,
          "azimuth": 359.77
        },
        {
          "lat": 37.60270347,
          "lon": 126.7000247,
          "depth": 1.306,
          "azimuth": 359.55
        },
        {
          "lat": 37.60271565,
          "lon": 126.7000247,
          "depth": 1.306,
          "azimuth": 0
        },
        {
          "lat": 37.60271257,
          "lon": 126.7000672,
          "depth": 1.306,
          "azimuth": 95.23
        },
        {
          "lat": 37.60270767,
          "lon": 126.7001349,
          "depth": 1.306,
          "azimuth": 95.22
        },
        {
          "lat": 37.60267468,
          "lon": 126.7005912,
          "depth": 1.306,
          "azimuth": 95.21
        },
        {
          "lat": 37.60265929,
          "lon": 126.700804,
          "depth": 1.306,
          "azimuth": 95.22
        },
        {
          "lat": 37.60265817,
          "lon": 126.7008194,
          "depth": 1.306,
          "azimuth": 95.24
        },
        {
          "lat": 37.60264168,
          "lon": 126.7010475,
          "depth": 1.306,
          "azimuth": 95.21
        },
        {
          "lat": 37.60262517,
          "lon": 126.7012757,
          "depth": 1.306,
          "azimuth": 95.22
        },
        {
          "lat": 37.6026244,
          "lon": 126.7012864,
          "depth": 1.306,
          "azimuth": 95.19
        },
        {
          "lat": 37.60261407,
          "lon": 126.7013538,
          "depth": 1.306,
          "azimuth": 100.95
        },
        {
          "lat": 37.60261228,
          "lon": 126.7013655,
          "depth": 2.348,
          "azimuth": 100.93
        },
        {
          "lat": 37.60260797,
          "lon": 126.7013937,
          "depth": 1.699,
          "azimuth": 100.92
        },
        {
          "lat": 37.60260728,
          "lon": 126.7013982,
          "depth": 1.306,
          "azimuth": 100.95
        },
        {
          "lat": 37.60260658,
          "lon": 126.7014079,
          "depth": 1.306,
          "azimuth": 95.2
        },
        {
          "lat": 37.60259977,
          "lon": 126.7015022,
          "depth": 1.306,
          "azimuth": 95.21
        },
        {
          "lat": 37.60259283,
          "lon": 126.7015983,
          "depth": 1.306,
          "azimuth": 95.21
        },
        {
          "lat": 37.60263021,
          "lon": 126.7016026,
          "depth": 1.306,
          "azimuth": 5.21
        },
        {
          "lat": 37.60263367,
          "lon": 126.701603,
          "depth": 1.306,
          "azimuth": 5.23
        },
        {
          "lat": 37.60264383,
          "lon": 126.7016041,
          "depth": 1.306,
          "azimuth": 4.9
        },
        {
          "lat": 37.6027981,
          "lon": 126.7016216,
          "depth": 1.306,
          "azimuth": 5.14
        },
        {
          "lat": 37.60280119,
          "lon": 126.7016219,
          "depth": 1.306,
          "azimuth": 4.4
        },
        {
          "lat": 37.60296599,
          "lon": 126.7016405,
          "depth": 1.306,
          "azimuth": 5.11
        },
        {
          "lat": 37.60302601,
          "lon": 126.7016473,
          "depth": 1.306,
          "azimuth": 5.13
        }
      ],
      "diameter": 200,
      "category": 0,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 2,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60263155,
          "lon": 126.6986787,
          "depth": 1.406,
          "azimuth": 359.73
        },
        {
          "lat": 37.6026653,
          "lon": 126.6986785,
          "depth": 1.406,
          "azimuth": 359.73
        },
        {
          "lat": 37.60270021,
          "lon": 126.6986784,
          "depth": 1.406,
          "azimuth": 359.87
        },
        {
          "lat": 37.60271639,
          "lon": 126.6986783,
          "depth": 3.157,
          "azimuth": 359.72
        },
        {
          "lat": 37.60274271,
          "lon": 126.6986782,
          "depth": 3.111,
          "azimuth": 359.83
        },
        {
          "lat": 37.60275846,
          "lon": 126.6986782,
          "depth": 1.406,
          "azimuth": 0
        },
        {
          "lat": 37.60280234,
          "lon": 126.698678,
          "depth": 1.406,
          "azimuth": 359.79
        },
        {
          "lat": 37.60284707,
          "lon": 126.6986778,
          "depth": 1.406,
          "azimuth": 359.8
        },
        {
          "lat": 37.60287274,
          "lon": 126.6986777,
          "depth": 1.406,
          "azimuth": 359.82
        },
        {
          "lat": 37.6029734,
          "lon": 126.6986773,
          "depth": 1.406,
          "azimuth": 359.82
        },
        {
          "lat": 37.60299541,
          "lon": 126.6986772,
          "depth": 1.406,
          "azimuth": 359.79
        },
        {
          "lat": 37.6030283,
          "lon": 126.6986771,
          "depth": 1.406,
          "azimuth": 359.86
        },
        {
          "lat": 37.60320979,
          "lon": 126.6986763,
          "depth": 1.406,
          "azimuth": 359.8
        },
        {
          "lat": 37.60321471,
          "lon": 126.6986763,
          "depth": 1.406,
          "azimuth": 0
        },
        {
          "lat": 37.6033044,
          "lon": 126.6986391,
          "depth": 1.406,
          "azimuth": 341.81
        },
        {
          "lat": 37.60330975,
          "lon": 126.6986369,
          "depth": 2.016,
          "azimuth": 341.96
        },
        {
          "lat": 37.60332957,
          "lon": 126.6986287,
          "depth": 2.143,
          "azimuth": 341.85
        },
        {
          "lat": 37.60333603,
          "lon": 126.698626,
          "depth": 1.406,
          "azimuth": 341.68
        },
        {
          "lat": 37.60334144,
          "lon": 126.6986237,
          "depth": 1.406,
          "azimuth": 341.39
        },
        {
          "lat": 37.60338456,
          "lon": 126.6986236,
          "depth": 1.406,
          "azimuth": 359.89
        },
        {
          "lat": 37.60356607,
          "lon": 126.6986228,
          "depth": 1.406,
          "azimuth": 359.8
        },
        {
          "lat": 37.60361821,
          "lon": 126.6986226,
          "depth": 1.406,
          "azimuth": 359.83
        },
        {
          "lat": 37.6036796,
          "lon": 126.6986224,
          "depth": 1.406,
          "azimuth": 359.85
        },
        {
          "lat": 37.60368411,
          "lon": 126.6986224,
          "depth": 1.406,
          "azimuth": 0
        },
        {
          "lat": 37.60371075,
          "lon": 126.6986223,
          "depth": 1.406,
          "azimuth": 359.83
        },
        {
          "lat": 37.60372026,
          "lon": 126.6986222,
          "depth": 1.406,
          "azimuth": 359.52
        },
        {
          "lat": 37.6037315,
          "lon": 126.6986222,
          "depth": 2.629,
          "azimuth": 0
        },
        {
          "lat": 37.60375769,
          "lon": 126.6986221,
          "depth": 2.699,
          "azimuth": 359.83
        },
        {
          "lat": 37.60376958,
          "lon": 126.698622,
          "depth": 1.406,
          "azimuth": 359.62
        },
        {
          "lat": 37.60377854,
          "lon": 126.698622,
          "depth": 1.406,
          "azimuth": 0
        },
        {
          "lat": 37.60380174,
          "lon": 126.6986219,
          "depth": 1.406,
          "azimuth": 359.8
        },
        {
          "lat": 37.60387004,
          "lon": 126.6986216,
          "depth": 1.406,
          "azimuth": 359.8
        },
        {
          "lat": 37.60388215,
          "lon": 126.6986216,
          "depth": 1.406,
          "azimuth": 0
        },
        {
          "lat": 37.60392817,
          "lon": 126.6986214,
          "depth": 1.406,
          "azimuth": 359.8
        },
        {
          "lat": 37.60410876,
          "lon": 126.6986207,
          "depth": 1.406,
          "azimuth": 359.82
        },
        {
          "lat": 37.60430618,
          "lon": 126.6986199,
          "depth": 1.406,
          "azimuth": 359.82
        },
        {
          "lat": 37.60434693,
          "lon": 126.6986299,
          "depth": 1.406,
          "azimuth": 11
        },
        {
          "lat": 37.60444142,
          "lon": 126.6986533,
          "depth": 1.406,
          "azimuth": 11.1
        },
        {
          "lat": 37.60479236,
          "lon": 126.6986519,
          "depth": 1.406,
          "azimuth": 359.82
        },
        {
          "lat": 37.60480761,
          "lon": 126.6986518,
          "depth": 3.064,
          "azimuth": 359.7
        },
        {
          "lat": 37.6048356,
          "lon": 126.6986517,
          "depth": 3.131,
          "azimuth": 359.84
        },
        {
          "lat": 37.60485147,
          "lon": 126.6986516,
          "depth": 1.406,
          "azimuth": 359.71
        },
        {
          "lat": 37.60528745,
          "lon": 126.6986499,
          "depth": 1.406,
          "azimuth": 359.82
        },
        {
          "lat": 37.60537013,
          "lon": 126.6986427,
          "depth": 1.406,
          "azimuth": 356.05
        },
        {
          "lat": 37.60542436,
          "lon": 126.698638,
          "depth": 1.406,
          "azimuth": 356.07
        },
        {
          "lat": 37.60546092,
          "lon": 126.6986378,
          "depth": 1.406,
          "azimuth": 359.75
        },
        {
          "lat": 37.605514,
          "lon": 126.6986376,
          "depth": 1.406,
          "azimuth": 359.83
        },
        {
          "lat": 37.60560404,
          "lon": 126.6986146,
          "depth": 1.406,
          "azimuth": 348.56
        },
        {
          "lat": 37.60596467,
          "lon": 126.6986132,
          "depth": 1.406,
          "azimuth": 359.82
        }
      ],
      "diameter": 400,
      "category": 0,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 3,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60790661,
          "lon": 126.6959578,
          "depth": 1.256,
          "azimuth": 240.63
        },
        {
          "lat": 37.60790554,
          "lon": 126.6959554,
          "depth": 1.256,
          "azimuth": 240.63
        },
        {
          "lat": 37.60790139,
          "lon": 126.6959462,
          "depth": 1.256,
          "azimuth": 240.34
        },
        {
          "lat": 37.60789051,
          "lon": 126.6959221,
          "depth": 1.256,
          "azimuth": 240.32
        },
        {
          "lat": 37.60788572,
          "lon": 126.6959115,
          "depth": 1.256,
          "azimuth": 240.3
        },
        {
          "lat": 37.60772756,
          "lon": 126.6955608,
          "depth": 1.256,
          "azimuth": 240.35
        },
        {
          "lat": 37.60770318,
          "lon": 126.6955067,
          "depth": 1.256,
          "azimuth": 240.37
        },
        {
          "lat": 37.60770216,
          "lon": 126.6955044,
          "depth": 1.256,
          "azimuth": 240.76
        },
        {
          "lat": 37.60769792,
          "lon": 126.695495,
          "depth": 1.256,
          "azimuth": 240.34
        },
        {
          "lat": 37.60768704,
          "lon": 126.6954709,
          "depth": 1.256,
          "azimuth": 240.32
        },
        {
          "lat": 37.60768224,
          "lon": 126.6954602,
          "depth": 1.256,
          "azimuth": 240.48
        },
        {
          "lat": 37.60749926,
          "lon": 126.6950545,
          "depth": 1.256,
          "azimuth": 240.35
        },
        {
          "lat": 37.60799029,
          "lon": 126.6947132,
          "depth": 1.256,
          "azimuth": 331.16
        },
        {
          "lat": 37.60800095,
          "lon": 126.6947058,
          "depth": 1.256,
          "azimuth": 331.19
        }
      ],
      "diameter": 100,
      "category": 0,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 4,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60790661,
          "lon": 126.6959578,
          "depth": 1.256,
          "azimuth": 331.04
        },
        {
          "lat": 37.60791835,
          "lon": 126.6959496,
          "depth": 1.256,
          "azimuth": 331.04
        },
        {
          "lat": 37.6080445,
          "lon": 126.695862,
          "depth": 1.256,
          "azimuth": 331.18
        },
        {
          "lat": 37.60839638,
          "lon": 126.6956174,
          "depth": 1.256,
          "azimuth": 331.16
        },
        {
          "lat": 37.60840833,
          "lon": 126.6956091,
          "depth": 1.256,
          "azimuth": 331.18
        },
        {
          "lat": 37.60840834,
          "lon": 126.6956091,
          "depth": 1.256,
          "azimuth": 0
        },
        {
          "lat": 37.60840662,
          "lon": 126.6956053,
          "depth": 1.256,
          "azimuth": 240.26
        },
        {
          "lat": 37.60822889,
          "lon": 126.6952112,
          "depth": 1.256,
          "azimuth": 240.35
        },
        {
          "lat": 37.6082049,
          "lon": 126.695158,
          "depth": 1.256,
          "azimuth": 240.35
        },
        {
          "lat": 37.60819383,
          "lon": 126.6951335,
          "depth": 1.256,
          "azimuth": 240.3
        },
        {
          "lat": 37.60805116,
          "lon": 126.6948171,
          "depth": 1.256,
          "azimuth": 240.35
        },
        {
          "lat": 37.60800095,
          "lon": 126.6947058,
          "depth": 1.256,
          "azimuth": 240.34
        }
      ],
      "diameter": 100,
      "category": 0,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 5,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60770318,
          "lon": 126.6955067,
          "depth": 1.256,
          "azimuth": 331.02
        },
        {
          "lat": 37.60771491,
          "lon": 126.6954985,
          "depth": 1.256,
          "azimuth": 331.02
        },
        {
          "lat": 37.60784108,
          "lon": 126.6954108,
          "depth": 1.256,
          "azimuth": 331.16
        },
        {
          "lat": 37.60819294,
          "lon": 126.6951663,
          "depth": 1.256,
          "azimuth": 331.17
        },
        {
          "lat": 37.6082049,
          "lon": 126.695158,
          "depth": 1.256,
          "azimuth": 331.2
        }
      ],
      "diameter": 100,
      "category": 0,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 6,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371075,
          "lon": 126.6986223,
          "depth": 1.356,
          "azimuth": 269.81
        },
        {
          "lat": 37.60371062,
          "lon": 126.6985733,
          "depth": 1.356,
          "azimuth": 269.81
        },
        {
          "lat": 37.60371054,
          "lon": 126.698542,
          "depth": 4.124,
          "azimuth": 269.82
        },
        {
          "lat": 37.60371043,
          "lon": 126.6984987,
          "depth": 4.063,
          "azimuth": 269.82
        },
        {
          "lat": 37.60371035,
          "lon": 126.6984681,
          "depth": 1.356,
          "azimuth": 269.81
        },
        {
          "lat": 37.60371023,
          "lon": 126.6984184,
          "depth": 1.356,
          "azimuth": 269.83
        },
        {
          "lat": 37.60372253,
          "lon": 126.6984184,
          "depth": 1.356,
          "azimuth": 0
        },
        {
          "lat": 37.6037323,
          "lon": 126.6984183,
          "depth": 2.42,
          "azimuth": 359.54
        },
        {
          "lat": 37.60375572,
          "lon": 126.6984182,
          "depth": 2.491,
          "azimuth": 359.81
        },
        {
          "lat": 37.60376613,
          "lon": 126.6984182,
          "depth": 1.356,
          "azimuth": 0
        },
        {
          "lat": 37.60377792,
          "lon": 126.6984181,
          "depth": 1.356,
          "azimuth": 359.61
        },
        {
          "lat": 37.60380118,
          "lon": 126.698418,
          "depth": 1.356,
          "azimuth": 359.8
        },
        {
          "lat": 37.60385964,
          "lon": 126.6984178,
          "depth": 1.356,
          "azimuth": 359.84
        },
        {
          "lat": 37.60386989,
          "lon": 126.6984178,
          "depth": 2.47,
          "azimuth": 0
        },
        {
          "lat": 37.60389338,
          "lon": 126.6984177,
          "depth": 2.585,
          "azimuth": 359.81
        },
        {
          "lat": 37.60390469,
          "lon": 126.6984176,
          "depth": 1.356,
          "azimuth": 359.6
        },
        {
          "lat": 37.60392773,
          "lon": 126.6984175,
          "depth": 1.356,
          "azimuth": 359.8
        },
        {
          "lat": 37.60410848,
          "lon": 126.6984168,
          "depth": 1.356,
          "azimuth": 359.82
        },
        {
          "lat": 37.60421267,
          "lon": 126.6984164,
          "depth": 1.356,
          "azimuth": 359.83
        },
        {
          "lat": 37.6042877,
          "lon": 126.6983973,
          "depth": 1.356,
          "azimuth": 348.6
        },
        {
          "lat": 37.60430285,
          "lon": 126.6983934,
          "depth": 1.356,
          "azimuth": 348.47
        },
        {
          "lat": 37.6043484,
          "lon": 126.6983819,
          "depth": 1.356,
          "azimuth": 348.69
        },
        {
          "lat": 37.60480811,
          "lon": 126.69838,
          "depth": 1.356,
          "azimuth": 359.81
        },
        {
          "lat": 37.60482248,
          "lon": 126.6983799,
          "depth": 2.917,
          "azimuth": 359.68
        },
        {
          "lat": 37.60484959,
          "lon": 126.6983798,
          "depth": 2.981,
          "azimuth": 359.83
        },
        {
          "lat": 37.60486454,
          "lon": 126.6983798,
          "depth": 1.356,
          "azimuth": 0
        },
        {
          "lat": 37.60552256,
          "lon": 126.6983771,
          "depth": 1.356,
          "azimuth": 359.81
        },
        {
          "lat": 37.60596406,
          "lon": 126.6983753,
          "depth": 1.356,
          "azimuth": 359.81
        }
      ],
      "diameter": 300,
      "category": 0,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 7,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60786643,
          "lon": 126.6947346,
          "depth": 2.16,
          "azimuth": 151.16
        },
        {
          "lat": 37.60744116,
          "lon": 126.6950302,
          "depth": 1.66,
          "azimuth": 151.16
        },
        {
          "lat": 37.60743961,
          "lon": 126.6950371,
          "depth": 2.16,
          "azimuth": 105.83
        },
        {
          "lat": 37.60764006,
          "lon": 126.6954815,
          "depth": 1.67,
          "azimuth": 60.34
        },
        {
          "lat": 37.60764406,
          "lon": 126.6954904,
          "depth": 2.67,
          "azimuth": 60.43
        },
        {
          "lat": 37.60784356,
          "lon": 126.6959328,
          "depth": 2.17,
          "azimuth": 60.35
        },
        {
          "lat": 37.60784755,
          "lon": 126.6959416,
          "depth": 2.67,
          "azimuth": 60.22
        },
        {
          "lat": 37.60804703,
          "lon": 126.696384,
          "depth": 2.17,
          "azimuth": 60.35
        },
        {
          "lat": 37.60805104,
          "lon": 126.6963928,
          "depth": 2.67,
          "azimuth": 60.09
        },
        {
          "lat": 37.60825052,
          "lon": 126.6968352,
          "depth": 2.16,
          "azimuth": 60.35
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 8,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60806995,
          "lon": 126.6951845,
          "depth": 2.16,
          "azimuth": 150.83
        },
        {
          "lat": 37.60764574,
          "lon": 126.6954834,
          "depth": 2.169,
          "azimuth": 150.83
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 9,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60827345,
          "lon": 126.6956357,
          "depth": 2.17,
          "azimuth": 150.83
        },
        {
          "lat": 37.60784925,
          "lon": 126.6959346,
          "depth": 2.169,
          "azimuth": 150.83
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 10,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60471023,
          "lon": 126.6986667,
          "depth": 4.16,
          "azimuth": 269.82
        },
        {
          "lat": 37.60470946,
          "lon": 126.6983655,
          "depth": 4.26,
          "azimuth": 269.82
        },
        {
          "lat": 37.60470539,
          "lon": 126.6983604,
          "depth": 4.26,
          "azimuth": 224.79
        },
        {
          "lat": 37.60435004,
          "lon": 126.6983618,
          "depth": 4.01,
          "azimuth": 179.82
        },
        {
          "lat": 37.60434201,
          "lon": 126.6983629,
          "depth": 4.01,
          "azimuth": 173.81
        },
        {
          "lat": 37.6042149,
          "lon": 126.6983954,
          "depth": 3.9,
          "azimuth": 168.55
        },
        {
          "lat": 37.60420687,
          "lon": 126.6983964,
          "depth": 3.9,
          "azimuth": 174.37
        },
        {
          "lat": 37.6038418,
          "lon": 126.6983979,
          "depth": 3.6,
          "azimuth": 179.81
        },
        {
          "lat": 37.60383372,
          "lon": 126.6983972,
          "depth": 3.65,
          "azimuth": 183.93
        },
        {
          "lat": 37.60362181,
          "lon": 126.6983598,
          "depth": 3.09,
          "azimuth": 187.96
        },
        {
          "lat": 37.60361375,
          "lon": 126.6983591,
          "depth": 3.09,
          "azimuth": 183.94
        },
        {
          "lat": 37.60332834,
          "lon": 126.6983602,
          "depth": 2.34,
          "azimuth": 179.83
        },
        {
          "lat": 37.60332041,
          "lon": 126.6983587,
          "depth": 2.34,
          "azimuth": 188.52
        },
        {
          "lat": 37.603252,
          "lon": 126.6983321,
          "depth": 2.17,
          "azimuth": 197.12
        },
        {
          "lat": 37.60324406,
          "lon": 126.6983306,
          "depth": 2.17,
          "azimuth": 188.51
        },
        {
          "lat": 37.60289415,
          "lon": 126.698333,
          "depth": 1.27,
          "azimuth": 179.69
        },
        {
          "lat": 37.60288605,
          "lon": 126.6983333,
          "depth": 2.77,
          "azimuth": 178.32
        },
        {
          "lat": 37.60261928,
          "lon": 126.6983505,
          "depth": 2.96,
          "azimuth": 177.08
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 11,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6034726,
          "lon": 126.6986428,
          "depth": 1.66,
          "azimuth": 179.81
        },
        {
          "lat": 37.60332907,
          "lon": 126.6986434,
          "depth": 1.17,
          "azimuth": 179.81
        },
        {
          "lat": 37.60332381,
          "lon": 126.6986385,
          "depth": 1.17,
          "azimuth": 216.43
        },
        {
          "lat": 37.60324932,
          "lon": 126.6983355,
          "depth": 1.16,
          "azimuth": 252.76
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 12,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60365129,
          "lon": 126.7005447,
          "depth": 1.67,
          "azimuth": 275.16
        },
        {
          "lat": 37.60367066,
          "lon": 126.700274,
          "depth": 1.524,
          "azimuth": 275.16
        },
        {
          "lat": 37.6036746,
          "lon": 126.7002063,
          "depth": 1.486,
          "azimuth": 274.2
        },
        {
          "lat": 37.60368678,
          "lon": 126.6998837,
          "depth": 1.26,
          "azimuth": 272.73
        },
        {
          "lat": 37.60368679,
          "lon": 126.6998735,
          "depth": 1.66,
          "azimuth": 270.07
        },
        {
          "lat": 37.60368664,
          "lon": 126.6998056,
          "depth": 1.604,
          "azimuth": 269.84
        },
        {
          "lat": 37.60368507,
          "lon": 126.6992818,
          "depth": 1.27,
          "azimuth": 269.78
        },
        {
          "lat": 37.603681,
          "lon": 126.6992767,
          "depth": 3.16,
          "azimuth": 224.79
        },
        {
          "lat": 37.60323861,
          "lon": 126.699278,
          "depth": 1.66,
          "azimuth": 179.87
        },
        {
          "lat": 37.60323081,
          "lon": 126.699276,
          "depth": 2.77,
          "azimuth": 191.48
        },
        {
          "lat": 37.60309705,
          "lon": 126.6992062,
          "depth": 2.76,
          "azimuth": 202.46
        },
        {
          "lat": 37.60308925,
          "lon": 126.6992043,
          "depth": 2.76,
          "azimuth": 190.92
        },
        {
          "lat": 37.60285105,
          "lon": 126.6992059,
          "depth": 1.26,
          "azimuth": 179.7
        },
        {
          "lat": 37.60284589,
          "lon": 126.6992108,
          "depth": 1.26,
          "azimuth": 143.04
        },
        {
          "lat": 37.60276243,
          "lon": 126.6995754,
          "depth": 2.66,
          "azimuth": 106.12
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 13,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60343353,
          "lon": 126.7017273,
          "depth": 1.67,
          "azimuth": 185.11
        },
        {
          "lat": 37.60312097,
          "lon": 126.701692,
          "depth": 1.26,
          "azimuth": 185.11
        },
        {
          "lat": 37.6031173,
          "lon": 126.7016865,
          "depth": 2.76,
          "azimuth": 229.89
        },
        {
          "lat": 37.60313324,
          "lon": 126.7014637,
          "depth": 2.27,
          "azimuth": 275.16
        },
        {
          "lat": 37.60313396,
          "lon": 126.7014535,
          "depth": 2.27,
          "azimuth": 275.09
        },
        {
          "lat": 37.60316843,
          "lon": 126.7009718,
          "depth": 1.27,
          "azimuth": 275.16
        },
        {
          "lat": 37.60316916,
          "lon": 126.7009616,
          "depth": 1.37,
          "azimuth": 275.16
        },
        {
          "lat": 37.60321684,
          "lon": 126.700295,
          "depth": 1.27,
          "azimuth": 275.16
        },
        {
          "lat": 37.60321757,
          "lon": 126.7002849,
          "depth": 1.37,
          "azimuth": 275.21
        },
        {
          "lat": 37.60322241,
          "lon": 126.7002172,
          "depth": 1.345,
          "azimuth": 275.16
        },
        {
          "lat": 37.60322598,
          "lon": 126.7001495,
          "depth": 1.332,
          "azimuth": 273.81
        },
        {
          "lat": 37.60323625,
          "lon": 126.6998358,
          "depth": 1.26,
          "azimuth": 272.37
        },
        {
          "lat": 37.60323621,
          "lon": 126.6998256,
          "depth": 1.26,
          "azimuth": 269.72
        },
        {
          "lat": 37.60323457,
          "lon": 126.6992831,
          "depth": 1.27,
          "azimuth": 269.78
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 14,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60263951,
          "lon": 126.7012844,
          "depth": 1.67,
          "azimuth": 275.19
        },
        {
          "lat": 37.60267928,
          "lon": 126.7007314,
          "depth": 1.26,
          "azimuth": 275.19
        },
        {
          "lat": 37.60268001,
          "lon": 126.7007212,
          "depth": 1.76,
          "azimuth": 275.16
        },
        {
          "lat": 37.60271977,
          "lon": 126.7001682,
          "depth": 1.27,
          "azimuth": 275.19
        },
        {
          "lat": 37.60272049,
          "lon": 126.700158,
          "depth": 1.77,
          "azimuth": 275.09
        },
        {
          "lat": 37.60276095,
          "lon": 126.6995854,
          "depth": 1.27,
          "azimuth": 275.1
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 15,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60275727,
          "lon": 126.6995799,
          "depth": 4.14,
          "azimuth": 184.45
        },
        {
          "lat": 37.60256999,
          "lon": 126.6995615,
          "depth": 4.14,
          "azimuth": 184.45
        },
        {
          "lat": 37.60256626,
          "lon": 126.699556,
          "depth": 4.14,
          "azimuth": 229.44
        },
        {
          "lat": 37.60260491,
          "lon": 126.6987438,
          "depth": 2.68,
          "azimuth": 273.44
        },
        {
          "lat": 37.60260525,
          "lon": 126.6987336,
          "depth": 3.18,
          "azimuth": 272.41
        },
        {
          "lat": 37.60261001,
          "lon": 126.6985748,
          "depth": 3.39,
          "azimuth": 272.17
        },
        {
          "lat": 37.6026103,
          "lon": 126.6985646,
          "depth": 4.69,
          "azimuth": 272.06
        },
        {
          "lat": 37.60261513,
          "lon": 126.6983559,
          "depth": 4.43,
          "azimuth": 271.67
        },
        {
          "lat": 37.60261533,
          "lon": 126.6983457,
          "depth": 1.96,
          "azimuth": 271.42
        },
        {
          "lat": 37.6026205,
          "lon": 126.6978479,
          "depth": 3.07,
          "azimuth": 270.75
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 16,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60286829,
          "lon": 126.6987435,
          "depth": 2.94,
          "azimuth": 180.82
        },
        {
          "lat": 37.60260913,
          "lon": 126.6987388,
          "depth": 3.18,
          "azimuth": 180.82
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 17,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6026061,
          "lon": 126.6985698,
          "depth": 4.69,
          "azimuth": 179.79
        },
        {
          "lat": 37.60224583,
          "lon": 126.6985715,
          "depth": 3.55,
          "azimuth": 179.79
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 18,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60367627,
          "lon": 126.6963868,
          "depth": 3.17,
          "azimuth": 89.78
        },
        {
          "lat": 37.60367861,
          "lon": 126.6971562,
          "depth": 1.26,
          "azimuth": 89.78
        },
        {
          "lat": 37.60367865,
          "lon": 126.6971664,
          "depth": 2.76,
          "azimuth": 89.72
        },
        {
          "lat": 37.60368045,
          "lon": 126.6977593,
          "depth": 1.26,
          "azimuth": 89.78
        },
        {
          "lat": 37.60367641,
          "lon": 126.6977644,
          "depth": 3.16,
          "azimuth": 135
        },
        {
          "lat": 37.60323403,
          "lon": 126.6977661,
          "depth": 1.26,
          "azimuth": 179.83
        },
        {
          "lat": 37.60322625,
          "lon": 126.6977681,
          "depth": 2.67,
          "azimuth": 168.49
        },
        {
          "lat": 37.6030929,
          "lon": 126.697839,
          "depth": 2.67,
          "azimuth": 157.16
        },
        {
          "lat": 37.60308511,
          "lon": 126.697841,
          "depth": 2.67,
          "azimuth": 168.5
        },
        {
          "lat": 37.60287782,
          "lon": 126.6978412,
          "depth": 1.26,
          "azimuth": 179.96
        },
        {
          "lat": 37.60286971,
          "lon": 126.6978412,
          "depth": 2.76,
          "azimuth": 180
        },
        {
          "lat": 37.60262456,
          "lon": 126.6978428,
          "depth": 3.07,
          "azimuth": 179.7
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 19,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60322553,
          "lon": 126.6963041,
          "depth": 2.67,
          "azimuth": 89.78
        },
        {
          "lat": 37.60322791,
          "lon": 126.6970867,
          "depth": 1.27,
          "azimuth": 89.78
        },
        {
          "lat": 37.60322794,
          "lon": 126.6970968,
          "depth": 2.17,
          "azimuth": 89.79
        },
        {
          "lat": 37.60322996,
          "lon": 126.6977611,
          "depth": 1.27,
          "azimuth": 89.78
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 20,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60281538,
          "lon": 126.6960495,
          "depth": 2.66,
          "azimuth": 89.95
        },
        {
          "lat": 37.60281566,
          "lon": 126.6964923,
          "depth": 1.26,
          "azimuth": 89.95
        },
        {
          "lat": 37.60281567,
          "lon": 126.6965025,
          "depth": 2.66,
          "azimuth": 89.93
        },
        {
          "lat": 37.60281598,
          "lon": 126.6969916,
          "depth": 1.27,
          "azimuth": 89.95
        },
        {
          "lat": 37.60281648,
          "lon": 126.6970018,
          "depth": 2.97,
          "azimuth": 86.46
        },
        {
          "lat": 37.60287393,
          "lon": 126.6976013,
          "depth": 1.27,
          "azimuth": 83.1
        },
        {
          "lat": 37.6028744,
          "lon": 126.6976114,
          "depth": 1.97,
          "azimuth": 86.64
        },
        {
          "lat": 37.60287378,
          "lon": 126.6978361,
          "depth": 1.27,
          "azimuth": 90.2
        }
      ],
      "diameter": 300,
      "category": 2,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 21,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60790634,
          "lon": 126.6947392,
          "depth": 1.855,
          "azimuth": 151.16
        },
        {
          "lat": 37.60747316,
          "lon": 126.6950403,
          "depth": 1.455,
          "azimuth": 151.16
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 22,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60747111,
          "lon": 126.6950495,
          "depth": 1.785,
          "azimuth": 60.34
        },
        {
          "lat": 37.60767016,
          "lon": 126.6954908,
          "depth": 1.465,
          "azimuth": 60.34
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 23,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60810755,
          "lon": 126.6951905,
          "depth": 1.975,
          "azimuth": 150.84
        },
        {
          "lat": 37.60767753,
          "lon": 126.6954934,
          "depth": 1.565,
          "azimuth": 150.84
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 24,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60767549,
          "lon": 126.6955027,
          "depth": 1.96,
          "azimuth": 60.35
        },
        {
          "lat": 37.60787365,
          "lon": 126.6959421,
          "depth": 1.5,
          "azimuth": 60.35
        }
      ],
      "diameter": 500,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 25,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60787897,
          "lon": 126.6959539,
          "depth": 2.24,
          "azimuth": 60.35
        },
        {
          "lat": 37.60807713,
          "lon": 126.6963933,
          "depth": 1.55,
          "azimuth": 60.35
        },
        {
          "lat": 37.60808246,
          "lon": 126.6964051,
          "depth": 2.2,
          "azimuth": 60.31
        },
        {
          "lat": 37.60828061,
          "lon": 126.6968445,
          "depth": 1.55,
          "azimuth": 60.35
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 26,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60602432,
          "lon": 126.698511,
          "depth": 2.414,
          "azimuth": 179.82
        },
        {
          "lat": 37.60518923,
          "lon": 126.6985144,
          "depth": 2.25,
          "azimuth": 179.82
        }
      ],
      "diameter": 1100,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 27,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60372529,
          "lon": 126.6962618,
          "depth": 2.995,
          "azimuth": 82.4
        },
        {
          "lat": 37.60373715,
          "lon": 126.696374,
          "depth": 2.72,
          "azimuth": 82.4
        },
        {
          "lat": 37.60373801,
          "lon": 126.6964022,
          "depth": 2.657,
          "azimuth": 87.8
        },
        {
          "lat": 37.60373962,
          "lon": 126.6969297,
          "depth": 1.465,
          "azimuth": 89.78
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 28,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60373965,
          "lon": 126.6969399,
          "depth": 2.87,
          "azimuth": 89.78
        },
        {
          "lat": 37.60374135,
          "lon": 126.6974959,
          "depth": 1.49,
          "azimuth": 89.78
        },
        {
          "lat": 37.60374139,
          "lon": 126.6975061,
          "depth": 2.86,
          "azimuth": 89.72
        },
        {
          "lat": 37.60374307,
          "lon": 126.6980604,
          "depth": 1.49,
          "azimuth": 89.78
        }
      ],
      "diameter": 500,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 29,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60374311,
          "lon": 126.698074,
          "depth": 2.24,
          "azimuth": 89.78
        },
        {
          "lat": 37.60374442,
          "lon": 126.6985117,
          "depth": 1.883,
          "azimuth": 89.78
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 30,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60364819,
          "lon": 126.7014541,
          "depth": 1.63,
          "azimuth": 275.16
        },
        {
          "lat": 37.60368769,
          "lon": 126.700902,
          "depth": 1.49,
          "azimuth": 275.16
        }
      ],
      "diameter": 500,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 31,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60368865,
          "lon": 126.7008884,
          "depth": 2.12,
          "azimuth": 275.16
        },
        {
          "lat": 37.60373503,
          "lon": 126.7002402,
          "depth": 1.636,
          "azimuth": 275.16
        },
        {
          "lat": 37.60374262,
          "lon": 126.7001123,
          "depth": 1.55,
          "azimuth": 274.28
        },
        {
          "lat": 37.60374324,
          "lon": 126.7000987,
          "depth": 2.1,
          "azimuth": 273.29
        },
        {
          "lat": 37.60374846,
          "lon": 126.6998472,
          "depth": 1.899,
          "azimuth": 271.5
        },
        {
          "lat": 37.603747,
          "lon": 126.6993639,
          "depth": 1.55,
          "azimuth": 269.78
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 32,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60374696,
          "lon": 126.6993503,
          "depth": 2.22,
          "azimuth": 269.78
        },
        {
          "lat": 37.60374447,
          "lon": 126.6985287,
          "depth": 1.942,
          "azimuth": 269.78
        }
      ],
      "diameter": 700,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 33,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60343985,
          "lon": 126.7016514,
          "depth": 1.615,
          "azimuth": 185.11
        },
        {
          "lat": 37.60306671,
          "lon": 126.7016093,
          "depth": 1.465,
          "azimuth": 185.11
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 34,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60306304,
          "lon": 126.7016037,
          "depth": 1.745,
          "azimuth": 275.16
        },
        {
          "lat": 37.60312284,
          "lon": 126.700768,
          "depth": 1.455,
          "azimuth": 275.16
        },
        {
          "lat": 37.60312356,
          "lon": 126.7007578,
          "depth": 1.745,
          "azimuth": 275.09
        },
        {
          "lat": 37.60316389,
          "lon": 126.7001941,
          "depth": 1.539,
          "azimuth": 275.16
        },
        {
          "lat": 37.60316566,
          "lon": 126.7001658,
          "depth": 1.53,
          "azimuth": 274.51
        },
        {
          "lat": 37.60317556,
          "lon": 126.6999495,
          "depth": 1.465,
          "azimuth": 273.31
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 35,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60317565,
          "lon": 126.6999393,
          "depth": 1.49,
          "azimuth": 270.55
        },
        {
          "lat": 37.6031763,
          "lon": 126.6998544,
          "depth": 1.488,
          "azimuth": 270.55
        },
        {
          "lat": 37.60317627,
          "lon": 126.6998261,
          "depth": 1.489,
          "azimuth": 269.92
        },
        {
          "lat": 37.6031743,
          "lon": 126.699172,
          "depth": 1.49,
          "azimuth": 269.78
        }
      ],
      "diameter": 500,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 36,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6035707,
          "lon": 126.6992,
          "depth": 1.715,
          "azimuth": 183.99
        },
        {
          "lat": 37.60317968,
          "lon": 126.6991656,
          "depth": 1.455,
          "azimuth": 183.99
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 37,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60316888,
          "lon": 126.6991652,
          "depth": 2.83,
          "azimuth": 179.81
        },
        {
          "lat": 37.60285411,
          "lon": 126.6991665,
          "depth": 1.55,
          "azimuth": 179.81
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 38,
      "type": "line",
      "geometry": [
        {
          "lat": 37.602849,
          "lon": 126.6991597,
          "depth": 1.57,
          "azimuth": 273.2
        },
        {
          "lat": 37.60285391,
          "lon": 126.6990487,
          "depth": 1.55,
          "azimuth": 273.2
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 39,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60284881,
          "lon": 126.6990416,
          "depth": 1.58,
          "azimuth": 182.47
        },
        {
          "lat": 37.60272745,
          "lon": 126.699035,
          "depth": 1.51,
          "azimuth": 182.47
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 40,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60242708,
          "lon": 126.7027783,
          "depth": 2.59,
          "azimuth": 280.18
        },
        {
          "lat": 37.6025041,
          "lon": 126.702237,
          "depth": 1.55,
          "azimuth": 280.18
        },
        {
          "lat": 37.60250563,
          "lon": 126.7022235,
          "depth": 2.42,
          "azimuth": 278.14
        },
        {
          "lat": 37.60254203,
          "lon": 126.7018298,
          "depth": 1.807,
          "azimuth": 276.66
        },
        {
          "lat": 37.60254422,
          "lon": 126.7018017,
          "depth": 1.767,
          "azimuth": 275.62
        },
        {
          "lat": 37.60255423,
          "lon": 126.701663,
          "depth": 1.55,
          "azimuth": 275.2
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 41,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60255521,
          "lon": 126.7016495,
          "depth": 2.73,
          "azimuth": 275.21
        },
        {
          "lat": 37.60257367,
          "lon": 126.7013938,
          "depth": 2.149,
          "azimuth": 275.21
        },
        {
          "lat": 37.60258247,
          "lon": 126.7012831,
          "depth": 1.908,
          "azimuth": 275.73
        },
        {
          "lat": 37.6025846,
          "lon": 126.7012549,
          "depth": 1.848,
          "azimuth": 275.45
        },
        {
          "lat": 37.60259198,
          "lon": 126.7011529,
          "depth": 1.61,
          "azimuth": 275.22
        },
        {
          "lat": 37.60259296,
          "lon": 126.7011394,
          "depth": 2.7,
          "azimuth": 275.24
        },
        {
          "lat": 37.60263279,
          "lon": 126.7005886,
          "depth": 1.61,
          "azimuth": 275.22
        },
        {
          "lat": 37.6026339,
          "lon": 126.7005751,
          "depth": 2.93,
          "azimuth": 275.93
        },
        {
          "lat": 37.60268202,
          "lon": 126.6999097,
          "depth": 1.61,
          "azimuth": 275.22
        }
      ],
      "diameter": 700,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 42,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60268269,
          "lon": 126.6998962,
          "depth": 3.36,
          "azimuth": 273.3
        },
        {
          "lat": 37.60271354,
          "lon": 126.6992213,
          "depth": 3.6,
          "azimuth": 273.3
        },
        {
          "lat": 37.60272175,
          "lon": 126.6990415,
          "depth": 1.67,
          "azimuth": 273.3
        }
      ],
      "diameter": 800,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 43,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60272204,
          "lon": 126.6990279,
          "depth": 1.75,
          "azimuth": 271.38
        },
        {
          "lat": 37.60273145,
          "lon": 126.6985356,
          "depth": 1.932,
          "azimuth": 271.38
        }
      ],
      "diameter": 900,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 44,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60213525,
          "lon": 126.7024266,
          "depth": 2.005,
          "azimuth": 286.86
        },
        {
          "lat": 37.60222548,
          "lon": 126.7020508,
          "depth": 1.565,
          "azimuth": 286.86
        },
        {
          "lat": 37.60222782,
          "lon": 126.7020411,
          "depth": 2.035,
          "azimuth": 286.93
        },
        {
          "lat": 37.60232668,
          "lon": 126.7016295,
          "depth": 1.565,
          "azimuth": 286.87
        },
        {
          "lat": 37.60232854,
          "lon": 126.7016195,
          "depth": 2.235,
          "azimuth": 283.21
        },
        {
          "lat": 37.60240533,
          "lon": 126.7010077,
          "depth": 1.565,
          "azimuth": 279
        },
        {
          "lat": 37.60240687,
          "lon": 126.7009942,
          "depth": 2.185,
          "azimuth": 278.19
        },
        {
          "lat": 37.60247386,
          "lon": 126.700337,
          "depth": 1.465,
          "azimuth": 277.33
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 45,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60247477,
          "lon": 126.7003269,
          "depth": 2.5,
          "azimuth": 275.61
        },
        {
          "lat": 37.60252645,
          "lon": 126.6996625,
          "depth": 1.49,
          "azimuth": 275.61
        },
        {
          "lat": 37.60252711,
          "lon": 126.6996523,
          "depth": 2.31,
          "azimuth": 274.67
        },
        {
          "lat": 37.60256279,
          "lon": 126.6989879,
          "depth": 1.49,
          "azimuth": 273.88
        },
        {
          "lat": 37.60256309,
          "lon": 126.6989777,
          "depth": 1.6,
          "azimuth": 272.13
        },
        {
          "lat": 37.60257016,
          "lon": 126.6985363,
          "depth": 1.822,
          "azimuth": 271.16
        }
      ],
      "diameter": 500,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 46,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6027624,
          "lon": 126.6949072,
          "depth": 1.49,
          "azimuth": 270.09
        },
        {
          "lat": 37.60276325,
          "lon": 126.6942379,
          "depth": 1.71,
          "azimuth": 270.09
        },
        {
          "lat": 37.60276325,
          "lon": 126.6942277,
          "depth": 1.71,
          "azimuth": 270
        },
        {
          "lat": 37.60276281,
          "lon": 126.6935584,
          "depth": 1.49,
          "azimuth": 269.95
        },
        {
          "lat": 37.6027628,
          "lon": 126.6935482,
          "depth": 1.67,
          "azimuth": 269.93
        },
        {
          "lat": 37.6027625,
          "lon": 126.6931072,
          "depth": 1.5,
          "azimuth": 269.95
        }
      ],
      "diameter": 500,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 47,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60276249,
          "lon": 126.6930936,
          "depth": 2,
          "azimuth": 269.95
        },
        {
          "lat": 37.60276213,
          "lon": 126.6925636,
          "depth": 1.55,
          "azimuth": 269.95
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 48,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60258576,
          "lon": 126.6949073,
          "depth": 1.49,
          "azimuth": 270.09
        },
        {
          "lat": 37.60258661,
          "lon": 126.6942381,
          "depth": 1.89,
          "azimuth": 270.09
        },
        {
          "lat": 37.60258662,
          "lon": 126.6942279,
          "depth": 1.89,
          "azimuth": 270.07
        },
        {
          "lat": 37.60258616,
          "lon": 126.6935603,
          "depth": 1.65,
          "azimuth": 269.95
        }
      ],
      "diameter": 500,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 49,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60258615,
          "lon": 126.6935467,
          "depth": 1.6,
          "azimuth": 269.95
        },
        {
          "lat": 37.60258586,
          "lon": 126.6931073,
          "depth": 1.55,
          "azimuth": 269.95
        },
        {
          "lat": 37.60258584,
          "lon": 126.6930937,
          "depth": 1.62,
          "azimuth": 269.89
        },
        {
          "lat": 37.60258419,
          "lon": 126.692571,
          "depth": 1.55,
          "azimuth": 269.77
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 50,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60348402,
          "lon": 126.6959363,
          "depth": 2.295,
          "azimuth": 188.74
        },
        {
          "lat": 37.60337275,
          "lon": 126.6959147,
          "depth": 1.985,
          "azimuth": 188.74
        },
        {
          "lat": 37.60335048,
          "lon": 126.6959108,
          "depth": 1.928,
          "azimuth": 187.9
        },
        {
          "lat": 37.60316846,
          "lon": 126.6959164,
          "depth": 1.465,
          "azimuth": 178.6
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 51,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60316442,
          "lon": 126.6959217,
          "depth": 2.815,
          "azimuth": 89.78
        },
        {
          "lat": 37.60316642,
          "lon": 126.6965775,
          "depth": 1.465,
          "azimuth": 89.78
        },
        {
          "lat": 37.60316645,
          "lon": 126.6965877,
          "depth": 2.675,
          "azimuth": 89.79
        },
        {
          "lat": 37.60316832,
          "lon": 126.6972004,
          "depth": 1.455,
          "azimuth": 89.78
        },
        {
          "lat": 37.60316834,
          "lon": 126.6972106,
          "depth": 2.135,
          "azimuth": 89.86
        },
        {
          "lat": 37.60317034,
          "lon": 126.6978676,
          "depth": 1.465,
          "azimuth": 89.78
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 52,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60359599,
          "lon": 126.6978416,
          "depth": 2.015,
          "azimuth": 176.5
        },
        {
          "lat": 37.60317575,
          "lon": 126.697874,
          "depth": 1.465,
          "azimuth": 176.5
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 53,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60316495,
          "lon": 126.6978744,
          "depth": 2.46,
          "azimuth": 179.82
        },
        {
          "lat": 37.6027461,
          "lon": 126.6978761,
          "depth": 1.65,
          "azimuth": 179.82
        }
      ],
      "diameter": 600,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 54,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60276415,
          "lon": 126.6955968,
          "depth": 2.405,
          "azimuth": 89.95
        },
        {
          "lat": 37.60276444,
          "lon": 126.6960396,
          "depth": 1.465,
          "azimuth": 89.95
        },
        {
          "lat": 37.60276445,
          "lon": 126.6960498,
          "depth": 2.505,
          "azimuth": 89.93
        },
        {
          "lat": 37.60276473,
          "lon": 126.6964926,
          "depth": 1.465,
          "azimuth": 89.95
        },
        {
          "lat": 37.60276474,
          "lon": 126.6965028,
          "depth": 2.595,
          "azimuth": 89.93
        },
        {
          "lat": 37.60276502,
          "lon": 126.6969456,
          "depth": 1.465,
          "azimuth": 89.95
        },
        {
          "lat": 37.60276475,
          "lon": 126.6969557,
          "depth": 2.505,
          "azimuth": 91.93
        },
        {
          "lat": 37.60274081,
          "lon": 126.6973986,
          "depth": 1.465,
          "azimuth": 93.9
        },
        {
          "lat": 37.60274054,
          "lon": 126.6974087,
          "depth": 2.545,
          "azimuth": 91.93
        },
        {
          "lat": 37.60274071,
          "lon": 126.6978694,
          "depth": 1.455,
          "azimuth": 89.97
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 55,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60274067,
          "lon": 126.697883,
          "depth": 2.51,
          "azimuth": 91
        },
        {
          "lat": 37.60273198,
          "lon": 126.698513,
          "depth": 1.783,
          "azimuth": 91
        }
      ],
      "diameter": 700,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 56,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60258621,
          "lon": 126.695597,
          "depth": 2.405,
          "azimuth": 89.95
        },
        {
          "lat": 37.60258649,
          "lon": 126.6960398,
          "depth": 1.465,
          "azimuth": 89.95
        },
        {
          "lat": 37.6025865,
          "lon": 126.69605,
          "depth": 2.505,
          "azimuth": 89.93
        },
        {
          "lat": 37.60258679,
          "lon": 126.6964928,
          "depth": 1.465,
          "azimuth": 89.95
        },
        {
          "lat": 37.60258679,
          "lon": 126.696503,
          "depth": 2.595,
          "azimuth": 90
        },
        {
          "lat": 37.60258708,
          "lon": 126.6969457,
          "depth": 1.465,
          "azimuth": 89.95
        },
        {
          "lat": 37.60258708,
          "lon": 126.6969559,
          "depth": 2.615,
          "azimuth": 90
        },
        {
          "lat": 37.60258737,
          "lon": 126.6973987,
          "depth": 1.465,
          "azimuth": 89.95
        },
        {
          "lat": 37.60258737,
          "lon": 126.6974089,
          "depth": 2.595,
          "azimuth": 90
        },
        {
          "lat": 37.60258761,
          "lon": 126.6977768,
          "depth": 1.639,
          "azimuth": 89.95
        },
        {
          "lat": 37.6025876,
          "lon": 126.6978051,
          "depth": 1.589,
          "azimuth": 90.03
        },
        {
          "lat": 37.60258758,
          "lon": 126.6978517,
          "depth": 1.465,
          "azimuth": 90.03
        },
        {
          "lat": 37.60258743,
          "lon": 126.6978619,
          "depth": 2.145,
          "azimuth": 91.06
        },
        {
          "lat": 37.60257,
          "lon": 126.6985136,
          "depth": 1.739,
          "azimuth": 91.93
        }
      ],
      "diameter": 450,
      "category": 1,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 57,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60597112,
          "lon": 126.6985655,
          "depth": 1.213,
          "azimuth": 179.81
        },
        {
          "lat": 37.60484481,
          "lon": 126.6985701,
          "depth": 1.213,
          "azimuth": 179.81
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 58,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60597113,
          "lon": 126.6985675,
          "depth": 1.213,
          "azimuth": 179.81
        },
        {
          "lat": 37.60484482,
          "lon": 126.6985721,
          "depth": 1.213,
          "azimuth": 179.81
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 59,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60597113,
          "lon": 126.6985695,
          "depth": 1.213,
          "azimuth": 179.82
        },
        {
          "lat": 37.60484482,
          "lon": 126.698574,
          "depth": 1.213,
          "azimuth": 179.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 60,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60597112,
          "lon": 126.6985655,
          "depth": 1.038,
          "azimuth": 179.81
        },
        {
          "lat": 37.60484481,
          "lon": 126.6985701,
          "depth": 1.038,
          "azimuth": 179.81
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 61,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60597113,
          "lon": 126.6985675,
          "depth": 1.038,
          "azimuth": 179.81
        },
        {
          "lat": 37.60484482,
          "lon": 126.6985721,
          "depth": 1.038,
          "azimuth": 179.81
        }
      ],
      "diameter": 100,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 62,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60480949,
          "lon": 126.6985702,
          "depth": 1.213,
          "azimuth": 179.82
        },
        {
          "lat": 37.60374493,
          "lon": 126.6985745,
          "depth": 1.213,
          "azimuth": 179.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 63,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6048095,
          "lon": 126.6985722,
          "depth": 1.213,
          "azimuth": 179.82
        },
        {
          "lat": 37.60374494,
          "lon": 126.6985765,
          "depth": 1.213,
          "azimuth": 179.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 64,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6048095,
          "lon": 126.6985742,
          "depth": 1.213,
          "azimuth": 179.82
        },
        {
          "lat": 37.60374494,
          "lon": 126.6985785,
          "depth": 1.213,
          "azimuth": 179.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 65,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60480949,
          "lon": 126.6985702,
          "depth": 1.038,
          "azimuth": 179.82
        },
        {
          "lat": 37.60374493,
          "lon": 126.6985745,
          "depth": 1.038,
          "azimuth": 179.82
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 66,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6048095,
          "lon": 126.6985722,
          "depth": 1.038,
          "azimuth": 179.82
        },
        {
          "lat": 37.60374494,
          "lon": 126.6985765,
          "depth": 1.038,
          "azimuth": 179.82
        }
      ],
      "diameter": 100,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 67,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60370962,
          "lon": 126.6985747,
          "depth": 1.213,
          "azimuth": 179.82
        },
        {
          "lat": 37.60301125,
          "lon": 126.6985775,
          "depth": 1.213,
          "azimuth": 179.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 68,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60370962,
          "lon": 126.6985766,
          "depth": 1.213,
          "azimuth": 179.82
        },
        {
          "lat": 37.60301125,
          "lon": 126.6985794,
          "depth": 1.213,
          "azimuth": 179.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 69,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60370963,
          "lon": 126.6985786,
          "depth": 1.213,
          "azimuth": 179.82
        },
        {
          "lat": 37.60301126,
          "lon": 126.6985814,
          "depth": 1.213,
          "azimuth": 179.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 70,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60370962,
          "lon": 126.6985747,
          "depth": 1.038,
          "azimuth": 179.82
        },
        {
          "lat": 37.60301125,
          "lon": 126.6985775,
          "depth": 1.038,
          "azimuth": 179.82
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 71,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60370962,
          "lon": 126.6985766,
          "depth": 1.038,
          "azimuth": 179.82
        },
        {
          "lat": 37.60301125,
          "lon": 126.6985794,
          "depth": 1.038,
          "azimuth": 179.82
        }
      ],
      "diameter": 100,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 72,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297593,
          "lon": 126.6985766,
          "depth": 1.213,
          "azimuth": 179.8
        },
        {
          "lat": 37.60284098,
          "lon": 126.6985772,
          "depth": 1.213,
          "azimuth": 179.8
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 73,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297593,
          "lon": 126.6985786,
          "depth": 1.213,
          "azimuth": 179.83
        },
        {
          "lat": 37.60284099,
          "lon": 126.6985791,
          "depth": 1.213,
          "azimuth": 179.83
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 74,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297594,
          "lon": 126.6985806,
          "depth": 1.213,
          "azimuth": 179.83
        },
        {
          "lat": 37.60284099,
          "lon": 126.6985811,
          "depth": 1.213,
          "azimuth": 179.83
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 75,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297594,
          "lon": 126.6985826,
          "depth": 1.213,
          "azimuth": 179.83
        },
        {
          "lat": 37.602841,
          "lon": 126.6985831,
          "depth": 1.213,
          "azimuth": 179.83
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 76,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297593,
          "lon": 126.6985766,
          "depth": 1.038,
          "azimuth": 179.8
        },
        {
          "lat": 37.60284098,
          "lon": 126.6985772,
          "depth": 1.038,
          "azimuth": 179.8
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 77,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297593,
          "lon": 126.6985786,
          "depth": 1.038,
          "azimuth": 179.83
        },
        {
          "lat": 37.60284099,
          "lon": 126.6985791,
          "depth": 1.038,
          "azimuth": 179.83
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 78,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297594,
          "lon": 126.6985806,
          "depth": 1.038,
          "azimuth": 179.83
        },
        {
          "lat": 37.60284099,
          "lon": 126.6985811,
          "depth": 1.038,
          "azimuth": 179.83
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 79,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297594,
          "lon": 126.6985826,
          "depth": 1.038,
          "azimuth": 179.83
        },
        {
          "lat": 37.602841,
          "lon": 126.6985831,
          "depth": 1.038,
          "azimuth": 179.83
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 80,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297593,
          "lon": 126.6985766,
          "depth": 0.863,
          "azimuth": 179.8
        },
        {
          "lat": 37.60284098,
          "lon": 126.6985772,
          "depth": 0.863,
          "azimuth": 179.8
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 81,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297593,
          "lon": 126.6985786,
          "depth": 0.863,
          "azimuth": 179.83
        },
        {
          "lat": 37.60284099,
          "lon": 126.6985791,
          "depth": 0.863,
          "azimuth": 179.83
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 82,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297594,
          "lon": 126.6985806,
          "depth": 0.863,
          "azimuth": 179.83
        },
        {
          "lat": 37.60284099,
          "lon": 126.6985811,
          "depth": 0.863,
          "azimuth": 179.83
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 83,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297594,
          "lon": 126.6985826,
          "depth": 0.863,
          "azimuth": 179.83
        },
        {
          "lat": 37.602841,
          "lon": 126.6985831,
          "depth": 0.863,
          "azimuth": 179.83
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 84,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297593,
          "lon": 126.6985766,
          "depth": 0.688,
          "azimuth": 179.8
        },
        {
          "lat": 37.60284098,
          "lon": 126.6985772,
          "depth": 0.688,
          "azimuth": 179.8
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 85,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297593,
          "lon": 126.6985786,
          "depth": 0.688,
          "azimuth": 179.83
        },
        {
          "lat": 37.60284099,
          "lon": 126.6985791,
          "depth": 0.688,
          "azimuth": 179.83
        }
      ],
      "diameter": 100,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 86,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297594,
          "lon": 126.6985806,
          "depth": 0.688,
          "azimuth": 179.83
        },
        {
          "lat": 37.60284099,
          "lon": 126.6985811,
          "depth": 0.688,
          "azimuth": 179.83
        }
      ],
      "diameter": 100,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 87,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261464,
          "lon": 126.6970912,
          "depth": 1.213,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261469,
          "lon": 126.6971695,
          "depth": 1.213,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261484,
          "lon": 126.697396,
          "depth": 1.213,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261498,
          "lon": 126.6976224,
          "depth": 1.213,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261505,
          "lon": 126.697849,
          "depth": 1.213,
          "azimuth": 89.98
        },
        {
          "lat": 37.60261378,
          "lon": 126.6980755,
          "depth": 1.213,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261069,
          "lon": 126.698302,
          "depth": 1.213,
          "azimuth": 90.99
        },
        {
          "lat": 37.60260543,
          "lon": 126.6985426,
          "depth": 1.213,
          "azimuth": 91.58
        },
        {
          "lat": 37.60259909,
          "lon": 126.6987549,
          "depth": 1.213,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259057,
          "lon": 126.6989812,
          "depth": 1.213,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258026,
          "lon": 126.6992074,
          "depth": 1.213,
          "azimuth": 93.29
        },
        {
          "lat": 37.60256813,
          "lon": 126.6994335,
          "depth": 1.213,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255421,
          "lon": 126.6996594,
          "depth": 1.213,
          "azimuth": 94.45
        },
        {
          "lat": 37.60253847,
          "lon": 126.6998851,
          "depth": 1.213,
          "azimuth": 95.03
        },
        {
          "lat": 37.60252688,
          "lon": 126.7000367,
          "depth": 1.213,
          "azimuth": 95.51
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 88,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261622,
          "lon": 126.6970912,
          "depth": 1.213,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261627,
          "lon": 126.6971695,
          "depth": 1.213,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261641,
          "lon": 126.6973959,
          "depth": 1.213,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261655,
          "lon": 126.6976224,
          "depth": 1.213,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261663,
          "lon": 126.697849,
          "depth": 1.213,
          "azimuth": 89.97
        },
        {
          "lat": 37.60261535,
          "lon": 126.6980755,
          "depth": 1.213,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261226,
          "lon": 126.6983021,
          "depth": 1.213,
          "azimuth": 90.99
        },
        {
          "lat": 37.602607,
          "lon": 126.6985426,
          "depth": 1.213,
          "azimuth": 91.58
        },
        {
          "lat": 37.60260066,
          "lon": 126.698755,
          "depth": 1.213,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259215,
          "lon": 126.6989813,
          "depth": 1.213,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258183,
          "lon": 126.6992076,
          "depth": 1.213,
          "azimuth": 93.29
        },
        {
          "lat": 37.60256971,
          "lon": 126.6994336,
          "depth": 1.213,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255577,
          "lon": 126.6996595,
          "depth": 1.213,
          "azimuth": 94.45
        },
        {
          "lat": 37.60254004,
          "lon": 126.6998853,
          "depth": 1.213,
          "azimuth": 95.03
        },
        {
          "lat": 37.60252845,
          "lon": 126.7000369,
          "depth": 1.213,
          "azimuth": 95.51
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 89,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261779,
          "lon": 126.6970912,
          "depth": 1.213,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261784,
          "lon": 126.6971694,
          "depth": 1.213,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261799,
          "lon": 126.6973959,
          "depth": 1.213,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261813,
          "lon": 126.6976224,
          "depth": 1.213,
          "azimuth": 89.96
        },
        {
          "lat": 37.6026182,
          "lon": 126.697849,
          "depth": 1.213,
          "azimuth": 89.98
        },
        {
          "lat": 37.60261693,
          "lon": 126.6980755,
          "depth": 1.213,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261384,
          "lon": 126.6983021,
          "depth": 1.213,
          "azimuth": 90.99
        },
        {
          "lat": 37.60260858,
          "lon": 126.6985427,
          "depth": 1.213,
          "azimuth": 91.58
        },
        {
          "lat": 37.60260224,
          "lon": 126.6987551,
          "depth": 1.213,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259373,
          "lon": 126.6989814,
          "depth": 1.213,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258341,
          "lon": 126.6992077,
          "depth": 1.213,
          "azimuth": 93.29
        },
        {
          "lat": 37.60257128,
          "lon": 126.6994338,
          "depth": 1.213,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255734,
          "lon": 126.6996597,
          "depth": 1.213,
          "azimuth": 94.45
        },
        {
          "lat": 37.60254161,
          "lon": 126.6998855,
          "depth": 1.213,
          "azimuth": 95.03
        },
        {
          "lat": 37.60253002,
          "lon": 126.700037,
          "depth": 1.213,
          "azimuth": 95.52
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 90,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261464,
          "lon": 126.6970912,
          "depth": 1.038,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261469,
          "lon": 126.6971695,
          "depth": 1.038,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261484,
          "lon": 126.697396,
          "depth": 1.038,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261498,
          "lon": 126.6976224,
          "depth": 1.038,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261505,
          "lon": 126.697849,
          "depth": 1.038,
          "azimuth": 89.98
        },
        {
          "lat": 37.60261378,
          "lon": 126.6980755,
          "depth": 1.038,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261069,
          "lon": 126.698302,
          "depth": 1.038,
          "azimuth": 90.99
        },
        {
          "lat": 37.60260543,
          "lon": 126.6985426,
          "depth": 1.038,
          "azimuth": 91.58
        },
        {
          "lat": 37.60259909,
          "lon": 126.6987549,
          "depth": 1.038,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259057,
          "lon": 126.6989812,
          "depth": 1.038,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258026,
          "lon": 126.6992074,
          "depth": 1.038,
          "azimuth": 93.29
        },
        {
          "lat": 37.60256813,
          "lon": 126.6994335,
          "depth": 1.038,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255421,
          "lon": 126.6996594,
          "depth": 1.038,
          "azimuth": 94.45
        },
        {
          "lat": 37.60253847,
          "lon": 126.6998851,
          "depth": 1.038,
          "azimuth": 95.03
        },
        {
          "lat": 37.60252688,
          "lon": 126.7000367,
          "depth": 1.038,
          "azimuth": 95.51
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 91,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261622,
          "lon": 126.6970912,
          "depth": 1.038,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261627,
          "lon": 126.6971695,
          "depth": 1.038,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261641,
          "lon": 126.6973959,
          "depth": 1.038,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261655,
          "lon": 126.6976224,
          "depth": 1.038,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261663,
          "lon": 126.697849,
          "depth": 1.038,
          "azimuth": 89.97
        },
        {
          "lat": 37.60261535,
          "lon": 126.6980755,
          "depth": 1.038,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261226,
          "lon": 126.6983021,
          "depth": 1.038,
          "azimuth": 90.99
        },
        {
          "lat": 37.602607,
          "lon": 126.6985426,
          "depth": 1.038,
          "azimuth": 91.58
        },
        {
          "lat": 37.60260066,
          "lon": 126.698755,
          "depth": 1.038,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259215,
          "lon": 126.6989813,
          "depth": 1.038,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258183,
          "lon": 126.6992076,
          "depth": 1.038,
          "azimuth": 93.29
        },
        {
          "lat": 37.60256971,
          "lon": 126.6994336,
          "depth": 1.038,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255577,
          "lon": 126.6996595,
          "depth": 1.038,
          "azimuth": 94.45
        },
        {
          "lat": 37.60254004,
          "lon": 126.6998853,
          "depth": 1.038,
          "azimuth": 95.03
        },
        {
          "lat": 37.60252845,
          "lon": 126.7000369,
          "depth": 1.038,
          "azimuth": 95.51
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 92,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261779,
          "lon": 126.6970912,
          "depth": 1.038,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261784,
          "lon": 126.6971694,
          "depth": 1.038,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261799,
          "lon": 126.6973959,
          "depth": 1.038,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261813,
          "lon": 126.6976224,
          "depth": 1.038,
          "azimuth": 89.96
        },
        {
          "lat": 37.6026182,
          "lon": 126.697849,
          "depth": 1.038,
          "azimuth": 89.98
        },
        {
          "lat": 37.60261693,
          "lon": 126.6980755,
          "depth": 1.038,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261384,
          "lon": 126.6983021,
          "depth": 1.038,
          "azimuth": 90.99
        },
        {
          "lat": 37.60260858,
          "lon": 126.6985427,
          "depth": 1.038,
          "azimuth": 91.58
        },
        {
          "lat": 37.60260224,
          "lon": 126.6987551,
          "depth": 1.038,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259373,
          "lon": 126.6989814,
          "depth": 1.038,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258341,
          "lon": 126.6992077,
          "depth": 1.038,
          "azimuth": 93.29
        },
        {
          "lat": 37.60257128,
          "lon": 126.6994338,
          "depth": 1.038,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255734,
          "lon": 126.6996597,
          "depth": 1.038,
          "azimuth": 94.45
        },
        {
          "lat": 37.60254161,
          "lon": 126.6998855,
          "depth": 1.038,
          "azimuth": 95.03
        },
        {
          "lat": 37.60253002,
          "lon": 126.700037,
          "depth": 1.038,
          "azimuth": 95.52
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 93,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261464,
          "lon": 126.6970912,
          "depth": 0.863,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261469,
          "lon": 126.6971695,
          "depth": 0.863,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261484,
          "lon": 126.697396,
          "depth": 0.863,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261498,
          "lon": 126.6976224,
          "depth": 0.863,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261505,
          "lon": 126.697849,
          "depth": 0.863,
          "azimuth": 89.98
        },
        {
          "lat": 37.60261378,
          "lon": 126.6980755,
          "depth": 0.863,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261069,
          "lon": 126.698302,
          "depth": 0.863,
          "azimuth": 90.99
        },
        {
          "lat": 37.60260543,
          "lon": 126.6985426,
          "depth": 0.863,
          "azimuth": 91.58
        },
        {
          "lat": 37.60259909,
          "lon": 126.6987549,
          "depth": 0.863,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259057,
          "lon": 126.6989812,
          "depth": 0.863,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258026,
          "lon": 126.6992074,
          "depth": 0.863,
          "azimuth": 93.29
        },
        {
          "lat": 37.60256813,
          "lon": 126.6994335,
          "depth": 0.863,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255421,
          "lon": 126.6996594,
          "depth": 0.863,
          "azimuth": 94.45
        },
        {
          "lat": 37.60253847,
          "lon": 126.6998851,
          "depth": 0.863,
          "azimuth": 95.03
        },
        {
          "lat": 37.60252688,
          "lon": 126.7000367,
          "depth": 0.863,
          "azimuth": 95.51
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 94,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261622,
          "lon": 126.6970912,
          "depth": 0.863,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261627,
          "lon": 126.6971695,
          "depth": 0.863,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261641,
          "lon": 126.6973959,
          "depth": 0.863,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261655,
          "lon": 126.6976224,
          "depth": 0.863,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261663,
          "lon": 126.697849,
          "depth": 0.863,
          "azimuth": 89.97
        },
        {
          "lat": 37.60261535,
          "lon": 126.6980755,
          "depth": 0.863,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261226,
          "lon": 126.6983021,
          "depth": 0.863,
          "azimuth": 90.99
        },
        {
          "lat": 37.602607,
          "lon": 126.6985426,
          "depth": 0.863,
          "azimuth": 91.58
        },
        {
          "lat": 37.60260066,
          "lon": 126.698755,
          "depth": 0.863,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259215,
          "lon": 126.6989813,
          "depth": 0.863,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258183,
          "lon": 126.6992076,
          "depth": 0.863,
          "azimuth": 93.29
        },
        {
          "lat": 37.60256971,
          "lon": 126.6994336,
          "depth": 0.863,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255577,
          "lon": 126.6996595,
          "depth": 0.863,
          "azimuth": 94.45
        },
        {
          "lat": 37.60254004,
          "lon": 126.6998853,
          "depth": 0.863,
          "azimuth": 95.03
        },
        {
          "lat": 37.60252845,
          "lon": 126.7000369,
          "depth": 0.863,
          "azimuth": 95.51
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 95,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261779,
          "lon": 126.6970912,
          "depth": 0.863,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261784,
          "lon": 126.6971694,
          "depth": 0.863,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261799,
          "lon": 126.6973959,
          "depth": 0.863,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261813,
          "lon": 126.6976224,
          "depth": 0.863,
          "azimuth": 89.96
        },
        {
          "lat": 37.6026182,
          "lon": 126.697849,
          "depth": 0.863,
          "azimuth": 89.98
        },
        {
          "lat": 37.60261693,
          "lon": 126.6980755,
          "depth": 0.863,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261384,
          "lon": 126.6983021,
          "depth": 0.863,
          "azimuth": 90.99
        },
        {
          "lat": 37.60260858,
          "lon": 126.6985427,
          "depth": 0.863,
          "azimuth": 91.58
        },
        {
          "lat": 37.60260224,
          "lon": 126.6987551,
          "depth": 0.863,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259373,
          "lon": 126.6989814,
          "depth": 0.863,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258341,
          "lon": 126.6992077,
          "depth": 0.863,
          "azimuth": 93.29
        },
        {
          "lat": 37.60257128,
          "lon": 126.6994338,
          "depth": 0.863,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255734,
          "lon": 126.6996597,
          "depth": 0.863,
          "azimuth": 94.45
        },
        {
          "lat": 37.60254161,
          "lon": 126.6998855,
          "depth": 0.863,
          "azimuth": 95.03
        },
        {
          "lat": 37.60253002,
          "lon": 126.700037,
          "depth": 0.863,
          "azimuth": 95.52
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 96,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60261464,
          "lon": 126.6970912,
          "depth": 0.688,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261469,
          "lon": 126.6971695,
          "depth": 0.688,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261484,
          "lon": 126.697396,
          "depth": 0.688,
          "azimuth": 89.95
        },
        {
          "lat": 37.60261498,
          "lon": 126.6976224,
          "depth": 0.688,
          "azimuth": 89.96
        },
        {
          "lat": 37.60261505,
          "lon": 126.697849,
          "depth": 0.688,
          "azimuth": 89.98
        },
        {
          "lat": 37.60261378,
          "lon": 126.6980755,
          "depth": 0.688,
          "azimuth": 90.41
        },
        {
          "lat": 37.60261069,
          "lon": 126.698302,
          "depth": 0.688,
          "azimuth": 90.99
        },
        {
          "lat": 37.60260543,
          "lon": 126.6985426,
          "depth": 0.688,
          "azimuth": 91.58
        },
        {
          "lat": 37.60259909,
          "lon": 126.6987549,
          "depth": 0.688,
          "azimuth": 92.16
        },
        {
          "lat": 37.60259057,
          "lon": 126.6989812,
          "depth": 0.688,
          "azimuth": 92.72
        },
        {
          "lat": 37.60258026,
          "lon": 126.6992074,
          "depth": 0.688,
          "azimuth": 93.29
        },
        {
          "lat": 37.60256813,
          "lon": 126.6994335,
          "depth": 0.688,
          "azimuth": 93.87
        },
        {
          "lat": 37.60255421,
          "lon": 126.6996594,
          "depth": 0.688,
          "azimuth": 94.45
        },
        {
          "lat": 37.60253847,
          "lon": 126.6998851,
          "depth": 0.688,
          "azimuth": 95.03
        },
        {
          "lat": 37.60252688,
          "lon": 126.7000367,
          "depth": 0.688,
          "azimuth": 95.51
        }
      ],
      "diameter": 100,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 97,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60483609,
          "lon": 126.698561,
          "depth": 1.213,
          "azimuth": 269.82
        },
        {
          "lat": 37.60483516,
          "lon": 126.698195,
          "depth": 1.213,
          "azimuth": 269.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 98,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60483767,
          "lon": 126.698561,
          "depth": 1.213,
          "azimuth": 269.81
        },
        {
          "lat": 37.60483673,
          "lon": 126.698195,
          "depth": 1.213,
          "azimuth": 269.81
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 99,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60483925,
          "lon": 126.698561,
          "depth": 1.213,
          "azimuth": 269.81
        },
        {
          "lat": 37.60483831,
          "lon": 126.698195,
          "depth": 1.213,
          "azimuth": 269.81
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 100,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60484082,
          "lon": 126.698561,
          "depth": 1.213,
          "azimuth": 269.82
        },
        {
          "lat": 37.60483989,
          "lon": 126.698195,
          "depth": 1.213,
          "azimuth": 269.82
        }
      ],
      "diameter": 50,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 101,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60483682,
          "lon": 126.698847,
          "depth": 1.213,
          "azimuth": 269.82
        },
        {
          "lat": 37.60483615,
          "lon": 126.6985832,
          "depth": 1.213,
          "azimuth": 269.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 102,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6048384,
          "lon": 126.6988469,
          "depth": 1.213,
          "azimuth": 269.82
        },
        {
          "lat": 37.60483773,
          "lon": 126.6985832,
          "depth": 1.213,
          "azimuth": 269.82
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 103,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60483998,
          "lon": 126.6988469,
          "depth": 1.213,
          "azimuth": 269.81
        },
        {
          "lat": 37.6048393,
          "lon": 126.6985832,
          "depth": 1.213,
          "azimuth": 269.81
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 104,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60484155,
          "lon": 126.6988469,
          "depth": 1.213,
          "azimuth": 269.82
        },
        {
          "lat": 37.60484088,
          "lon": 126.6985832,
          "depth": 1.213,
          "azimuth": 269.82
        }
      ],
      "diameter": 50,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 105,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371806,
          "lon": 126.6985655,
          "depth": 1.213,
          "azimuth": 269.82
        },
        {
          "lat": 37.60371728,
          "lon": 126.6982581,
          "depth": 1.213,
          "azimuth": 269.82
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 106,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371648,
          "lon": 126.6985655,
          "depth": 1.213,
          "azimuth": 269.82
        },
        {
          "lat": 37.6037157,
          "lon": 126.6982581,
          "depth": 1.213,
          "azimuth": 269.82
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 107,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371491,
          "lon": 126.6985655,
          "depth": 1.213,
          "azimuth": 269.81
        },
        {
          "lat": 37.60371412,
          "lon": 126.6982581,
          "depth": 1.213,
          "azimuth": 269.81
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 108,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371806,
          "lon": 126.6985655,
          "depth": 1.038,
          "azimuth": 269.82
        },
        {
          "lat": 37.60371728,
          "lon": 126.6982581,
          "depth": 1.038,
          "azimuth": 269.82
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 109,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371648,
          "lon": 126.6985655,
          "depth": 1.038,
          "azimuth": 269.82
        },
        {
          "lat": 37.6037157,
          "lon": 126.6982581,
          "depth": 1.038,
          "azimuth": 269.82
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 110,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371491,
          "lon": 126.6985655,
          "depth": 1.038,
          "azimuth": 269.81
        },
        {
          "lat": 37.60371412,
          "lon": 126.6982581,
          "depth": 1.038,
          "azimuth": 269.81
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 111,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371806,
          "lon": 126.6985655,
          "depth": 0.863,
          "azimuth": 269.82
        },
        {
          "lat": 37.60371728,
          "lon": 126.6982581,
          "depth": 0.863,
          "azimuth": 269.82
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 112,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371749,
          "lon": 126.6985877,
          "depth": 1.213,
          "azimuth": 89.78
        },
        {
          "lat": 37.60371973,
          "lon": 126.6993276,
          "depth": 1.213,
          "azimuth": 89.78
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 113,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371591,
          "lon": 126.6985877,
          "depth": 1.213,
          "azimuth": 89.78
        },
        {
          "lat": 37.60371815,
          "lon": 126.6993276,
          "depth": 1.213,
          "azimuth": 89.78
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 114,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371749,
          "lon": 126.6985877,
          "depth": 1.038,
          "azimuth": 89.78
        },
        {
          "lat": 37.60371973,
          "lon": 126.6993276,
          "depth": 1.038,
          "azimuth": 89.78
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 115,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371591,
          "lon": 126.6985877,
          "depth": 1.038,
          "azimuth": 89.78
        },
        {
          "lat": 37.60371815,
          "lon": 126.6993276,
          "depth": 1.038,
          "azimuth": 89.78
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 116,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60374493,
          "lon": 126.6985745,
          "depth": 0.863,
          "azimuth": 15.94
        },
        {
          "lat": 37.60377655,
          "lon": 126.6985859,
          "depth": 0.863,
          "azimuth": 15.94
        },
        {
          "lat": 37.60380521,
          "lon": 126.6986055,
          "depth": 0.863,
          "azimuth": 28.45
        },
        {
          "lat": 37.60382986,
          "lon": 126.6986324,
          "depth": 0.863,
          "azimuth": 40.85
        },
        {
          "lat": 37.60384917,
          "lon": 126.6986649,
          "depth": 0.863,
          "azimuth": 53.13
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 117,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60374494,
          "lon": 126.6985765,
          "depth": 0.863,
          "azimuth": 15.97
        },
        {
          "lat": 37.60377594,
          "lon": 126.6985877,
          "depth": 0.863,
          "azimuth": 15.97
        },
        {
          "lat": 37.6038043,
          "lon": 126.6986072,
          "depth": 0.863,
          "azimuth": 28.58
        },
        {
          "lat": 37.60382871,
          "lon": 126.6986338,
          "depth": 0.863,
          "azimuth": 40.8
        },
        {
          "lat": 37.60384802,
          "lon": 126.6986663,
          "depth": 0.863,
          "azimuth": 53.13
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 118,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60374494,
          "lon": 126.6985785,
          "depth": 0.863,
          "azimuth": 16.13
        },
        {
          "lat": 37.60377534,
          "lon": 126.6985896,
          "depth": 0.863,
          "azimuth": 16.13
        },
        {
          "lat": 37.60380341,
          "lon": 126.6986088,
          "depth": 0.863,
          "azimuth": 28.45
        },
        {
          "lat": 37.60382755,
          "lon": 126.6986351,
          "depth": 0.863,
          "azimuth": 40.8
        },
        {
          "lat": 37.60384687,
          "lon": 126.6986678,
          "depth": 0.863,
          "azimuth": 53.29
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 119,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60374493,
          "lon": 126.6985745,
          "depth": 0.688,
          "azimuth": 15.94
        },
        {
          "lat": 37.60377655,
          "lon": 126.6985859,
          "depth": 0.688,
          "azimuth": 15.94
        },
        {
          "lat": 37.60380521,
          "lon": 126.6986055,
          "depth": 0.688,
          "azimuth": 28.45
        },
        {
          "lat": 37.60382986,
          "lon": 126.6986324,
          "depth": 0.688,
          "azimuth": 40.85
        },
        {
          "lat": 37.60384917,
          "lon": 126.6986649,
          "depth": 0.688,
          "azimuth": 53.13
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 120,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60374494,
          "lon": 126.6985765,
          "depth": 0.688,
          "azimuth": 15.97
        },
        {
          "lat": 37.60377594,
          "lon": 126.6985877,
          "depth": 0.688,
          "azimuth": 15.97
        },
        {
          "lat": 37.6038043,
          "lon": 126.6986072,
          "depth": 0.688,
          "azimuth": 28.58
        },
        {
          "lat": 37.60382871,
          "lon": 126.6986338,
          "depth": 0.688,
          "azimuth": 40.8
        },
        {
          "lat": 37.60384802,
          "lon": 126.6986663,
          "depth": 0.688,
          "azimuth": 53.13
        }
      ],
      "diameter": 100,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 121,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371468,
          "lon": 126.6985877,
          "depth": 1.213,
          "azimuth": 113.5
        },
        {
          "lat": 37.60370228,
          "lon": 126.6986237,
          "depth": 1.213,
          "azimuth": 113.5
        },
        {
          "lat": 37.60368295,
          "lon": 126.6986554,
          "depth": 1.213,
          "azimuth": 127.58
        },
        {
          "lat": 37.6036586,
          "lon": 126.6986811,
          "depth": 1.213,
          "azimuth": 140.1
        },
        {
          "lat": 37.6036304,
          "lon": 126.6986995,
          "depth": 1.213,
          "azimuth": 152.66
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 122,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371305,
          "lon": 126.6985877,
          "depth": 1.213,
          "azimuth": 113.65
        },
        {
          "lat": 37.60370094,
          "lon": 126.6986226,
          "depth": 1.213,
          "azimuth": 113.65
        },
        {
          "lat": 37.60368182,
          "lon": 126.698654,
          "depth": 1.213,
          "azimuth": 127.55
        },
        {
          "lat": 37.60365772,
          "lon": 126.6986794,
          "depth": 1.213,
          "azimuth": 140.14
        },
        {
          "lat": 37.60362983,
          "lon": 126.6986976,
          "depth": 1.213,
          "azimuth": 152.66
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 123,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371142,
          "lon": 126.6985877,
          "depth": 1.213,
          "azimuth": 113.74
        },
        {
          "lat": 37.60369961,
          "lon": 126.6986216,
          "depth": 1.213,
          "azimuth": 113.74
        },
        {
          "lat": 37.60368068,
          "lon": 126.6986526,
          "depth": 1.213,
          "azimuth": 127.62
        },
        {
          "lat": 37.60365686,
          "lon": 126.6986778,
          "depth": 1.213,
          "azimuth": 140.03
        },
        {
          "lat": 37.60362927,
          "lon": 126.6986958,
          "depth": 1.213,
          "azimuth": 152.67
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 124,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60298096,
          "lon": 126.6985685,
          "depth": 1.213,
          "azimuth": 273.83
        },
        {
          "lat": 37.60298854,
          "lon": 126.6984256,
          "depth": 1.213,
          "azimuth": 273.83
        },
        {
          "lat": 37.60302021,
          "lon": 126.6982884,
          "depth": 1.213,
          "azimuth": 286.24
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 125,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60298254,
          "lon": 126.6985685,
          "depth": 1.213,
          "azimuth": 273.83
        },
        {
          "lat": 37.60299009,
          "lon": 126.698426,
          "depth": 1.213,
          "azimuth": 273.83
        },
        {
          "lat": 37.60302168,
          "lon": 126.6982892,
          "depth": 1.213,
          "azimuth": 286.25
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 126,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60298412,
          "lon": 126.6985684,
          "depth": 1.213,
          "azimuth": 273.83
        },
        {
          "lat": 37.60299165,
          "lon": 126.6984263,
          "depth": 1.213,
          "azimuth": 273.83
        },
        {
          "lat": 37.60302314,
          "lon": 126.6982899,
          "depth": 1.213,
          "azimuth": 286.25
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 127,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60301172,
          "lon": 126.6985775,
          "depth": 1.213,
          "azimuth": 25.83
        },
        {
          "lat": 37.60304494,
          "lon": 126.6985978,
          "depth": 1.213,
          "azimuth": 25.83
        },
        {
          "lat": 37.60307207,
          "lon": 126.6986295,
          "depth": 1.213,
          "azimuth": 42.79
        },
        {
          "lat": 37.60309085,
          "lon": 126.6986695,
          "depth": 1.213,
          "azimuth": 59.35
        },
        {
          "lat": 37.60309971,
          "lon": 126.6987147,
          "depth": 1.213,
          "azimuth": 76.1
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 128,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60301125,
          "lon": 126.6985794,
          "depth": 1.213,
          "azimuth": 25.9
        },
        {
          "lat": 37.60304405,
          "lon": 126.6985995,
          "depth": 1.213,
          "azimuth": 25.9
        },
        {
          "lat": 37.60307084,
          "lon": 126.6986307,
          "depth": 1.213,
          "azimuth": 42.7
        },
        {
          "lat": 37.60308939,
          "lon": 126.6986703,
          "depth": 1.213,
          "azimuth": 59.41
        },
        {
          "lat": 37.60309813,
          "lon": 126.6987149,
          "depth": 1.213,
          "azimuth": 76.11
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 129,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60301079,
          "lon": 126.6985813,
          "depth": 1.213,
          "azimuth": 25.86
        },
        {
          "lat": 37.60304315,
          "lon": 126.6986011,
          "depth": 1.213,
          "azimuth": 25.86
        },
        {
          "lat": 37.60306961,
          "lon": 126.6986319,
          "depth": 1.213,
          "azimuth": 42.68
        },
        {
          "lat": 37.60308793,
          "lon": 126.698671,
          "depth": 1.213,
          "azimuth": 59.4
        },
        {
          "lat": 37.60309656,
          "lon": 126.698715,
          "depth": 1.213,
          "azimuth": 76.1
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 130,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297986,
          "lon": 126.6985903,
          "depth": 1.213,
          "azimuth": 109.5
        },
        {
          "lat": 37.60296019,
          "lon": 126.6986604,
          "depth": 1.213,
          "azimuth": 109.5
        },
        {
          "lat": 37.60292545,
          "lon": 126.698721,
          "depth": 1.213,
          "azimuth": 125.89
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 131,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60298142,
          "lon": 126.6985907,
          "depth": 1.213,
          "azimuth": 109.53
        },
        {
          "lat": 37.60296158,
          "lon": 126.6986613,
          "depth": 1.213,
          "azimuth": 109.53
        },
        {
          "lat": 37.60292659,
          "lon": 126.6987223,
          "depth": 1.213,
          "azimuth": 125.91
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 132,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60298296,
          "lon": 126.6985911,
          "depth": 1.213,
          "azimuth": 109.53
        },
        {
          "lat": 37.60296298,
          "lon": 126.6986622,
          "depth": 1.213,
          "azimuth": 109.53
        },
        {
          "lat": 37.60292772,
          "lon": 126.6987237,
          "depth": 1.213,
          "azimuth": 125.89
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 133,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60297986,
          "lon": 126.6985903,
          "depth": 1.038,
          "azimuth": 109.5
        },
        {
          "lat": 37.60296019,
          "lon": 126.6986604,
          "depth": 1.038,
          "azimuth": 109.5
        },
        {
          "lat": 37.60292545,
          "lon": 126.698721,
          "depth": 1.038,
          "azimuth": 125.89
        }
      ],
      "diameter": 175,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 134,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60298142,
          "lon": 126.6985907,
          "depth": 1.038,
          "azimuth": 109.53
        },
        {
          "lat": 37.60296158,
          "lon": 126.6986613,
          "depth": 1.038,
          "azimuth": 109.53
        },
        {
          "lat": 37.60292659,
          "lon": 126.6987223,
          "depth": 1.038,
          "azimuth": 125.91
        }
      ],
      "diameter": 150,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 135,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60298296,
          "lon": 126.6985911,
          "depth": 1.038,
          "azimuth": 109.53
        },
        {
          "lat": 37.60296298,
          "lon": 126.6986622,
          "depth": 1.038,
          "azimuth": 109.53
        },
        {
          "lat": 37.60292772,
          "lon": 126.6987237,
          "depth": 1.038,
          "azimuth": 125.89
        }
      ],
      "diameter": 100,
      "category": 8,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 146,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60724853,
          "lon": 126.6984409,
          "depth": 1.1,
          "azimuth": 179.81
        },
        {
          "lat": 37.60634755,
          "lon": 126.6984446,
          "depth": 1.1,
          "azimuth": 179.81
        },
        {
          "lat": 37.6061197,
          "lon": 126.6984455,
          "depth": 1.1,
          "azimuth": 179.82
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 147,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6061197,
          "lon": 126.6984455,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.60611969,
          "lon": 126.6984455,
          "depth": 2.1,
          "azimuth": 0
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 148,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6061197,
          "lon": 126.6984455,
          "depth": 2.1,
          "azimuth": 179.75
        },
        {
          "lat": 37.60610168,
          "lon": 126.6984456,
          "depth": 2.1,
          "azimuth": 179.75
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 149,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60610168,
          "lon": 126.6984456,
          "depth": 2.1,
          "azimuth": 0
        },
        {
          "lat": 37.60610167,
          "lon": 126.6984456,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 150,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60610168,
          "lon": 126.6984456,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60600321,
          "lon": 126.698446,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60598972,
          "lon": 126.698446,
          "depth": 1.1,
          "azimuth": 180
        },
        {
          "lat": 37.60589706,
          "lon": 126.6984464,
          "depth": 1.1,
          "azimuth": 179.8
        },
        {
          "lat": 37.60544658,
          "lon": 126.6984482,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60499609,
          "lon": 126.69845,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.6045456,
          "lon": 126.6984519,
          "depth": 1.1,
          "azimuth": 179.81
        },
        {
          "lat": 37.60409511,
          "lon": 126.6984537,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60376904,
          "lon": 126.698455,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60371953,
          "lon": 126.6984552,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60364462,
          "lon": 126.6984555,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60328818,
          "lon": 126.6984569,
          "depth": 1.1,
          "azimuth": 179.82
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 151,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60328818,
          "lon": 126.6984569,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.60328817,
          "lon": 126.6984569,
          "depth": 1.6,
          "azimuth": 0
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 152,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60328818,
          "lon": 126.6984569,
          "depth": 1.6,
          "azimuth": 179.75
        },
        {
          "lat": 37.60327016,
          "lon": 126.698457,
          "depth": 1.6,
          "azimuth": 179.75
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 153,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60327016,
          "lon": 126.698457,
          "depth": 1.6,
          "azimuth": 0
        },
        {
          "lat": 37.60327015,
          "lon": 126.698457,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 154,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60327016,
          "lon": 126.698457,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60319413,
          "lon": 126.6984573,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60303196,
          "lon": 126.698458,
          "depth": 1.1,
          "azimuth": 179.8
        },
        {
          "lat": 37.60301391,
          "lon": 126.698458,
          "depth": 1.1,
          "azimuth": 180
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 155,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60600321,
          "lon": 126.698446,
          "depth": 1.1,
          "azimuth": 269.82
        },
        {
          "lat": 37.60600295,
          "lon": 126.698344,
          "depth": 1.1,
          "azimuth": 269.82
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 156,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60598969,
          "lon": 126.698446,
          "depth": 1.1,
          "azimuth": 89.81
        },
        {
          "lat": 37.60598986,
          "lon": 126.6985111,
          "depth": 1.1,
          "azimuth": 89.81
        },
        {
          "lat": 37.6059902,
          "lon": 126.6986442,
          "depth": 1.1,
          "azimuth": 89.82
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 157,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60376904,
          "lon": 126.698455,
          "depth": 1.1,
          "azimuth": 270.21
        },
        {
          "lat": 37.60376924,
          "lon": 126.698387,
          "depth": 1.1,
          "azimuth": 270.21
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 158,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371953,
          "lon": 126.6984552,
          "depth": 1.1,
          "azimuth": 89.82
        },
        {
          "lat": 37.60371965,
          "lon": 126.6985033,
          "depth": 1.1,
          "azimuth": 89.82
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 159,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371965,
          "lon": 126.6985033,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.60371964,
          "lon": 126.6985033,
          "depth": 0.35,
          "azimuth": 0
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 160,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371965,
          "lon": 126.6985033,
          "depth": 0.35,
          "azimuth": 89.81
        },
        {
          "lat": 37.60371974,
          "lon": 126.6985373,
          "depth": 0.35,
          "azimuth": 89.81
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 161,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371974,
          "lon": 126.6985373,
          "depth": 0.35,
          "azimuth": 0
        },
        {
          "lat": 37.60371973,
          "lon": 126.6985373,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 162,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60371974,
          "lon": 126.6985373,
          "depth": 1.1,
          "azimuth": 89.82
        },
        {
          "lat": 37.60371985,
          "lon": 126.6985806,
          "depth": 1.1,
          "azimuth": 89.82
        },
        {
          "lat": 37.60372005,
          "lon": 126.698659,
          "depth": 1.1,
          "azimuth": 89.82
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 163,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60724853,
          "lon": 126.6984523,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60634755,
          "lon": 126.6984559,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60611951,
          "lon": 126.6984568,
          "depth": 1.1,
          "azimuth": 179.82
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 164,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60611951,
          "lon": 126.6984568,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.6061195,
          "lon": 126.6984568,
          "depth": 2.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 165,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60611951,
          "lon": 126.6984568,
          "depth": 2.1,
          "azimuth": 179.75
        },
        {
          "lat": 37.60610149,
          "lon": 126.6984569,
          "depth": 2.1,
          "azimuth": 179.75
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 166,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60610149,
          "lon": 126.6984569,
          "depth": 2.1,
          "azimuth": 0
        },
        {
          "lat": 37.60610148,
          "lon": 126.6984569,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 167,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60610149,
          "lon": 126.6984569,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60599873,
          "lon": 126.6984573,
          "depth": 1.1,
          "azimuth": 179.82
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 168,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60599873,
          "lon": 126.6984573,
          "depth": 1.85,
          "azimuth": 0
        },
        {
          "lat": 37.60599872,
          "lon": 126.6984573,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 169,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60599873,
          "lon": 126.6984573,
          "depth": 1.85,
          "azimuth": 179.75
        },
        {
          "lat": 37.60598071,
          "lon": 126.6984574,
          "depth": 1.85,
          "azimuth": 179.75
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 170,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60598071,
          "lon": 126.6984574,
          "depth": 1.85,
          "azimuth": 0
        },
        {
          "lat": 37.605980699999996,
          "lon": 126.6984574,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 171,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60598071,
          "lon": 126.6984574,
          "depth": 1.1,
          "azimuth": 179.84
        },
        {
          "lat": 37.60589707,
          "lon": 126.6984577,
          "depth": 1.1,
          "azimuth": 179.84
        },
        {
          "lat": 37.60544658,
          "lon": 126.6984595,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60499609,
          "lon": 126.6984614,
          "depth": 1.1,
          "azimuth": 179.81
        },
        {
          "lat": 37.60454546,
          "lon": 126.6984632,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60409497,
          "lon": 126.698465,
          "depth": 1.1,
          "azimuth": 179.82
        },
        {
          "lat": 37.60372852,
          "lon": 126.6984665,
          "depth": 1.1,
          "azimuth": 179.81
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 172,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60372852,
          "lon": 126.6984665,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.603728509999996,
          "lon": 126.6984665,
          "depth": 1.85,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 173,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60372852,
          "lon": 126.6984665,
          "depth": 1.85,
          "azimuth": 180
        },
        {
          "lat": 37.6037105,
          "lon": 126.6984665,
          "depth": 1.85,
          "azimuth": 180
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 174,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6037105,
          "lon": 126.6984665,
          "depth": 1.85,
          "azimuth": 0
        },
        {
          "lat": 37.60371049,
          "lon": 126.6984665,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 175,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6037105,
          "lon": 126.6984665,
          "depth": 1.1,
          "azimuth": 179.79
        },
        {
          "lat": 37.60364448,
          "lon": 126.6984668,
          "depth": 1.1,
          "azimuth": 179.79
        },
        {
          "lat": 37.60329097,
          "lon": 126.6984682,
          "depth": 1.1,
          "azimuth": 179.82
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 176,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60329097,
          "lon": 126.6984682,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.60329096,
          "lon": 126.6984682,
          "depth": 1.6,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 177,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60329097,
          "lon": 126.6984682,
          "depth": 1.6,
          "azimuth": 179.75
        },
        {
          "lat": 37.60327295,
          "lon": 126.6984683,
          "depth": 1.6,
          "azimuth": 179.75
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 178,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60327295,
          "lon": 126.6984683,
          "depth": 1.6,
          "azimuth": 0
        },
        {
          "lat": 37.60327294,
          "lon": 126.6984683,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 179,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60327295,
          "lon": 126.6984683,
          "depth": 1.1,
          "azimuth": 179.83
        },
        {
          "lat": 37.60319399,
          "lon": 126.6984686,
          "depth": 1.1,
          "azimuth": 179.83
        },
        {
          "lat": 37.60303196,
          "lon": 126.6984693,
          "depth": 1.1,
          "azimuth": 179.8
        },
        {
          "lat": 37.60301394,
          "lon": 126.6984694,
          "depth": 1.1,
          "azimuth": 179.75
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 180,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60285401,
          "lon": 126.6926531,
          "depth": 0.5,
          "azimuth": 179.62
        },
        {
          "lat": 37.60247308,
          "lon": 126.6926563,
          "depth": 0.5,
          "azimuth": 179.62
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 181,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60285402,
          "lon": 126.6926553,
          "depth": 0.5,
          "azimuth": 179.62
        },
        {
          "lat": 37.6024731,
          "lon": 126.6926585,
          "depth": 0.5,
          "azimuth": 179.62
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 182,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60247309,
          "lon": 126.6926613,
          "depth": 0.5,
          "azimuth": 36.37
        },
        {
          "lat": 37.60248783,
          "lon": 126.692675,
          "depth": 0.5,
          "azimuth": 36.37
        },
        {
          "lat": 37.60250009,
          "lon": 126.6926922,
          "depth": 0.5,
          "azimuth": 48.02
        },
        {
          "lat": 37.60250936,
          "lon": 126.692712,
          "depth": 0.5,
          "azimuth": 59.42
        },
        {
          "lat": 37.60251529,
          "lon": 126.6927338,
          "depth": 0.5,
          "azimuth": 71.05
        },
        {
          "lat": 37.60251765,
          "lon": 126.6927596,
          "depth": 0.5,
          "azimuth": 83.41
        },
        {
          "lat": 37.60251809,
          "lon": 126.6934201,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60251896,
          "lon": 126.693447,
          "depth": 0.5,
          "azimuth": 87.66
        },
        {
          "lat": 37.60252004,
          "lon": 126.6934604,
          "depth": 0.5,
          "azimuth": 84.19
        },
        {
          "lat": 37.60254338,
          "lon": 126.6937032,
          "depth": 0.5,
          "azimuth": 83.08
        },
        {
          "lat": 37.60254484,
          "lon": 126.6937235,
          "depth": 0.5,
          "azimuth": 84.81
        },
        {
          "lat": 37.60254534,
          "lon": 126.6937438,
          "depth": 0.5,
          "azimuth": 88.22
        },
        {
          "lat": 37.60254588,
          "lon": 126.6945662,
          "depth": 0.5,
          "azimuth": 89.95
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 183,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60247076,
          "lon": 126.692662,
          "depth": 0.5,
          "azimuth": 36.31
        },
        {
          "lat": 37.60248661,
          "lon": 126.6926767,
          "depth": 0.5,
          "azimuth": 36.31
        },
        {
          "lat": 37.60249862,
          "lon": 126.6926935,
          "depth": 0.5,
          "azimuth": 47.94
        },
        {
          "lat": 37.60250772,
          "lon": 126.692713,
          "depth": 0.5,
          "azimuth": 59.5
        },
        {
          "lat": 37.60251352,
          "lon": 126.6927343,
          "depth": 0.5,
          "azimuth": 71.03
        },
        {
          "lat": 37.60251585,
          "lon": 126.6927597,
          "depth": 0.5,
          "azimuth": 83.4
        },
        {
          "lat": 37.60251629,
          "lon": 126.6934202,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60251716,
          "lon": 126.6934471,
          "depth": 0.5,
          "azimuth": 87.66
        },
        {
          "lat": 37.60251825,
          "lon": 126.6934607,
          "depth": 0.5,
          "azimuth": 84.22
        },
        {
          "lat": 37.60254158,
          "lon": 126.6937034,
          "depth": 0.5,
          "azimuth": 83.08
        },
        {
          "lat": 37.60254304,
          "lon": 126.6937236,
          "depth": 0.5,
          "azimuth": 84.79
        },
        {
          "lat": 37.60254354,
          "lon": 126.6937438,
          "depth": 0.5,
          "azimuth": 88.21
        },
        {
          "lat": 37.60254408,
          "lon": 126.6945662,
          "depth": 0.5,
          "azimuth": 89.95
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 184,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60254589,
          "lon": 126.6945752,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60254738,
          "lon": 126.6968675,
          "depth": 0.5,
          "azimuth": 89.95
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 185,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60254409,
          "lon": 126.6945752,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60254558,
          "lon": 126.6968675,
          "depth": 0.5,
          "azimuth": 89.95
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 186,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60254739,
          "lon": 126.6968766,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60254753,
          "lon": 126.6970963,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60254706,
          "lon": 126.6971167,
          "depth": 0.5,
          "azimuth": 91.67
        },
        {
          "lat": 37.60254562,
          "lon": 126.697137,
          "depth": 0.5,
          "azimuth": 95.12
        },
        {
          "lat": 37.60252261,
          "lon": 126.6973791,
          "depth": 0.5,
          "azimuth": 96.84
        },
        {
          "lat": 37.60252118,
          "lon": 126.6973993,
          "depth": 0.5,
          "azimuth": 95.11
        },
        {
          "lat": 37.60252071,
          "lon": 126.6974195,
          "depth": 0.5,
          "azimuth": 91.68
        },
        {
          "lat": 37.60252094,
          "lon": 126.6977847,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60252087,
          "lon": 126.6978691,
          "depth": 0.5,
          "azimuth": 90.06
        },
        {
          "lat": 37.60252044,
          "lon": 126.697971,
          "depth": 0.5,
          "azimuth": 90.31
        },
        {
          "lat": 37.60251965,
          "lon": 126.6980729,
          "depth": 0.5,
          "azimuth": 90.56
        },
        {
          "lat": 37.60251849,
          "lon": 126.6981748,
          "depth": 0.5,
          "azimuth": 90.82
        },
        {
          "lat": 37.60251825,
          "lon": 126.6981929,
          "depth": 0.5,
          "azimuth": 90.96
        },
        {
          "lat": 37.60251505,
          "lon": 126.6982766,
          "depth": 0.5,
          "azimuth": 92.76
        },
        {
          "lat": 37.60250973,
          "lon": 126.6983783,
          "depth": 0.5,
          "azimuth": 93.78
        },
        {
          "lat": 37.60250284,
          "lon": 126.6984799,
          "depth": 0.5,
          "azimuth": 94.89
        },
        {
          "lat": 37.60249441,
          "lon": 126.6985812,
          "depth": 0.5,
          "azimuth": 96
        },
        {
          "lat": 37.60248441,
          "lon": 126.6986824,
          "depth": 0.5,
          "azimuth": 97.11
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 187,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60254559,
          "lon": 126.6968766,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60254573,
          "lon": 126.6970962,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60254526,
          "lon": 126.6971165,
          "depth": 0.5,
          "azimuth": 91.67
        },
        {
          "lat": 37.60254382,
          "lon": 126.6971367,
          "depth": 0.5,
          "azimuth": 95.14
        },
        {
          "lat": 37.60252082,
          "lon": 126.6973789,
          "depth": 0.5,
          "azimuth": 96.83
        },
        {
          "lat": 37.60251938,
          "lon": 126.6973992,
          "depth": 0.5,
          "azimuth": 95.12
        },
        {
          "lat": 37.60251891,
          "lon": 126.6974195,
          "depth": 0.5,
          "azimuth": 91.67
        },
        {
          "lat": 37.60251914,
          "lon": 126.6977847,
          "depth": 0.5,
          "azimuth": 89.95
        },
        {
          "lat": 37.60251907,
          "lon": 126.697869,
          "depth": 0.5,
          "azimuth": 90.06
        },
        {
          "lat": 37.60251864,
          "lon": 126.697971,
          "depth": 0.5,
          "azimuth": 90.3
        },
        {
          "lat": 37.60251785,
          "lon": 126.6980729,
          "depth": 0.5,
          "azimuth": 90.56
        },
        {
          "lat": 37.60251669,
          "lon": 126.6981748,
          "depth": 0.5,
          "azimuth": 90.82
        },
        {
          "lat": 37.60251644,
          "lon": 126.6981929,
          "depth": 0.5,
          "azimuth": 91
        },
        {
          "lat": 37.60251324,
          "lon": 126.6982765,
          "depth": 0.5,
          "azimuth": 92.77
        },
        {
          "lat": 37.60250793,
          "lon": 126.6983781,
          "depth": 0.5,
          "azimuth": 93.77
        },
        {
          "lat": 37.60250105,
          "lon": 126.6984796,
          "depth": 0.5,
          "azimuth": 94.89
        },
        {
          "lat": 37.60249261,
          "lon": 126.698581,
          "depth": 0.5,
          "azimuth": 96
        },
        {
          "lat": 37.6024826,
          "lon": 126.6986824,
          "depth": 0.5,
          "azimuth": 97.1
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 188,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60248671,
          "lon": 126.6986914,
          "depth": 0.5,
          "azimuth": 58.51
        },
        {
          "lat": 37.60249166,
          "lon": 126.6987016,
          "depth": 0.5,
          "azimuth": 58.51
        },
        {
          "lat": 37.60249771,
          "lon": 126.6987179,
          "depth": 0.5,
          "azimuth": 64.9
        },
        {
          "lat": 37.60250188,
          "lon": 126.6987352,
          "depth": 0.5,
          "azimuth": 73.08
        },
        {
          "lat": 37.6025041,
          "lon": 126.698753,
          "depth": 0.5,
          "azimuth": 81.05
        },
        {
          "lat": 37.60250433,
          "lon": 126.698771,
          "depth": 0.5,
          "azimuth": 89.08
        },
        {
          "lat": 37.6024995,
          "lon": 126.6989025,
          "depth": 0.5,
          "azimuth": 92.65
        },
        {
          "lat": 37.60249533,
          "lon": 126.6990043,
          "depth": 0.5,
          "azimuth": 92.96
        },
        {
          "lat": 37.60248592,
          "lon": 126.6992078,
          "depth": 0.5,
          "azimuth": 93.34
        },
        {
          "lat": 37.60248066,
          "lon": 126.6993095,
          "depth": 0.5,
          "azimuth": 93.74
        },
        {
          "lat": 37.60247519,
          "lon": 126.6994085,
          "depth": 0.5,
          "azimuth": 93.99
        },
        {
          "lat": 37.60247472,
          "lon": 126.6994464,
          "depth": 0.5,
          "azimuth": 90.9
        },
        {
          "lat": 37.60248261,
          "lon": 126.699691,
          "depth": 0.5,
          "azimuth": 87.67
        },
        {
          "lat": 37.60248268,
          "lon": 126.6997167,
          "depth": 0.5,
          "azimuth": 89.8
        },
        {
          "lat": 37.60248184,
          "lon": 126.6997341,
          "depth": 0.5,
          "azimuth": 93.49
        },
        {
          "lat": 37.60247594,
          "lon": 126.6998183,
          "depth": 0.5,
          "azimuth": 95.05
        },
        {
          "lat": 37.60246849,
          "lon": 126.6999198,
          "depth": 0.5,
          "azimuth": 95.29
        },
        {
          "lat": 37.60246067,
          "lon": 126.7000212,
          "depth": 0.5,
          "azimuth": 95.56
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 189,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60248459,
          "lon": 126.6986914,
          "depth": 0.5,
          "azimuth": 58.3
        },
        {
          "lat": 37.60249007,
          "lon": 126.6987026,
          "depth": 0.5,
          "azimuth": 58.3
        },
        {
          "lat": 37.60249602,
          "lon": 126.6987187,
          "depth": 0.5,
          "azimuth": 64.99
        },
        {
          "lat": 37.60250012,
          "lon": 126.6987357,
          "depth": 0.5,
          "azimuth": 73.07
        },
        {
          "lat": 37.6025023,
          "lon": 126.6987532,
          "depth": 0.5,
          "azimuth": 81.06
        },
        {
          "lat": 37.60250252,
          "lon": 126.698771,
          "depth": 0.5,
          "azimuth": 89.11
        },
        {
          "lat": 37.6024977,
          "lon": 126.6989024,
          "depth": 0.5,
          "azimuth": 92.65
        },
        {
          "lat": 37.60249354,
          "lon": 126.6990042,
          "depth": 0.5,
          "azimuth": 92.95
        },
        {
          "lat": 37.60248412,
          "lon": 126.6992077,
          "depth": 0.5,
          "azimuth": 93.34
        },
        {
          "lat": 37.60247886,
          "lon": 126.6993094,
          "depth": 0.5,
          "azimuth": 93.74
        },
        {
          "lat": 37.60247339,
          "lon": 126.6994084,
          "depth": 0.5,
          "azimuth": 93.99
        },
        {
          "lat": 37.60247292,
          "lon": 126.6994465,
          "depth": 0.5,
          "azimuth": 90.89
        },
        {
          "lat": 37.60248081,
          "lon": 126.6996911,
          "depth": 0.5,
          "azimuth": 87.67
        },
        {
          "lat": 37.60248088,
          "lon": 126.6997167,
          "depth": 0.5,
          "azimuth": 89.8
        },
        {
          "lat": 37.60248004,
          "lon": 126.699734,
          "depth": 0.5,
          "azimuth": 93.51
        },
        {
          "lat": 37.60247414,
          "lon": 126.6998181,
          "depth": 0.5,
          "azimuth": 95.06
        },
        {
          "lat": 37.60246669,
          "lon": 126.6999196,
          "depth": 0.5,
          "azimuth": 95.29
        },
        {
          "lat": 37.60245886,
          "lon": 126.7000212,
          "depth": 0.5,
          "azimuth": 95.56
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 190,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60245995,
          "lon": 126.7000303,
          "depth": 0.5,
          "azimuth": 95.92
        },
        {
          "lat": 37.60244672,
          "lon": 126.7001914,
          "depth": 0.5,
          "azimuth": 95.92
        },
        {
          "lat": 37.60242876,
          "lon": 126.700394,
          "depth": 0.5,
          "azimuth": 96.38
        },
        {
          "lat": 37.60240933,
          "lon": 126.7005964,
          "depth": 0.5,
          "azimuth": 96.91
        },
        {
          "lat": 37.60238845,
          "lon": 126.7007985,
          "depth": 0.5,
          "azimuth": 97.43
        },
        {
          "lat": 37.60236611,
          "lon": 126.7010004,
          "depth": 0.5,
          "azimuth": 97.95
        },
        {
          "lat": 37.60233797,
          "lon": 126.7012375,
          "depth": 0.5,
          "azimuth": 98.52
        },
        {
          "lat": 37.60232841,
          "lon": 126.701306,
          "depth": 0.5,
          "azimuth": 99.99
        },
        {
          "lat": 37.60231258,
          "lon": 126.7014024,
          "depth": 0.5,
          "azimuth": 101.71
        },
        {
          "lat": 37.60229465,
          "lon": 126.7015018,
          "depth": 0.5,
          "azimuth": 102.83
        },
        {
          "lat": 37.60227517,
          "lon": 126.7016007,
          "depth": 0.5,
          "azimuth": 103.96
        },
        {
          "lat": 37.60224688,
          "lon": 126.7017315,
          "depth": 0.5,
          "azimuth": 105.27
        },
        {
          "lat": 37.60218073,
          "lon": 126.7019906,
          "depth": 0.5,
          "azimuth": 107.86
        },
        {
          "lat": 37.60213374,
          "lon": 126.7021857,
          "depth": 0.5,
          "azimuth": 106.91
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 191,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60245814,
          "lon": 126.7000303,
          "depth": 0.5,
          "azimuth": 95.92
        },
        {
          "lat": 37.60244493,
          "lon": 126.7001912,
          "depth": 0.5,
          "azimuth": 95.92
        },
        {
          "lat": 37.60242696,
          "lon": 126.7003938,
          "depth": 0.5,
          "azimuth": 96.39
        },
        {
          "lat": 37.60240755,
          "lon": 126.7005961,
          "depth": 0.5,
          "azimuth": 96.91
        },
        {
          "lat": 37.60238666,
          "lon": 126.7007982,
          "depth": 0.5,
          "azimuth": 97.43
        },
        {
          "lat": 37.60236433,
          "lon": 126.7010001,
          "depth": 0.5,
          "azimuth": 97.95
        },
        {
          "lat": 37.6023362,
          "lon": 126.7012372,
          "depth": 0.5,
          "azimuth": 98.52
        },
        {
          "lat": 37.60232664,
          "lon": 126.7013056,
          "depth": 0.5,
          "azimuth": 100
        },
        {
          "lat": 37.60231082,
          "lon": 126.7014019,
          "depth": 0.5,
          "azimuth": 101.71
        },
        {
          "lat": 37.6022929,
          "lon": 126.7015013,
          "depth": 0.5,
          "azimuth": 102.82
        },
        {
          "lat": 37.60227343,
          "lon": 126.7016001,
          "depth": 0.5,
          "azimuth": 103.97
        },
        {
          "lat": 37.60224516,
          "lon": 126.7017308,
          "depth": 0.5,
          "azimuth": 105.27
        },
        {
          "lat": 37.60217902,
          "lon": 126.70199,
          "depth": 0.5,
          "azimuth": 107.85
        },
        {
          "lat": 37.60213185,
          "lon": 126.7021857,
          "depth": 0.5,
          "azimuth": 106.92
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 192,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60213161,
          "lon": 126.7021948,
          "depth": 0.5,
          "azimuth": 105.93
        },
        {
          "lat": 37.60207238,
          "lon": 126.7024567,
          "depth": 0.5,
          "azimuth": 105.93
        },
        {
          "lat": 37.60203076,
          "lon": 126.702653,
          "depth": 0.5,
          "azimuth": 104.98
        },
        {
          "lat": 37.60199475,
          "lon": 126.7028525,
          "depth": 0.5,
          "azimuth": 102.83
        },
        {
          "lat": 37.60194537,
          "lon": 126.7031131,
          "depth": 0.5,
          "azimuth": 103.45
        },
        {
          "lat": 37.60170717,
          "lon": 126.7043379,
          "depth": 0.5,
          "azimuth": 103.79
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 193,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60212973,
          "lon": 126.7021948,
          "depth": 0.5,
          "azimuth": 105.93
        },
        {
          "lat": 37.60207065,
          "lon": 126.7024561,
          "depth": 0.5,
          "azimuth": 105.93
        },
        {
          "lat": 37.60202901,
          "lon": 126.7026525,
          "depth": 0.5,
          "azimuth": 104.98
        },
        {
          "lat": 37.60199299,
          "lon": 126.702852,
          "depth": 0.5,
          "azimuth": 102.84
        },
        {
          "lat": 37.60194362,
          "lon": 126.7031126,
          "depth": 0.5,
          "azimuth": 103.45
        },
        {
          "lat": 37.60170532,
          "lon": 126.7043379,
          "depth": 0.5,
          "azimuth": 103.79
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 194,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6017054,
          "lon": 126.704347,
          "depth": 0.5,
          "azimuth": 103.79
        },
        {
          "lat": 37.60140875,
          "lon": 126.7058722,
          "depth": 0.5,
          "azimuth": 103.79
        },
        {
          "lat": 37.60133902,
          "lon": 126.7062505,
          "depth": 0.5,
          "azimuth": 103.1
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 195,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60170355,
          "lon": 126.704347,
          "depth": 0.5,
          "azimuth": 103.79
        },
        {
          "lat": 37.601407,
          "lon": 126.7058717,
          "depth": 0.5,
          "azimuth": 103.79
        },
        {
          "lat": 37.60133717,
          "lon": 126.7062505,
          "depth": 0.5,
          "azimuth": 103.1
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 196,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60286004,
          "lon": 126.6986893,
          "depth": 0.5,
          "azimuth": 180.43
        },
        {
          "lat": 37.60249067,
          "lon": 126.6986858,
          "depth": 0.5,
          "azimuth": 180.43
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 197,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60286002,
          "lon": 126.6986915,
          "depth": 0.5,
          "azimuth": 180.42
        },
        {
          "lat": 37.60249066,
          "lon": 126.6986881,
          "depth": 0.5,
          "azimuth": 180.42
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 198,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60287026,
          "lon": 126.6986859,
          "depth": 0.5,
          "azimuth": 320.92
        },
        {
          "lat": 37.60288509,
          "lon": 126.6986707,
          "depth": 0.5,
          "azimuth": 320.92
        },
        {
          "lat": 37.60290112,
          "lon": 126.6986576,
          "depth": 0.5,
          "azimuth": 327.08
        },
        {
          "lat": 37.60291816,
          "lon": 126.6986466,
          "depth": 0.5,
          "azimuth": 332.91
        },
        {
          "lat": 37.60293602,
          "lon": 126.698638,
          "depth": 0.5,
          "azimuth": 339.12
        },
        {
          "lat": 37.60296397,
          "lon": 126.6986296,
          "depth": 0.5,
          "azimuth": 346.61
        },
        {
          "lat": 37.60299263,
          "lon": 126.6986269,
          "depth": 0.5,
          "azimuth": 355.73
        },
        {
          "lat": 37.60361191,
          "lon": 126.6986244,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60362508,
          "lon": 126.6986258,
          "depth": 0.5,
          "azimuth": 4.81
        },
        {
          "lat": 37.60363783,
          "lon": 126.6986302,
          "depth": 0.5,
          "azimuth": 15.29
        },
        {
          "lat": 37.60364973,
          "lon": 126.6986375,
          "depth": 0.5,
          "azimuth": 25.92
        },
        {
          "lat": 37.60366041,
          "lon": 126.6986473,
          "depth": 0.5,
          "azimuth": 36.02
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 199,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60287313,
          "lon": 126.6986859,
          "depth": 0.5,
          "azimuth": 321.04
        },
        {
          "lat": 37.60288616,
          "lon": 126.6986726,
          "depth": 0.5,
          "azimuth": 321.04
        },
        {
          "lat": 37.60290203,
          "lon": 126.6986596,
          "depth": 0.5,
          "azimuth": 327.02
        },
        {
          "lat": 37.60291889,
          "lon": 126.6986487,
          "depth": 0.5,
          "azimuth": 332.88
        },
        {
          "lat": 37.60293656,
          "lon": 126.6986402,
          "depth": 0.5,
          "azimuth": 339.14
        },
        {
          "lat": 37.60296425,
          "lon": 126.6986318,
          "depth": 0.5,
          "azimuth": 346.49
        },
        {
          "lat": 37.60299269,
          "lon": 126.6986291,
          "depth": 0.5,
          "azimuth": 355.7
        },
        {
          "lat": 37.60361184,
          "lon": 126.6986266,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60362476,
          "lon": 126.698628,
          "depth": 0.5,
          "azimuth": 4.91
        },
        {
          "lat": 37.6036372,
          "lon": 126.6986324,
          "depth": 0.5,
          "azimuth": 15.65
        },
        {
          "lat": 37.6036488,
          "lon": 126.6986394,
          "depth": 0.5,
          "azimuth": 25.55
        },
        {
          "lat": 37.60365737,
          "lon": 126.6986473,
          "depth": 0.5,
          "azimuth": 36.14
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 200,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60367058,
          "lon": 126.6986489,
          "depth": 0.5,
          "azimuth": 350.55
        },
        {
          "lat": 37.60371058,
          "lon": 126.6986405,
          "depth": 0.5,
          "azimuth": 350.55
        },
        {
          "lat": 37.60375077,
          "lon": 126.6986338,
          "depth": 0.5,
          "azimuth": 352.48
        },
        {
          "lat": 37.60378045,
          "lon": 126.6986299,
          "depth": 0.5,
          "azimuth": 354.06
        },
        {
          "lat": 37.60383156,
          "lon": 126.6986253,
          "depth": 0.5,
          "azimuth": 355.92
        },
        {
          "lat": 37.60389122,
          "lon": 126.6986232,
          "depth": 0.5,
          "azimuth": 358.4
        },
        {
          "lat": 37.6042792,
          "lon": 126.6986217,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60430593,
          "lon": 126.6986232,
          "depth": 0.5,
          "azimuth": 2.55
        },
        {
          "lat": 37.60433241,
          "lon": 126.6986281,
          "depth": 0.5,
          "azimuth": 8.34
        },
        {
          "lat": 37.60441511,
          "lon": 126.6986485,
          "depth": 0.5,
          "azimuth": 11.06
        },
        {
          "lat": 37.60444142,
          "lon": 126.6986533,
          "depth": 0.5,
          "azimuth": 8.22
        },
        {
          "lat": 37.60446796,
          "lon": 126.6986549,
          "depth": 0.5,
          "azimuth": 2.73
        },
        {
          "lat": 37.6048971,
          "lon": 126.6986531,
          "depth": 0.5,
          "azimuth": 359.81
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 201,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60367088,
          "lon": 126.6986511,
          "depth": 0.5,
          "azimuth": 350.54
        },
        {
          "lat": 37.60371084,
          "lon": 126.6986427,
          "depth": 0.5,
          "azimuth": 350.54
        },
        {
          "lat": 37.60375098,
          "lon": 126.698636,
          "depth": 0.5,
          "azimuth": 352.47
        },
        {
          "lat": 37.60378061,
          "lon": 126.6986321,
          "depth": 0.5,
          "azimuth": 354.05
        },
        {
          "lat": 37.60383164,
          "lon": 126.6986275,
          "depth": 0.5,
          "azimuth": 355.92
        },
        {
          "lat": 37.60389124,
          "lon": 126.6986255,
          "depth": 0.5,
          "azimuth": 358.48
        },
        {
          "lat": 37.60427916,
          "lon": 126.6986239,
          "depth": 0.5,
          "azimuth": 359.81
        },
        {
          "lat": 37.60430576,
          "lon": 126.6986255,
          "depth": 0.5,
          "azimuth": 2.73
        },
        {
          "lat": 37.60433211,
          "lon": 126.6986303,
          "depth": 0.5,
          "azimuth": 8.21
        },
        {
          "lat": 37.60441481,
          "lon": 126.6986507,
          "depth": 0.5,
          "azimuth": 11.06
        },
        {
          "lat": 37.60444124,
          "lon": 126.6986556,
          "depth": 0.5,
          "azimuth": 8.36
        },
        {
          "lat": 37.60446793,
          "lon": 126.6986571,
          "depth": 0.5,
          "azimuth": 2.55
        },
        {
          "lat": 37.60489711,
          "lon": 126.6986554,
          "depth": 0.5,
          "azimuth": 359.82
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 202,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60491242,
          "lon": 126.6986531,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60526046,
          "lon": 126.6986517,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60528718,
          "lon": 126.6986499,
          "depth": 0.5,
          "azimuth": 356.95
        },
        {
          "lat": 37.60531741,
          "lon": 126.6986438,
          "depth": 0.5,
          "azimuth": 350.92
        },
        {
          "lat": 37.60539687,
          "lon": 126.6986235,
          "depth": 0.5,
          "azimuth": 348.56
        },
        {
          "lat": 37.60542284,
          "lon": 126.6986186,
          "depth": 0.5,
          "azimuth": 351.5
        },
        {
          "lat": 37.60543593,
          "lon": 126.6986174,
          "depth": 0.5,
          "azimuth": 355.85
        },
        {
          "lat": 37.60544905,
          "lon": 126.6986169,
          "depth": 0.5,
          "azimuth": 358.27
        },
        {
          "lat": 37.60588306,
          "lon": 126.6986152,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60592724,
          "lon": 126.6986156,
          "depth": 0.5,
          "azimuth": 0.41
        },
        {
          "lat": 37.60596411,
          "lon": 126.6986175,
          "depth": 0.5,
          "azimuth": 2.34
        },
        {
          "lat": 37.60600455,
          "lon": 126.6986212,
          "depth": 0.5,
          "azimuth": 4.15
        },
        {
          "lat": 37.60604487,
          "lon": 126.6986265,
          "depth": 0.5,
          "azimuth": 5.95
        },
        {
          "lat": 37.60607804,
          "lon": 126.6986322,
          "depth": 0.5,
          "azimuth": 7.75
        },
        {
          "lat": 37.60611109,
          "lon": 126.698639,
          "depth": 0.5,
          "azimuth": 9.26
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 203,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60491242,
          "lon": 126.6986553,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60526052,
          "lon": 126.6986539,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60528738,
          "lon": 126.6986522,
          "depth": 0.5,
          "azimuth": 357.13
        },
        {
          "lat": 37.60531773,
          "lon": 126.6986461,
          "depth": 0.5,
          "azimuth": 350.95
        },
        {
          "lat": 37.60539719,
          "lon": 126.6986258,
          "depth": 0.5,
          "azimuth": 348.56
        },
        {
          "lat": 37.60542304,
          "lon": 126.6986209,
          "depth": 0.5,
          "azimuth": 351.46
        },
        {
          "lat": 37.60543602,
          "lon": 126.6986197,
          "depth": 0.5,
          "azimuth": 355.81
        },
        {
          "lat": 37.60544908,
          "lon": 126.6986192,
          "depth": 0.5,
          "azimuth": 358.26
        },
        {
          "lat": 37.60588306,
          "lon": 126.6986175,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.6059272,
          "lon": 126.6986179,
          "depth": 0.5,
          "azimuth": 0.41
        },
        {
          "lat": 37.60596401,
          "lon": 126.6986198,
          "depth": 0.5,
          "azimuth": 2.34
        },
        {
          "lat": 37.60600439,
          "lon": 126.6986234,
          "depth": 0.5,
          "azimuth": 4.04
        },
        {
          "lat": 37.60604465,
          "lon": 126.6986288,
          "depth": 0.5,
          "azimuth": 6.07
        },
        {
          "lat": 37.60607778,
          "lon": 126.6986344,
          "depth": 0.5,
          "azimuth": 7.63
        },
        {
          "lat": 37.6061111,
          "lon": 126.6986413,
          "depth": 0.5,
          "azimuth": 9.32
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 204,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6036631,
          "lon": 126.6983627,
          "depth": 0.5,
          "azimuth": 89.82
        },
        {
          "lat": 37.60366382,
          "lon": 126.6986473,
          "depth": 0.5,
          "azimuth": 89.82
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 205,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60366129,
          "lon": 126.6983627,
          "depth": 0.5,
          "azimuth": 89.81
        },
        {
          "lat": 37.60366202,
          "lon": 126.6986473,
          "depth": 0.5,
          "azimuth": 89.81
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 206,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60366384,
          "lon": 126.6983555,
          "depth": 0.5,
          "azimuth": 328.58
        },
        {
          "lat": 37.60367227,
          "lon": 126.698349,
          "depth": 0.5,
          "azimuth": 328.58
        },
        {
          "lat": 37.60367884,
          "lon": 126.6983398,
          "depth": 0.5,
          "azimuth": 312.03
        },
        {
          "lat": 37.60368215,
          "lon": 126.6983317,
          "depth": 0.5,
          "azimuth": 297.28
        },
        {
          "lat": 37.60368386,
          "lon": 126.6983241,
          "depth": 0.5,
          "azimuth": 285.85
        },
        {
          "lat": 37.60368443,
          "lon": 126.6983162,
          "depth": 0.5,
          "azimuth": 275.2
        },
        {
          "lat": 37.60368363,
          "lon": 126.698002,
          "depth": 0.5,
          "azimuth": 269.82
        },
        {
          "lat": 37.60367208,
          "lon": 126.6977209,
          "depth": 0.5,
          "azimuth": 267.03
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 207,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60367256,
          "lon": 126.6977118,
          "depth": 0.5,
          "azimuth": 283.81
        },
        {
          "lat": 37.60367856,
          "lon": 126.697681,
          "depth": 0.5,
          "azimuth": 283.81
        },
        {
          "lat": 37.60368025,
          "lon": 126.6976493,
          "depth": 0.5,
          "azimuth": 273.85
        },
        {
          "lat": 37.60367732,
          "lon": 126.6965051,
          "depth": 0.5,
          "azimuth": 269.82
        },
        {
          "lat": 37.60367692,
          "lon": 126.6963523,
          "depth": 0.5,
          "azimuth": 269.81
        },
        {
          "lat": 37.6036695,
          "lon": 126.6962976,
          "depth": 0.5,
          "azimuth": 260.28
        },
        {
          "lat": 37.60363706,
          "lon": 126.6961929,
          "depth": 0.5,
          "azimuth": 248.64
        },
        {
          "lat": 37.603602,
          "lon": 126.6961287,
          "depth": 0.5,
          "azimuth": 235.42
        },
        {
          "lat": 37.60354325,
          "lon": 126.6960619,
          "depth": 0.5,
          "azimuth": 222.01
        },
        {
          "lat": 37.60348929,
          "lon": 126.6960261,
          "depth": 0.5,
          "azimuth": 207.73
        },
        {
          "lat": 37.60341197,
          "lon": 126.6959961,
          "depth": 0.5,
          "azimuth": 197.09
        },
        {
          "lat": 37.60337185,
          "lon": 126.6959889,
          "depth": 0.5,
          "azimuth": 188.09
        },
        {
          "lat": 37.60333008,
          "lon": 126.6959893,
          "depth": 0.5,
          "azimuth": 179.57
        },
        {
          "lat": 37.60311114,
          "lon": 126.6959962,
          "depth": 0.5,
          "azimuth": 178.57
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 208,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60310305,
          "lon": 126.6960007,
          "depth": 0.5,
          "azimuth": 89.81
        },
        {
          "lat": 37.60310758,
          "lon": 126.6977623,
          "depth": 0.5,
          "azimuth": 89.81
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 209,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60311351,
          "lon": 126.6977693,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60362015,
          "lon": 126.6977673,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60363388,
          "lon": 126.6977606,
          "depth": 0.5,
          "azimuth": 338.86
        },
        {
          "lat": 37.6036461,
          "lon": 126.6977503,
          "depth": 0.5,
          "azimuth": 326.27
        },
        {
          "lat": 37.60365622,
          "lon": 126.6977368,
          "depth": 0.5,
          "azimuth": 313.42
        },
        {
          "lat": 37.60366374,
          "lon": 126.6977209,
          "depth": 0.5,
          "azimuth": 300.84
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 210,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60366845,
          "lon": 126.6986563,
          "depth": 0.5,
          "azimuth": 42.67
        },
        {
          "lat": 37.60367859,
          "lon": 126.6986681,
          "depth": 0.5,
          "azimuth": 42.67
        },
        {
          "lat": 37.60368635,
          "lon": 126.6986824,
          "depth": 0.5,
          "azimuth": 55.59
        },
        {
          "lat": 37.60369131,
          "lon": 126.6986986,
          "depth": 0.5,
          "azimuth": 68.87
        },
        {
          "lat": 37.60369324,
          "lon": 126.6987157,
          "depth": 0.5,
          "azimuth": 81.89
        },
        {
          "lat": 37.6036891,
          "lon": 126.6993063,
          "depth": 0.5,
          "azimuth": 90.51
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 211,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6036889,
          "lon": 126.6993154,
          "depth": 0.5,
          "azimuth": 90.53
        },
        {
          "lat": 37.6036833,
          "lon": 126.7000733,
          "depth": 0.5,
          "azimuth": 90.53
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 212,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60368474,
          "lon": 126.7000824,
          "depth": 0.5,
          "azimuth": 94.99
        },
        {
          "lat": 37.60359346,
          "lon": 126.7014024,
          "depth": 0.5,
          "azimuth": 94.99
        },
        {
          "lat": 37.60358567,
          "lon": 126.7015038,
          "depth": 0.5,
          "azimuth": 95.54
        },
        {
          "lat": 37.6035822,
          "lon": 126.7015185,
          "depth": 0.5,
          "azimuth": 106.59
        },
        {
          "lat": 37.60357606,
          "lon": 126.7015316,
          "depth": 0.5,
          "azimuth": 120.61
        },
        {
          "lat": 37.60356611,
          "lon": 126.7015441,
          "depth": 0.5,
          "azimuth": 135.14
        },
        {
          "lat": 37.60355383,
          "lon": 126.7015526,
          "depth": 0.5,
          "azimuth": 151.26
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 213,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60354527,
          "lon": 126.7015617,
          "depth": 0.5,
          "azimuth": 128.21
        },
        {
          "lat": 37.60353866,
          "lon": 126.7015723,
          "depth": 0.5,
          "azimuth": 128.21
        },
        {
          "lat": 37.60352998,
          "lon": 126.7015801,
          "depth": 0.5,
          "azimuth": 144.55
        },
        {
          "lat": 37.60351991,
          "lon": 126.7015847,
          "depth": 0.5,
          "azimuth": 160.1
        },
        {
          "lat": 37.60350924,
          "lon": 126.7015856,
          "depth": 0.5,
          "azimuth": 176.18
        },
        {
          "lat": 37.60303798,
          "lon": 126.7015204,
          "depth": 0.5,
          "azimuth": 186.26
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 214,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60303786,
          "lon": 126.7015113,
          "depth": 0.5,
          "azimuth": 275.36
        },
        {
          "lat": 37.60313903,
          "lon": 126.7001504,
          "depth": 0.5,
          "azimuth": 275.36
        },
        {
          "lat": 37.60314196,
          "lon": 126.7000895,
          "depth": 0.5,
          "azimuth": 273.48
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 215,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60314336,
          "lon": 126.7000804,
          "depth": 0.5,
          "azimuth": 269.82
        },
        {
          "lat": 37.60314134,
          "lon": 126.6992861,
          "depth": 0.5,
          "azimuth": 269.82
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 216,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60315536,
          "lon": 126.6992813,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60362476,
          "lon": 126.6992794,
          "depth": 0.5,
          "azimuth": 359.82
        },
        {
          "lat": 37.60368099,
          "lon": 126.6993125,
          "depth": 0.5,
          "azimuth": 25
        }
      ],
      "diameter": 100,
      "category": 9,
      "shape": 0,
      "azimuth": 0
    },
    {
      "groupNo": 217,
      "type": "line",
      "geometry": [
        {
          "lat": 37.60518923,
          "lon": 126.6985144,
          "depth": 2.5,
          "azimuth": 179.82
        },
        {
          "lat": 37.60446849,
          "lon": 126.6985173,
          "depth": 2.52,
          "azimuth": 179.82
        },
        {
          "lat": 37.60374767,
          "lon": 126.6985202,
          "depth": 2.39,
          "azimuth": 179.82
        },
        {
          "lat": 37.60314401,
          "lon": 126.6985226,
          "depth": 2.4,
          "azimuth": 179.82
        },
        {
          "lat": 37.6027593,
          "lon": 126.6985242,
          "depth": 2.17,
          "azimuth": 179.81
        }
      ],
      "category": 3,
      "width": 1.5,
      "height": 1.8,
      "shape": 1,
      "azimuth": 0
    },
    {
      "groupNo": 218,
      "type": "line",
      "geometry": [
        {
          "lat": 37.6027593,
          "lon": 126.6985242,
          "depth": 2.27,
          "azimuth": 179.82
        },
        {
          "lat": 37.602489,
          "lon": 126.6985253,
          "depth": 2.62,
          "azimuth": 179.82
        }
      ],
      "category": 3,
      "width": 2,
      "height": 2,
      "shape": 1,
      "azimuth": 0
    },
    {
      "groupNo": 100000,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.6061197,
          "lon": 126.6984455,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.60611969,
          "lon": 126.6984455,
          "depth": 2.1,
          "azimuth": 0
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100001,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60610168,
          "lon": 126.6984456,
          "depth": 2.1,
          "azimuth": 0
        },
        {
          "lat": 37.60610167,
          "lon": 126.6984456,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100002,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60328818,
          "lon": 126.6984569,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.60328817,
          "lon": 126.6984569,
          "depth": 1.6,
          "azimuth": 0
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100003,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60327016,
          "lon": 126.698457,
          "depth": 1.6,
          "azimuth": 0
        },
        {
          "lat": 37.60327015,
          "lon": 126.698457,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 355,
      "category": 7,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100004,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60371965,
          "lon": 126.6985033,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.60371964,
          "lon": 126.6985033,
          "depth": 0.35,
          "azimuth": 0
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100005,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60371974,
          "lon": 126.6985373,
          "depth": 0.35,
          "azimuth": 0
        },
        {
          "lat": 37.60371973,
          "lon": 126.6985373,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 280,
      "category": 7,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100006,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60611951,
          "lon": 126.6984568,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.6061195,
          "lon": 126.6984568,
          "depth": 2.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100007,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60610149,
          "lon": 126.6984569,
          "depth": 2.1,
          "azimuth": 0
        },
        {
          "lat": 37.60610148,
          "lon": 126.6984569,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100008,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60599873,
          "lon": 126.6984573,
          "depth": 1.85,
          "azimuth": 0
        },
        {
          "lat": 37.60599872,
          "lon": 126.6984573,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100009,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60598071,
          "lon": 126.6984574,
          "depth": 1.85,
          "azimuth": 0
        },
        {
          "lat": 37.605980699999996,
          "lon": 126.6984574,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100010,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60372852,
          "lon": 126.6984665,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.603728509999996,
          "lon": 126.6984665,
          "depth": 1.85,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100011,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.6037105,
          "lon": 126.6984665,
          "depth": 1.85,
          "azimuth": 0
        },
        {
          "lat": 37.60371049,
          "lon": 126.6984665,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100012,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60329097,
          "lon": 126.6984682,
          "depth": 1.1,
          "azimuth": 0
        },
        {
          "lat": 37.60329096,
          "lon": 126.6984682,
          "depth": 1.6,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 2,
      "azimuth": 0
    },
    {
      "groupNo": 100013,
      "type": "cylinder",
      "geometry": [
        {
          "lat": 37.60327295,
          "lon": 126.6984683,
          "depth": 1.6,
          "azimuth": 0
        },
        {
          "lat": 37.60327294,
          "lon": 126.6984683,
          "depth": 1.1,
          "azimuth": 0
        }
      ],
      "diameter": 200,
      "category": 6,
      "shape": 2,
      "azimuth": 0
    }
  ]
}

def getFromJsonToDic(jsonData):
    '''
    convert jsonData to Dictionary
    :param jsonData: json data from web
    :return: dictionary(dic pipe ,dic joint, dic hole(obstruction))
    '''
    dicPipelst = {}
    dictJointlst = {}
    lstPipe = []
    lstJoint = []
    lstobstruction = []
    dicResult = {}
    area = ''
    for key, value in jsonData.items():
      if key=="data":
        for i in range(len(value)):
          for key,value_ in value[i].items():
            if key=='type':
              if value_=='line':
                dicPipelst.setdefault('line',value)
                continue
              elif value=='cylinder':
                dictJointlst.set('Cylinder',value)
    return dicPipelst

inputfile = "G:\Data\python\Obj\pipe\pipe-8.0m.obj"
insertimage = "G:\Data\python\Obj\pipe\Low_pipe_8_0m_BaseColor.png"
inputWidth = 60
savepath = "G:\Data\python\Objwriter"
dicFileLocation={}

dic=getFromJsonToDic(json)
pipLst=dic.get('line')
for i in range(0,4):
  width=0
  height=0
  type=pipLst[i].get('type')
  geometry=pipLst[i].get('geometry')
  diameter=pipLst[i].get('diameter')
  category=pipLst[i].get('category')
  shape=pipLst[i].get('shape')
  azimuth=pipLst[i].get('azimuth')
  if category=='3':
    width=pipLst[i].get('width')
    height=pipLst[i].get('height')
  if type=='line':
    firstlon,firstlat=convertGeo4326To5186(geometry[0].get('lon'), geometry[0].get('lat'))
    nextlon, nextlon = convertGeo4326To5186(geometry[1].get('lon'), geometry[1].get('lat'))
    depth = geometry[0].get('depth')
    azimuth = geometry[0].get('gepth')
    newSize = math.sqrt((firstlon - nextlon) ** 2 + (firstlat - nextlon) ** 2) * 2
    newWidth = diameter
    saveFile = '20210601_pip' + str(0)
    jobid = 'shlee0601'

    outfile_0 = obj_editor.makePipeResize(savepath, inputfile, insertimage, inputWidth, newSize, newWidth, saveFile,jobid)
    obj_editor.rotationObj(outfile_0, [-90, 0, float(geometry[0].get('azimuth'))])
    dicFileLocation.setdefault("0",[outfile_0,0,0,depth])
    for j in range(1,8):
      lon,lat=convertGeo4326To5186(geometry[j].get('lon'), geometry[j].get('lat'))
      before_lon,before_lat=convertGeo4326To5186(geometry[j-1].get('lon'), geometry[j-1].get('lat'))
      print('lot lon :',lon, lat,"before :",before_lon,before_lat)
      depth=geometry[j].get('depth')
      azimuth=geometry[j].get('gepth')
      newSize = math.sqrt((lon - before_lon)**2+(lat-before_lat)**2)*2
      newWidth=diameter
      saveFile='20210531_pip'+str(j)
      print("newSize :",newSize,"newWidth :",newWidth)

      outfile=obj_editor.makePipeResize(savepath,inputfile,insertimage,inputWidth,newSize,newWidth,saveFile,jobid)
      obj_editor.rotationObj(outfile,[-90,0,float(geometry[j].get('azimuth'))])
      dicFileLocation.setdefault(str(j), [outfile, lon-firstlon, lat-firstlat,depth])

#
# l=[dicFileLocation.get(str(1))[1]-dicFileLocation.get(str(0))[1],dicFileLocation.get(str(1))[2]-dicFileLocation.get(str(0))[2],dicFileLocation.get(str(1))[3]]
# obj_editor.addObjFile(dicFileLocation.get(str(0))[0],dicFileLocation.get(str(1))[0],l)

obj_editor.addObjFile(dicFileLocation,savepath+"\lastFile.obj")
print(dicFileLocation)
for i in range(len(dicFileLocation)):
  file=dicFileLocation.get(str(i))[0]
  location=[dicFileLocation.get(str(i))[1]-dicFileLocation.get(str(0))[1],dicFileLocation.get(str(i))[2]-dicFileLocation.get(str(0))[2],dicFileLocation.get(str(i))[3]]
  print("filename :",file,"location :",location)
