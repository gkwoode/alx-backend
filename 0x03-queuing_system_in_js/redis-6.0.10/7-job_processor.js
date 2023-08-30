import kue from 'kue';

const queue = kue.createQueue({ concurrency: 2 });

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  // Track progress of the job
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job if phone number is blacklisted
    job.fail(new Error(`Phone number ${phoneNumber} is blacklisted`));
    done();
  } else {
    // Update progress and send notification
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
};

// Process jobs from the "push_notification_code_2" queue
queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Listen for queue "complete" event
queue.on('job complete', (id) => {
  kue.Job.get(id, (err, job) => {
    if (err) {
      console.error(`Error getting job ${id}: ${err}`);
    } else {
      console.log(`Job ${id} completed`);
    }
  });
});
