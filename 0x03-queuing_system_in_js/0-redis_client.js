import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.on('error', err => console.log('Redis client not connected to the server: Error_MESSAGE', err));

client.set('key', 'value', (err, reply) => {
if (err) {
	console.error('Error setting value:', err);
}else {
	console.log('Value set:', reply);

 client.get('key', (err, value) => {
	 if(err) {
	    console.error('Error getting value:', err);
	 }else {
		 console.log('Retrieved value:', value);
		 client.quit();
}
});
}
});
