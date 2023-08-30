import redis from "redis";

const client = redis.createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (error) => {
  console.log("Redis client not connected to the server: " + error);
});

function createHash() {
  client.hset("HolbertonSchools", "Portland", 50, (err, res) => {
    if (err) {
      console.log(err);
    } else {
      redis.print("Set Portland to 50 in HolbertonSchools hash");
    }
  });

  client.hset("HolbertonSchools", "Seattle", 80, (err, res) => {
    if (err) {
      console.log(err);
    } else {
      redis.print("Set Seattle to 80 in HolbertonSchools hash");
    }
  });

  client.hset("HolbertonSchools", "New York", 20, (err, res) => {
    if (err) {
      console.log(err);
    } else {
      redis.print("Set New York to 20 in HolbertonSchools hash");
    }
  });

  client.hset("HolbertonSchools", "Bogota", 20, (err, res) => {
    if (err) {
      console.log(err);
    } else {
      redis.print("Set Bogota to 20 in HolbertonSchools hash");
    }
  });

  client.hset("HolbertonSchools", "Cali", 40, (err, res) => {
    if (err) {
      console.log(err);
    } else {
      redis.print("Set Cali to 40 in HolbertonSchools hash");
    }
  });

  client.hset("HolbertonSchools", "Paris", 2, (err, res) => {
    if (err) {
      console.log(err);
    } else {
      redis.print("Set Paris to 2 in HolbertonSchools hash");
    }
  });
}

function displayHash() {
  client.hgetall("HolbertonSchools", (err, res) => {
    if (err) {
      console.log(err);
    } else {
      console.log("The HolbertonSchools hash contains:");
      console.log(res);
    }
  });
}

createHash();
displayHash();
