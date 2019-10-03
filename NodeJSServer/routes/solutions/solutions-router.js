const express = require('express');
const router = express.Router();
const auth = require('../auth');
const jsonfile = require('jsonfile');
const jwtDecode = require('jwt-decode');
const level_links = require('../../config/links');

var user = 'non';

/* GET home page. */
router.get('/', auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('solutions/solution-index', {
    title: 'Beeblebrox CTF',
    data: level_links,
    users: user,
  });
});

/*Get the levels. PW requierd */
router.get(
  /\/ctf(1?[0-9])|20$/,
  auth.specific_requiredSol,
  (req, res, next) => {
    var token = req.cookies.Auth;
    if (token) {
      var userinfo = jwtDecode(token);
      user = userinfo.email;
    }
    var str = __dirname;
    var file = str.substring(0, str.length - 16);
    var level_num = req.url.match(/\d+/)[0];

    file = file + 'data/LevelInfo.json';
    jsonfile.readFile(file, (err, levelinfo) => {
      if (err) {
        console.error(err);
        res.status(err.status || 500);
        res.render('error');
      } else {
        res.render('solutions/gen-level-sol', {
          title: "Solution Level " + level_num,
          data: level_links,
          users: user,
          num: level_num
        });
      }
    });
  },
);
module.exports = router;
