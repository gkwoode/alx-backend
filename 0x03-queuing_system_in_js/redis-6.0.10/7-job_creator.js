import kue from 'kue';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: "4153518780",
    message: "This is the code 1234 to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153518743",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4153538781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153118782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4153718781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4159518782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4158718781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153818782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4154318781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4151218782",
    message: "This is the code 4321 to verify your account",
  },
];

for (const job of jobs) {
  queue.create(job, (err, job) => {
    if (err) {
      console.log("Error creating job: " + err);
    } else {
      console.log("Notification job created: " + job.id);
    }
  });
}

queue.on("job_completed", (job) => {
  console.log("Notification job " + job.id + " completed");
});

queue.on("job_failed", (job, error) => {
  console.log("Notification job " + job.id + " failed: " + error);
});

queue.on("job_progress", (job, progress) => {
  console.log("Notification job " + job.id + " " + progress + "% complete");
});
