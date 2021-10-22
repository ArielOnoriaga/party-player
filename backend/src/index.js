require('dotenv').config();
const request = require('request-promise-native');
const credentials = Buffer.from(`${process.env.CLIENT_ID}:${process.env.CLIENT_SECRET}`).toString('base64');

const getData = async () => request({
    method: 'POST',
    uri: 'https://accounts.spotify.com/api/token',
    headers: {
      Authorization: `Basic ${credentials}`,
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'grant_type=client_credentials',
    json: true,
  });

const baseGet = (token) => async (point) => request({
    method: 'GET',
    uri: `${process.env.BASE_URL}/${point}`,
    headers: { Authorization: `Bearer ${token}` },
    json: true,
});

const [ arg ] = process.argv.slice(2);

(async () => {
  const access = await getData();
  const token = access.access_token;

  const requestGet = baseGet(token);

  const search = encodeURIComponent(arg)
  const result = await requestGet(`search?q=${search}&type=artist,track&limit=20`);

  result.tracks.items.forEach(item => console.log(item));
})();
