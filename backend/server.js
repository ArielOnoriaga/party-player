'use strict';
require('dotenv').config();

const express = require('express');
const routes = require('./src/routes');
const spotifyClient = require('./src/request');

const app = express();
const port = process.env.PORT || 9090;

app.use(express.json());

routes(app);

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header('Access-Control-Allow-Methods', 'GET,POST');
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.listen(port, async () => {
  await spotifyClient.create();

  console.log(`listening on ${port}`);
});
