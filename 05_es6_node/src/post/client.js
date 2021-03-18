const fetch = require('node-fetch');
const NodeCache = require('node-cache');

const cache = new NodeCache({ stdTTL: 100, checkperiod: 120 });

async function loadJson() {
    let response = await fetch('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json');
    return await response.json();
}

async function loadCachedJson() {
    let cached = cache.get('postalJson');
    if (cached) {
        return cached;
    } else {
        let data = await loadJson();
        cache.set('postalJson', data);
        return data;
    }
}

async function getPostalDistrict(postalCode) {
    let data = await loadCachedJson();
    return data[postalCode.toUpperCase()] || null;
}

async function getPostalCodes(district) {
    let data = await loadCachedJson();
    return Object.entries(data)
        .filter(([code, name]) => name.toUpperCase() === district.toUpperCase())
        .map(([code, name]) => code);
}


module.exports = { getPostalDistrict, getPostalCodes };