import pytest
import postinumerot

POSTINUMEROT = {
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "74701": "KIURUVESI",
    "73460": "MUURUVESI"
}

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "65374": "SMART POST",
    "74704": "SMARTPOST",
    "90210": "BEVERLY HILLS",
    "91150": "YLI-OLHAVA",
    "96204": "smart-post"
}


@pytest.fixture
def ryhmitelty():
    # Katso: https://docs.pytest.org/en/stable/fixture.html
    kaikki = {**POSTINUMEROT, **ERIKOISTAPAUKSET}
    return postinumerot.ryhmittele_toimipaikoittain(kaikki)


def test_ryhmittele_yksittainen_postinumero(ryhmitelty):
    assert ryhmitelty["JUUPAJOKI"] == ["35540"]


def test_ryhmittele_useita_postinumeroita(ryhmitelty):
    assert ryhmitelty["KIURUVESI"] == ["74700", "74701"]


def test_ryhmittele_toimipaikkojen_erikoistapaukset(ryhmitelty):
    assert "43800" in ryhmitelty["KIVIJÄRVI"]
    assert "65374" in ryhmitelty["SMARTPOST"]
    assert "91150" in ryhmitelty["YLIOLHAVA"]


def test_ryhmittely_ei_huomioi_valimerkkeja_eika_kirjainkokoa(ryhmitelty):
    assert ryhmitelty["SMARTPOST"] == ["65374", "74704", "96204"]


def test_etsi_postinumero_toimii_kirjainkoosta_riippumatta(ryhmitelty):
    numerot = postinumerot.etsi_postinumerot('Kivijärvi', ryhmitelty)

    assert numerot == ["43800"]


def test_etsi_smart_post_eri_kirjoitsasuilla(ryhmitelty):
    SMARTPOST = postinumerot.etsi_postinumerot('SMARTPOST', ryhmitelty)
    smartpost = postinumerot.etsi_postinumerot('smartpost', ryhmitelty)
    smart_post = postinumerot.etsi_postinumerot('SMART POST', ryhmitelty)

    assert SMARTPOST == smartpost == smart_post == ["65374", "74704", "96204"]
