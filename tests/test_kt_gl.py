import pytest
from owslib.wms import WebMapService


@pytest.fixture(scope="module")
def wms_kt_gl():
    wms = WebMapService('https://wms.geo.gl.ch?SERVICE=WMS&Request=GetCapabilities',
                        version='1.3.0')
    yield wms


@pytest.mark.parametrize("layer_name,layer_title", [
    ("ch.gl.imagery.orthofoto2013", "Luftbild Orthofoto 2013"),
    ("ch.gl.imagery.orthofoto2015", "Digitales Terrainmodell 50cm, Relief"),
    ("ch.gl.imagery.orthofoto2017", "Digitales Terrainmodell 50cm, Relief"),
])
@pytest.mark.filterwarnings('ignore:.*Content metadata for layer*')
def test_layer(layer_name, layer_title, wms_kt_gl):
    assert layer_name in wms_kt_gl.contents
    assert wms_kt_gl[layer_name].title == layer_title
