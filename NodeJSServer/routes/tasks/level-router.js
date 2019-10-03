const express = require('express');
const router = express.Router();
const auth = require('../auth');
const jwtDecode = require('jwt-decode');
const jsonfile = require('jsonfile');
const level_links = require('../../config/links');

var user = 'non';

/* GET home page. */
router.get('/', auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('task/task-index', {
    title: 'Beeblebrox CTF',
    data: level_links,
    users: user,
  });
});

/*Get the levels. 16-19 */
/*Cahnge the 6 to 7 if you added a level */
router.get(/\/ctf1[6-9]$/, auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('task/win', {
    title: 'Win',
    data: level_links,
    users: user,
  });
});

/*Get the levels. 0-19 */
router.get(/\/ctf1?[0-9]$/, auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  var str = __dirname;
  var file = str.substring(0, str.length - 12);
  var level_num = req.url.match(/\d+/)[0];
  file = file + 'data/LevelInfo.json';
  jsonfile.readFile(file, (err, levelinfo) => {
    if (err) {
      console.error(err);
      res.status(err.status || 500);
      res.render('error');
    } else {
      res.render('task/gen_level_disc', {
        title: levelinfo.levels[level_num].name,
        data: level_links,
        discription: levelinfo.levels[level_num].discription,
        tipp: levelinfo.levels[level_num].tipps,
        commands: levelinfo.levels[level_num].tools,
        link: levelinfo.levels[level_num].link,
        users: user,
      });
    }
  });
});

/*Get the levels. PW requierd */
router.get('/ctf20', auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('task/win', {
    title: 'Win',
    data: level_links,
    users: user,
  });
});
module.exports = router;
