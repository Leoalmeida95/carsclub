require('dotenv').load()

const rabbitConfig = {
    amqpUri: process.env.AMQP_URI || 'amqp://user:password@server-name/my-vhost',
    mongoUri: process.env.MONGODB_URI || 'mongodb://localhost:27017',
    queue: process.env.QUEUE || 'your-queue-signup',
    sendgrid: process.env.SENDGRID_API_KEY
  }
  
  module.exports = rabbitConfig