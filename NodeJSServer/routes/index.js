const express = require('express');
const mongoose = require('mongoose');
const passport = require('passport');
const jwtDecode = require('jwt-decode');
const levels = require('./tasks/level-router');
const solutions = require('./solutions/solutions-router');
const ctf = require('./ctf/ctf-router');
const auth = require('./auth');
const level_links = require('../config/links');

const router = express.Router();

router.use('/ctf', ctf);
router.use('/task', levels);
router.use('/solution', solutions);

const Users = mongoose.model('Users');

var user = 'non';

/* GET home page. */
router.get('/', auth.optional, (req, res, next) => {
  res.redirect('/task');
});

//Login GET
router.get('/login', auth.optional, (req, res, next) => {
  res.render('login', { title: 'Log in to CTF', users: user });
});

//Credits GET
router.get('/tipps', auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('tipps', { title: 'General Tipps', users: user, data: level_links });
});

//Credits GET
router.get('/credits', auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('credits', { title: 'Credits', users: user, data: level_links });
});

//About GET
router.get('/about', auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('about', { title: 'About', users: user, data: level_links });
});

//Login GET
router.get('/logedin', auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('logedin', { title: 'Logedin!', users: user });
});

//About GET
router.get(/\/example[0-9]$/, auth.optional, (req, res, next) => {
  var level_num = req.url.match(/\d+/)[0];
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('example', { title: 'Example ' + level_num, users: user, data: level_links, num: level_num });
});

// //Login GET
// router.get('/register', auth.optional, (req, res, next) => {
//   res.render('task/register', { title: 'Register for CTF' });
// });

// //Login POST
// router.post('/register', auth.optional, (req, res, next) => {
//   const user = req.body;

//   if (!user.email) {
//     return res.status(422).json({
//       errors: {
//         email: 'is required',
//       },
//     });
//   }
//   if (!user.password) {
//     return res.status(422).json({
//       errors: {
//         password: 'is required',
//       },
//     });
//   }

//   const finalUser = new Users(user);

//   finalUser.setPassword(user.password);
//   console.log('Saved: ' + finalUser);

//   return finalUser
//     .save()
//     .then(() => res.json({ user: finalUser.toAuthJSON() }));
// });

//POST login route (optional, everyone has access)
router.post('/login', auth.optional, (req, res, next) => {
  const user = req.body;
  console.log(user);

  if (!user.email) {
    return res.status(422).json({
      errors: {
        email: 'is required',
      },
    });
  }

  if (!user.password) {
    return res.status(422).json({
      errors: {
        password: 'is required',
      },
    });
  }

  return passport.authenticate(
    'local',
    { session: true },
    (err, passportUser, info) => {
      if (err) {
        return next(err);
      }

      if (passportUser) {
        console.log('Found user');
        const user = passportUser;
        user.token = passportUser.generateJWT();

        tokens = user.toAuthJSON().token;
        console.log('Token: ' + tokens);

        res.setHeader('Authorization', 'Bearer ' + tokens);
        res.token = tokens;
        res.cookie('Auth', tokens, {
          maxAge: 900000,
          httpOnly: true,
        });

        return res.redirect('logedin');
        //return res.json({ user: user.toAuthJSON() });
      }

      return res.render('err/unauthorized', {
        title: 'Login Faild',
        status: 'Invalid input!',
        message: 'Ether the username or passowrd is not corect.',
        users: 'non',
      });
    },
  )(req, res, next);
});

/* All other urls. */
router.get(/\/*/, auth.optional, (req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  res.render('err/not-found', {
    title: 'Page not found!',
    users: user,
  });
});

module.exports = router;
