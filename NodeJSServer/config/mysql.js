'user strict';

var mysql = require('mysql');

//local mysql db connection
var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'ctf10',
    password : 'ConSecurMariaDB',
    database : 'ctf10'
});

connection.connect(function(err) {
    if (err) throw err;
});

module.exports = connection;