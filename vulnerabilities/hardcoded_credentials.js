// Hardcoded Credentials
const mongoose = require('mongoose');

// VULNERABILITY: Hardcoded credentials in code
const mongoUri = 'mongodb://admin:P@ssw0rd123@mongodb.example.com:27017/myapp';

mongoose.connect(mongoUri, {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('MongoDB connection error:', err);
});

// AWS credentials hardcoded
const AWS = require('aws-sdk');
const s3 = new AWS.S3({
  accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
  secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
});

module.exports = { mongoUri, s3 };
