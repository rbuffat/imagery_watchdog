import pytest
from owslib.wms import WebMapService

wms = WebMapService('https://geo.so.ch/api/wms?ERVICE=WMS&Request=GetCapabilities',
                    version='1.3.0')


@pytest.mark.parametrize("layer_name,layer_title", [
    ("ch.so.agi.lidar_2014.dom_relief", "Relief digitales Oberflächenmodell (LiDAR 2014)"),
    ("ch.so.agi.lidar_2014.dtm_relief", "Relief digitales Terrainmodell 2014 (LiDAR 2014)")
])
def test_layer(layer_name, layer_title):
    assert layer_name in wms.contents
    assert wms[layer_name].title == layer_title
