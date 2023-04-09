const baseUrl = "http://localhost:8000";

const urls = {
  "br-male": "/br-male",
  "br-male-complete": "/br-male-complete",
  "br-female": "/br-female",
  "br-female-complete": "/br-female-complete",
  "br-surname": "/br-surname",

  "en-male": "/en-male",
  "en-male-complete": "/en-male-complete",
  "en-female": "/en-female",
  "en-female-complete": "/en-female-complete",

  "fantasy-name": "/fantasy-name",
};


class Api {
  static async getBrName(quantity = 1) {
    const response = await fetch(`${baseUrl}${urls.brMale}/?quantity=${quantity}`);
    return await response.json();
  }

  static async getBrSurname() {

  }
  static async get(key, quantity = 1) {
    const response = await fetch(`${baseUrl}${urls[key]}/?quantity=${quantity}`);
    return await response.json();
  }
}

export default Api;