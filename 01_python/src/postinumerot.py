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


def main():
    postinumerot = http_pyynto.hae_postinumerot()

    toimipaikat = ryhmittele_toimipaikoittain(postinumerot)

    toimipaikka = input('Kirjoita postitoimipaikka: ')

    loydetyt = etsi_postinumerot(toimipaikka, toimipaikat)

    if loydetyt:
        loydetyt = sorted(loydetyt)
        print('Postinumerot: ' + ', '.join(loydetyt))
    else:
        print('Toimipaikkaa ei löytynyt')


if __name__ == '__main__':
    main()
