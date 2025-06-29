const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello from ShopSphere!');
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
});

