const express = require('express');
const app = express();
const port = 3000;

const server1 = {
    'nome': 'Server 1',
    'ip': '10.108.66.33',
}

const server2 = {
    'nome': 'Server 2',
    'ip': '10.108.66.15',
}

app.get('/server1', (req, res) => {
    res.json(server1);
});

app.get('/server2', (req, res) => {
    res.json(server2);
})


app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
  