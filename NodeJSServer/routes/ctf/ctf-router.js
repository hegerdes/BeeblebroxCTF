const express = require('express');
const router = express.Router();
const auth = require('../auth');
const jsonfile = require('jsonfile');
const jwtDecode = require('jwt-decode');
const mariadb = require('mariadb');
const level_links = require('../../config/links');

var user = 'non';

/*Level 6 */
router.get('/ctf6', auth.specific_required, (req, res, next) => {
  res.render('ctf/level_06', { title: 'Level 6' });
});

/*Level 7 */
router.get('/ctf7', auth.specific_required, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  var logedin = req.cookies.LogedIn;
  if (logedin || user === 'ctf8') {
    if (logedin == 1 || user === 'ctf8') {
      res.render('ctf/level_07', {
        title: 'Level 7',
        allowed: true,
        users: user,
      });
    } else {
      res.render('ctf/level_07', {
        title: 'Level 7',
        allowed: false,
        users: user,
      });
    }
  } else {
    res.cookie('LogedIn', 0, { maxAge: 900000, httpOnly: true });
    res.render('ctf/level_07', {
      title: 'Level 7',
      allowed: false,
      users: user,
    });
  }
});

/*Level 8 */
router.get('/ctf8', auth.specific_required, (req, res, next) => {
  var allowed =
    req.useragent.isiPad ||
    req.useragent.isiPod ||
    req.useragent.isSafari ||
    req.useragent.isiPhone;

  res.render('ctf/level_08', { title: 'Level 8  ', iphone: allowed });
});

/*Level 9 */
router.get('/ctf9', auth.specific_required, (req, res, next) => {
  res.render('ctf/level_09', { title: 'Level 9 Task ', logedin: false, wrong: false });
});

/*Level 9 */
router.post('/ctf9', auth.specific_required, (req, res, next) => {
  var userinput = req.body.text;

  if(userinput === '4242'){
    return res.render('ctf/level_09', { title: 'Level 9 Task ', logedin: true, wrong: false });
  }
  else{
    return res.render('ctf/level_09', { title: 'Level 9 Task ', logedin: false, wrong: true });
  }
  
});

/*Level 10 */
router.get('/ctf10', auth.specific_required, (req, res, next) => {
  res.render('ctf/level_10', { title: 'Level 10 Task ' });
});

/*Level 10 */
router.post('/ctf10', auth.specific_required, (req, res, next) => {
  var rows = [];
  var userinput = req.body.text;
  var query =
    'SELECT user from Data WHERE user LIKE "' + userinput + '" ';
  if (userinput.includes(';')) {
    var tmp = userinput.split(';');
    query = tmp[1];
  }
  if (
    userinput.match(/\d=\d/g) ||
    userinput.match(/or\strue/i) ||
    userinput.includes(' or 1 ') ||
    userinput.includes(' or True')
  ) {
    var query = 'SELECT user from Data WHERE user LIKE "%" ';
  }

  const pool = mariadb.createPool({
    host: 'localhost',
    user: 'ctf10',
    connectionLimit: 5,
    password: 'ConSecurMariaDB',
    database: 'ctf10',
  });

  async function dbcall(callback) {
    let conn;
    try {
      conn = await pool.getConnection();
      rows = await conn.query(query);

      callback(rows);
    } catch (err) {
      console.log(err);
      return res.render('ctf/level_10-result', {
        title:
          'Internal error. No DB connection or invalid query. Please ty agian.',
        out: rows,
      });
    } finally {
      if (conn) return conn.end();
    }
  }

  dbcall(function(rows) {
    return res.render('ctf/level_10-result', {
      title: 'Level 10  Task',
      out: rows,
      uin: userinput,
    });
  });
});

/*Level 11 */
router.get('/ctf11', auth.specific_required, (req, res, next) => {
  res.render('ctf/level_11', { title: 'Level 11 Task ' });
});

/*Level 11 */
router.post('/ctf11', auth.specific_required, (req, res, next) => {
  var userinput = req.body.text;
  var query =
    'SELECT * from ctf11.Data WHERE user LIKE "' + userinput + '"';

  var stati = false;

  mypool.query(query)
  .then(rows => {
    if (rows.length < 1) {
      stati = false;
    } else {
      stati = true;
    }
    return res
      .render('ctf/level_11-result', {
        title: 'Level 11  Task',
        out: rows,
        uin: stati,
      })
  // .catch(err => {
  //   console.error('No DB connection:', err.stack);
  //   console.log('Try reconnect');
  //   const mytmppool = mariadb.createPool({
  //     host: 'localhost',
  //     user: 'ctf11',
  //     connectionLimit: 500,
  //     password: 'ConSecurMariaDB',
  //     database: 'ctf11',
  //   });
  //   mytmppool
  //     .getConnection()
  //     .then(conn => {
  //       console.log('SQL connected agian');
  //       global.mypool = mytmppool;
  //     })
  //     .catch(err => {
  //       console.log(err);
  //       process.exit(1);
  //     });
  // });
});

  // mypool.getConnection()
  // .then(conn => {
  //   conn.query(query)
  //   .then(rows =>{
  //     if(rows.length < 1){
  //       stati = false
  //     }else{
  //       stati = true
  //     }
  //     console.log(stati)
  //     return res.render('ctf/level_11-result', {
  //       title: 'Level 11  Task',
  //       out: rows,
  //       uin: stati,
  //     });
  //   })
  // })
});

module.exports = router;
