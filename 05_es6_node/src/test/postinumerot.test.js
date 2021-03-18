const assert = require('assert');
const { getPostalDistrict, getPostalCodes } = require('../post/client');

describe('Get district name by postal code', function () {
    it('Gets Helsinki for 00100', async function () {
        let name = await getPostalDistrict('00100');

        assert.strictEqual(name, 'HELSINKI');
    });

    it('Gets Korvatunturi for 99999', async function () {
        let name = await getPostalDistrict('99999');

        assert.strictEqual(name, 'KORVATUNTURI');
    });

    it('Returns null when postal code is not found', async function () {
        let name = await getPostalDistrict('???');

        assert.strictEqual(name, null);
    });
});

describe('Get postal codes by district name', function () {
    it('Gets postal code for KORVATUNTURI', async function () {
        let codes = await getPostalCodes('KORVATUNTURI');

        assert.deepStrictEqual(codes, ['99999']);
    });

    it('Gets postal codes in case-insensitive  manner', async function () {
        let codes = await getPostalCodes('Kiuruvesi');

        assert.deepStrictEqual(codes, ["74700", "74701"]);
    });

    it('Returns empty array when no postal codes are found', async function () {
        let codes = await getPostalCodes('?????');

        assert.deepStrictEqual(codes, []);
    });
});
