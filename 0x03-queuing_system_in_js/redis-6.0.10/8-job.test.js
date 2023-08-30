import kue from 'kue';
import { createPushNotificationsJobs } from './8-job'; // Import the function to be tested

// Create a Kue queue in test mode
const queue = kue.createQueue({ testMode: true });

describe('createPushNotificationsJobs', () => {
  // Clear the queue before each test
  beforeEach(() => {
    queue.testMode.clear();
  });

  // Exit test mode after all tests
  afterAll(() => {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).toThrowError('Jobs is not an array');
  });

  it('should create jobs in the queue and handle events', () => {
    const jobsArray = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      // ... (other job objects)
    ];

    createPushNotificationsJobs(jobsArray, queue);

    // Assert the number of jobs in the queue
    expect(queue.testMode.jobs.length).toBe(jobsArray.length);

    // Loop through each job and test events
    jobsArray.forEach((jobData, index) => {
      const job = queue.testMode.jobs[index];

      // Validate job properties
      expect(job.type).toBe('push_notification_code_3');
      expect(job.data).toEqual(jobData);

      // Simulate job completion
      job.complete();

      // Assert completion event
      expect(job._state).toBe('complete');
    });
  });
});
