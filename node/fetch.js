const axios = require('axios');
const fs = require('fs');

const url1 = 'http://localhost:3000/server1'; // Sostituisci con l'URL del server
const url2 = 'http://localhost:3000/server2';
axios.get(url1)
  .then(response => {
    const jsonData = response.data;
    file = fs.open('servers.json', 'a+', (err, f) => {
      if (err) {
        console.error(err);
      }
      fs.writeFileSync(f, '{');
      fs.writeFileSync(f, JSON.stringify(jsonData));
      return f;
    })
  });

axios.get(url2)
  .then(response => {
    const jsonData = response.data;
    file = fs.open('servers.json', 'a+', (err, f) => {
      if (err) {
        console.error(err);
      }
      fs.writeFileSync(f, JSON.stringify(jsonData))
      fs.writeFileSync(f, '}');
      return f
    })
  });
