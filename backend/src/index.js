const client = require('./request');

const [ arg ] = process.argv.slice(2);

(async () => {
  const http = await client.create();
  
  const search = encodeURIComponent(arg)
  const result = await http.get(`search?q=${search}&type=artist,track&limit=20`);

  result.tracks.items.forEach(item => console.log(item));
})();
