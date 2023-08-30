import kue from 'kue';

const queue = kue.createQueue();

// Function to create push notification jobs
const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (err) {
          console.error(`Error creating job: ${err}`);
        } else {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    // Listen for job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Listen for job failure
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // Listen for job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
};

// Example array of jobs
const jobsArray = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  // ... (other job objects)
];

// Calling the function to create jobs
createPushNotificationsJobs(jobsArray, queue);
