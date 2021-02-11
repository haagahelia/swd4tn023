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
    "90210": "BEVERLY HILLS"
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

    assert toimipaikat["KIVIJÄRVI"] == ["43800"]
    assert toimipaikat["SMARTPOST"] == ["65374"]
    assert toimipaikat["YLIOLHAVA"] == ["91150"]
