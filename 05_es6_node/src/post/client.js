const fetch = require('node-fetch');

async function loadJson() {
    let response = await fetch('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json');
    return await response.json();
}

async function getPostalDistrict(postalCode) {
    let data = await loadJson();
    return data[postalCode.toUpperCase()] || null;
}

async function getPostalCodes(district) {
    let data = await loadJson();
    return Object.entries(data)
        .filter(([code, name]) => name.toUpperCase() === district.toUpperCase())
        .map(([code, name]) => code);
}


module.exports = { getPostalDistrict, getPostalCodes };