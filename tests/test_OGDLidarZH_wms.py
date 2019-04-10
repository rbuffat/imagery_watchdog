import pytest
from owslib.wms import WebMapService

wms = WebMapService('https://wms.zh.ch/OGDOrthoZH?SERVICE=WMS&Request=GetCapabilities',
                    version='1.3.0')


@pytest.mark.parametrize("layer_name,layer_title", [
    ("ortho", "Orthofoto ZH Sommer 2018 RGB"),
    ("ortho_w_15", "Orthofoto ZH Frühjahr 2015/16 RGB"),
    ("ortho_s_14", "Orthofoto ZH Sommer 2014/15 RGB"),
])
def test_layer(layer_name, layer_title):
    assert layer_name in wms.contents
    assert wms[layer_name].title == layer_title