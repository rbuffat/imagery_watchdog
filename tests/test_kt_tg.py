import pytest
from owslib.wms import WebMapService


@pytest.fixture(scope="module")
def wms_kt_tg_basisplan():
    wms = WebMapService('https://ows.geo.tg.ch/geofy_access_proxy/basisplanf?SERVICE=WMS&Request=GetCapabilities',
                        version='1.3.0')
    yield wms


@pytest.fixture(scope="module")
def wms_kt_tg_radwege():
    wms = WebMapService('https://ows.geo.tg.ch/geofy_access_proxy/radwege?SERVICE=WMS&Request=GetCapabilities',
                        version='1.3.0')
    yield wms


@pytest.fixture(scope="module")
def wms_kt_tg_wanderwege():
    wms = WebMapService('https://ows.geo.tg.ch/geofy_access_proxy/wanderwege?SERVICE=WMS&Request=GetCapabilities',
                        version='1.3.0')
    yield wms


@pytest.fixture(scope="module")
def wms_kt_tg_dsm():
    wms = WebMapService('https://ows-raster.geo.tg.ch/geofy_access_proxy/reliefschattierung?SERVICE=WMS&Request=GetCapabilities',
                        version='1.3.0')
    yield wms


@pytest.fixture(scope="module")
def wms_kt_tg_ortho2017():
    wms = WebMapService('https://ows-raster.geo.tg.ch/geofy_access_proxy/orthofoto2017?SERVICE=WMS&Request=GetCapabilities',
                        version='1.3.0')
    yield wms


@pytest.mark.parametrize("layer_name,layer_title", [
    ("Basisplan_farbig", "Basisplan farbig"),
])
def test_layer(layer_name, layer_title, wms_kt_tg_basisplan):
    assert layer_name in wms_kt_tg_basisplan.contents
    assert wms_kt_tg_basisplan[layer_name].title == layer_title


@pytest.mark.parametrize("layer_name,layer_title", [
    ("Radwege", "Radwege"),
])
def test_layer(layer_name, layer_title, wms_kt_tg_radwege):
    assert layer_name in wms_kt_tg_radwege.contents
    assert wms_kt_tg_radwege[layer_name].title == layer_title


@pytest.mark.parametrize("layer_name,layer_title", [
    ("Wanderwege", "Wanderwege"),
])
def test_layer(layer_name, layer_title, wms_kt_tg_wanderwege):
    assert layer_name in wms_kt_tg_wanderwege.contents
    assert wms_kt_tg_wanderwege[layer_name].title == layer_title


@pytest.mark.parametrize("layer_name,layer_title", [
    ("DTMRelief", "Relief DTM"),
])
@pytest.mark.filterwarnings('ignore:.*Content metadata for layer*')
def test_layer(layer_name, layer_title, wms_kt_tg_dsm):
    assert layer_name in wms_kt_tg_dsm.contents
    assert wms_kt_tg_dsm[layer_name].title == layer_title


@pytest.mark.parametrize("layer_name,layer_title", [
    ("Orthofoto2017_RGB", "Orthofoto2017 RGB"),
])
def test_layer(layer_name, layer_title, wms_kt_tg_ortho2017):
    assert layer_name in wms_kt_tg_ortho2017.contents
    assert wms_kt_tg_ortho2017[layer_name].title == layer_title
