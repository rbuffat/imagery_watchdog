import pytest
from owslib.wms import WebMapService

wms = WebMapService('https://geoweb.so.ch/wms/wms_lidar?SERVICE=WMS&Request=GetCapabilities',
                    version='1.3.0')


@pytest.mark.parametrize("layer_name,layer_title", [
    ("dom_relief2014_50cm", "DOM Relief 2014 - Auflösung 50cm"),
    ("dtm_relief2014_50cm", "DTM Relief 2014 - Auflösung 50cm")
])
def test_layer(layer_name, layer_title):
    assert layer_name in wms.contents
    assert wms[layer_name].title == layer_title