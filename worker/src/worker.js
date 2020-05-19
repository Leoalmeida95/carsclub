const amqp = require('amqplib')
const nunjucks = require('nunjucks')
const sgMail = require('@sendgrid/mail')

require('dotenv').load()
const config = require('./config')
const { amqpUri, queue, sendgrid } = config
const { Register } = require('./models')
const assertQueueOptions = { durable: true }
const consumeQueueOptions = { noAck: false }

nunjucks.configure('.', { autoescape: true })
sgMail.setApiKey(sendgrid)

const generatedHtml = (body, name, context) => {
  return new Promise( (resolve, reject) => {
    const { url, app } = context

    try {
      const html = nunjucks.render(
        './src/register.html', { full_name: name, app: app, url: url }
      )
      const plain = nunjucks.renderString(body, {app: app, url: url })
      const result = {
        'html': html,
        'plain': plain
      }
      resolve(result)
    } catch (e) {
      reject(e)
    }
  })
}

const doWork = async (msg) => {
  const body = msg.content.toString()
  console.log(" [x] Received");
  const data = JSON.parse(body)

  // console.info(data.context)

  const { html, plain } = await generatedHtml(data.body, data.to, data.context)


  const email = new Register({
    app:data.app, from:data.from, to:data.to, subject:data.subject,
    body: plain, html: html, status: 'gen-html'
  })

  const emailMsg = {
    to: email.to, from: email.from, subject: email.subject, text: email.body,
    html: email.html, categories: 'register',
    headers: { 'X-Send-By': 'FireRabbit', 'X-Collection': 'register'},
    customArgs: { id: `${email.id}`, collection: 'register'}
  }

  // console.log(emailMsg)

  try {
    await sgMail.send(emailMsg)
    email.status = 'prepare'
    email.save()
  } catch (error) {
    // console.log(error)
    next(error);
  }

}

const assertAndConsumeQueue = (channel) => {
  const ackMsg = msg => Promise.resolve(doWork(msg))
  .then(() => channel.ack(msg))
  .catch(() => {
    channel.nack()
    channel.reject(msg, true)
  })

  return channel.assertQueue(queue, assertQueueOptions)
    .then(() => channel.prefetch(1))
    .then(() => channel.consume(queue, ackMsg, consumeQueueOptions));
}

const getQueueMessages = (
  () => amqp.connect(amqpUri).then(
    connection => connection.createChannel()
  ).then(
    channel => assertAndConsumeQueue(channel)
  ).catch(
    error => console.log(error)
  )
)

getQueueMessages()