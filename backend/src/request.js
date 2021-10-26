require('dotenv').config();

const request = require('request-promise-native');
const credentials = Buffer.from(`${process.env.CLIENT_ID}:${process.env.CLIENT_SECRET}`).toString('base64');

class HttpClient {
  #tokenData;
  #base = 'https://api.spotify.com/v1';

  constructor(tokenData) {
    this.#tokenData = tokenData;
  }

  static async create() {
    const token = await request({
      method: 'POST',
      uri: 'https://accounts.spotify.com/api/token',
      headers: {
        Authorization: `Basic ${credentials}`,
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: 'grant_type=client_credentials',
      json: true,
    });

    return new this(token);
  }

  get token() {
    return this.#tokenData.access_token;
  }

  async get(endpoint) {
    return request({
      method: 'GET',
      uri: `${this.#base}/${endpoint}`,
      headers: { Authorization: `Bearer ${this.token}` },
      json: true
    });
  }
}

module.exports = HttpClient;
