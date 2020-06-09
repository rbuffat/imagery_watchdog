import warnings

import pytest
from owslib.wms import WebMapService


@pytest.fixture(scope="module")
def wms_kt_so():
    wms = WebMapService('https://geo.so.ch/api/wms?ERVICE=WMS&Request=GetCapabilities',
                        version='1.3.0')
    yield wms


@pytest.mark.parametrize("layer_name,layer_title", [
    ("ch.so.agi.lidar_2014.dom_relief", "Relief digitales Oberflächenmodell (LiDAR 2014)"),
    ("ch.so.agi.lidar_2014.dtm_relief", "Relief digitales Terrainmodell 2014 (LiDAR 2014)")
])
@pytest.mark.filterwarnings('ignore:.*Content metadata for layer*')
def test_layer(layer_name, layer_title, wms_kt_so):
    assert layer_name in wms_kt_so.contents
    assert wms_kt_so[layer_name].title == layer_title
