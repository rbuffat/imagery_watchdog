import pytest
from owslib.wms import WebMapService

wms = WebMapService('https://wms.zh.ch/OGDLidarZH?SERVICE=WMS&Request=GetCapabilities',
                    version='1.3.0')


@pytest.mark.parametrize("layer_name,layer_title", [
    ("dtm2014hillshade", "Terrainschummerung"),
    ("dom2014hillshade", "Oberflächenschummerung")
])
def test_layer(layer_name, layer_title):
    assert layer_name in wms.contents
    assert wms[layer_name].title == layer_title