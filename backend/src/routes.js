'use strict';

  module.exports = app => {
    const spotifyClient = require('./request');

    app.route('/search').post(async (req, res) => {
      const { body } = req;

      const args = encodeURIComponent(body.value);
      const limit = body?.limit ?? 20;

      const client = await spotifyClient.create();
      const response = await client.get(`search?q=${args}&type=artist,track,playlist&limit=${limit}`);

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(response));
    });
  }

