const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const cors = require('cors');

// Create main application
const mainApp = express();
mainApp.use(cookieParser());
mainApp.use(express.static(path.join(__dirname, 'public')));

// Create attacker application
const attackerApp = express();
attackerApp.use(cors());
attackerApp.use(express.static(path.join(__dirname, 'attacker')));

// Secret API - this is what we're trying to protect
mainApp.get('/api/secret', (req, res) => {
  // Check if user is authenticated
  if (req.cookies.authToken === 'secret-auth-token-123') {
    res.json({ secret: 'FLAG{p0st_m3ss4g3_vuln3r4b1l1ty_3xpl01t3d}' });
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
});

// Routes
mainApp.get('/', (req, res) => {
  // Set auth cookie when user visits main page
  res.cookie('authToken', 'secret-auth-token-123', { httpOnly: false });
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

mainApp.get('/dashboard', (req, res) => {
  if (req.cookies.authToken === 'secret-auth-token-123') {
    res.sendFile(path.join(__dirname, 'public', 'dashboard.html'));
  } else {
    res.redirect('/');
  }
});

// Start both servers
mainApp.listen(3000, () => {
  console.log('Main application running on http://localhost:3000');
});

attackerApp.listen(3001, () => {
  console.log('Attacker application running on http://localhost:3001');
});
