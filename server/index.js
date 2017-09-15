const robot = require('robotjs');

const net = require('net');

const badgeIP = '192.168.1.1';

const server = net.createServer((socket) => {
	socket.on('data', (action) => {
		console.log(action);

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
});

server.listen(1337, badgeIP);
