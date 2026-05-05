// Command Injection Vulnerability
const express = require('express');
const { exec } = require('child_process');

const app = express();

app.get('/ping', (req, res) => {
  const hostname = req.query.host;
  
  // VULNERABILITY: User input directly passed to exec without sanitization
  exec(`ping -c 4 ${hostname}`, (error, stdout, stderr) => {
    if (error) {
      res.status(400).send(`Error: ${error.message}`);
      return;
    }
    res.send(stdout);
  });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
