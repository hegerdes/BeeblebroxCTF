const mongoose = require('mongoose');
const passport = require('passport');
const LocalStrategy = require('passport-local');

const Users = mongoose.model('Users');

passport.use(
  new LocalStrategy(
    {
      usernameField: 'email',
      passwordField: 'password',
      session: true,
    },
    (username, password, done) => {
      Users.findOne({ email: username }, (err, user) => {
        if (err) {
          return done(err);
        }
        if (!user) {
          console.log('User err');
          return done(null, false, {
            message: 'Incorrect username.',
          });
        }
        console.log('Found user');
        if (!user.validatePassword(password)) {
          console.log('PW err');
          return done(null, false, {
            message: 'Incorrect password.',
          });
        }
        console.log('User and PW ok');
        return done(null, user);
      });
    },
  ),
);

passport.serializeUser(function(user, done) {
  done(null, user);
});

passport.deserializeUser(function(user, done) {
  done(null, user);
});
