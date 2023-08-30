import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: '+233200273290',
  message: 'Hello from Kue!',
};

// Create a job in the "push_notification_code" queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error(`Error creating job: ${err}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
