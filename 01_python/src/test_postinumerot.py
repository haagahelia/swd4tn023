import postinumerot

POSTINUMEROT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST",
    "90210": "BEVERLY HILLS",
    "74704": "SMARTPOST"
}


def test_ryhmittele_yksittainen_postinumero():
    toimipaikat = postinumerot.ryhmittele_toimipaikoittain(POSTINUMEROT)

    assert toimipaikat["JUUPAJOKI"] == ["35540"]


def test_ryhmittele_useita_postinumeroita():
    toimipaikat = postinumerot.ryhmittele_toimipaikoittain(POSTINUMEROT)

    assert toimipaikat["KIURUVESI"] == ["74701", "74700"]


def test_ryhmittely_tuottaa_oikean_maaran_ryhmia():
    toimipaikat = postinumerot.ryhmittele_toimipaikoittain(POSTINUMEROT)
    assert len(toimipaikat) == 3


def test_ryhmittele_toimipaikkojen_erikoistapaukset():
    toimipaikat = postinumerot.ryhmittele_toimipaikoittain(ERIKOISTAPAUKSET)

    assert "43800" in toimipaikat["KIVIJÄRVI"]
    assert "65374" in toimipaikat["SMARTPOST"]
    assert "91150" in toimipaikat["YLIOLHAVA"]


def test_ryhmittely_ei_huomioi_valimerkkeja_eika_kirjainkokoa():
    smart_postit = {
        "65374": "SMART POST",
        "74704": "SMARTPOST",
        "96204": "smart-post"
    }
    toimipaikat = postinumerot.ryhmittele_toimipaikoittain(smart_postit)

    assert toimipaikat["SMARTPOST"] == ["65374", "74704", "96204"]
