const config = require('./config')
const Mongoose = require('mongoose')
const db = Mongoose.connect("mongodb://localhost:27017/api-users", {
  useNewUrlParser: true, 
  useUnifiedTopology: true
}).connection

const status = [
  'gen-html', 'prepare',
  'processed', 'dropped', 'delivered', 'deferred', 'bounce', 'open', 'click',
  'spam-report', 'unsubscribe', 'group-unsubscribe', 'group-resubscribe'
]

const Event = new Mongoose.Schema({
  status: {type: String, enum: status},
  email: {type: String, required: true, trim: true},
  timestamp: {type: Number, required: true, trim: true},
  smtp_id: {type: String, trim: true},
  sg_event_id: {type: String, required: true, trim: true},
  sg_message_id: {type: String, required: true, trim: true},
  ip: {type: String, trim: true},
  created: {type: Date, default: Date.now}
})

const Email = new Mongoose.Schema({
  app: {type: String, required: true, trim: true},
  from: { type: String, required: true, trim: true},
  to: { type: String, required: true, trim: true},
  subject: { type: String, required: true, trim: true},
  body: { type: String, required: true, trim: true},
  html: { type: String},
  status: {type: String, enum: status},
  events: [Event]
},
{
  timestamps: true
})

module.exports = {
  db,
  Register: Mongoose.model('registers', Email)
}