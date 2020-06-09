import pytest
from owslib.wms import WebMapService


@pytest.fixture(scope="module")
def wms_kt_be():
    wms = WebMapService('https://www.geoservice.apps.be.ch/geoservice2/services/a42geo/a42geo_hoehenwms_d_fk/MapServer/WMSServer?SERVICE=WMS&Request=GetCapabilities',
                        version='1.3.0')
    yield wms


@pytest.mark.parametrize("layer_name,layer_title", [
    ("GEODB.LDOM50CM_LORELIEF", "Digitales Oberflaechenmodell 50cm, Relief"),
    ("GEODB.LDTM50CM_LTRELIEF", "Digitales Terrainmodell 50cm, Relief"),
])
def test_layer(layer_name, layer_title, wms_kt_be):
    assert layer_name in wms_kt_be.contents
    assert wms_kt_be[layer_name].title == layer_title
