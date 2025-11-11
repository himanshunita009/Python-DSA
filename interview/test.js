setImmediate(() => console.log("immediate"));
Promise.resolve(console.log("Himanshu"))
process.nextTick(() => console.log("nextTick"));
