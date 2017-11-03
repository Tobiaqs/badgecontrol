const robot = require('robotjs');

const net = require('net');

let client = new net.Socket();
client.connect(1337, '192.168.1.104', () => {
	console.log('connected to badge!');
});

client.on('data', (buffer) => {
	const action = buffer.toString();
	if (action === 'left' || action === 'up' || action === 'right' || action === 'down') {
		robot.keyTap(action);
	} else if (action === 'A') {
		robot.keyTap('enter');
	} else if (action === 'B') {
		console.log('B');
	} else if (action === 'SELECT') {
		console.log('SELECT');
	}
});

client.on('close', () => {
	console.log('socket closed');
});

