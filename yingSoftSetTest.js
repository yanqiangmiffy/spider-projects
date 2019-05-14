//CBC模式解密
var CryptoJS = require('./crypto-js');

function aesDecrypt(message) {
    var keyHex = CryptoJS.enc.Utf8.parse("5QTtRO3vQMaYnPajQqc4d7eaF6BNS2dG");
    var ivHex = CryptoJS.enc.Utf8.parse("5QTtRO3vQMaYnPajQqc4d7eaF6BNS2dG");
    var decrypted = CryptoJS.DES.decrypt({
        ciphertext: CryptoJS.enc.Hex.parse(message)
    }, keyHex, {
        iv: ivHex,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return decrypted.toString(CryptoJS.enc.Utf8);
}