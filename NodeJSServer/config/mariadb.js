const mariadb = require('mariadb');

const dbconfig = {
  host: 'localhost',
  user: 'ctf9',
  connectionLimit: 5,
  password: 'ConSecurMariaDB',
  database: 'ctf9',
};

const poolPromise = mariadb.createPool(dbconfig)
  .getConnection()
  .then(pool => {
    console.log('Connected to MSSQL')
    return pool
  })
  .catch(err => console.log('Database Connection Failed! Bad Config: ', err))

module.exports = {
  mariadb, poolPromise
}