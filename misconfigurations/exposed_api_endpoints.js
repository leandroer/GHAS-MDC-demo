// Exposed Dangerous API Endpoints
const express = require('express');
const app = express();

// VULNERABILITY: Admin endpoint with no authentication
app.post('/admin/delete-user/:userId', (req, res) => {
  const userId = req.params.userId;
  // No authentication check - anyone can call this
  database.deleteUser(userId);
  res.json({ message: 'User deleted' });
});

// VULNERABILITY: Sensitive operation without rate limiting
app.post('/reset-password', (req, res) => {
  const email = req.body.email;
  // No rate limiting - allows brute force attacks
  sendPasswordResetEmail(email);
  res.json({ message: 'Reset link sent' });
});

// VULNERABILITY: Debug endpoint left in production
app.get('/debug/users', (req, res) => {
  // Should not be exposed - returns all user data
  res.json(database.getAllUsers());
});

app.listen(3000);
