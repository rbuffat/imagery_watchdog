import pytest
from owslib.wms import WebMapService
import requests

headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 6.0; Imagery Watchdog CI check)'}


@pytest.fixture(scope="module")
def wms_kt_zh_ogdlidar():
    url = 'https://wms.zh.ch/OGDLidarZH?SERVICE=WMS&Request=GetCapabilities'
    try:
        wms = WebMapService(url, version='1.3.0', headers=headers)
        yield wms
    except:
        print(requests.get(url, headers=headers).text)
        yield None


@pytest.fixture(scope="module")
def wms_kt_zh_ortho():
    url = 'https://wms.zh.ch/OGDOrthoZH?SERVICE=WMS&Request=GetCapabilities'
    try:
        wms = WebMapService(url, version='1.3.0')
        yield wms
    except:
        print(requests.get(url).text)
        yield None


@pytest.mark.parametrize("layer_name,layer_title", [
    ("dtm2014hillshade", "Terrainschummerung"),
    ("dom2014hillshade", "Oberflächenschummerung"),
])
def test_layer_lidar(layer_name, layer_title, wms_kt_zh_ogdlidar):
    assert layer_name in wms_kt_zh_ogdlidar.contents
    assert wms_kt_zh_ogdlidar[layer_name].title == layer_title


@pytest.mark.parametrize("layer_name,layer_title", [
    ("ortho", "Orthofoto ZH Sommer 2018 RGB"),
    ("ortho_w_15", "Orthofoto ZH Frühjahr 2015/16 RGB"),
    ("ortho_s_14", "Orthofoto ZH Sommer 2014/15 RGB"),
])
def test_layer_ortho(layer_name, layer_title, wms_kt_zh_ortho):
    assert layer_name in wms_kt_zh_ortho.contents
    assert wms_kt_zh_ortho[layer_name].title == layer_title
