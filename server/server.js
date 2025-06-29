const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello from ShopSphere!');
});

app.listen(5000, '0.0.0.0', () => {
  console.log(`Server running on port 5000`);
});
