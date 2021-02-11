import http_pyynto


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        nimi = normalisoi_nimi(nimi)
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat


def normalisoi_nimi(nimi):
    return nimi.upper().strip().replace(' ', '').replace('-', '')


def etsi_postinumerot(nimi, toimipaikat_dict):
    normalisoitu = normalisoi_nimi(nimi)
    return toimipaikat_dict.get(normalisoitu, [])


def etsi_samankaltaiset(nimi, toimipaikat_dict):
    normalisoitu = normalisoi_nimi(nimi)
    muunnokset = luo_muunnokset(normalisoitu)
    postinumerot = []
    for hakusana in muunnokset:
        postinumerot += etsi_postinumerot(hakusana, toimipaikat_dict)
    return postinumerot


def luo_muunnokset(termi):
    """
    Luo kaikki muunnokset, jossa kaksi peräkkäistä kirjainta on vaihtunut keskenään
    """
    muunnokset = {termi}  # set-tietorakenne ei salli duplikaatteja!
    for i in range(0, len(termi) - 2):
        muunnos = vaihda_paikkaa(termi, i, i+1)
        muunnokset.add(muunnos)
    return muunnokset


def vaihda_paikkaa(merkkijono, i, j):
    kirjaimet = list(merkkijono)
    kirjaimet[i], kirjaimet[j] = kirjaimet[j], kirjaimet[i]
    return ''.join(kirjaimet)


def main():
    postinumerot = http_pyynto.hae_postinumerot()

    toimipaikat = ryhmittele_toimipaikoittain(postinumerot)

    toimipaikka = input('Kirjoita postitoimipaikka: ')

    loydetyt = etsi_samankaltaiset(toimipaikka, toimipaikat)

    if loydetyt:
        loydetyt = sorted(loydetyt)
        print('Postinumerot: ' + ', '.join(loydetyt))
    else:
        print('Toimipaikkaa ei löytynyt')


if __name__ == '__main__':
    main()
