//Get the needed stuff
const mongoose = require('mongoose');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');

//Schema for DB
const { Schema } = mongoose;

//Datamodel for user
const UsersSchema = new Schema({
  email: { type: String },
  hash: { type: String },
  salt: { type: String },
  message: { type: String, default: 'No Message' },
});

/*Additional methods*/

//Set password
UsersSchema.methods.setPassword = function(password) {
  this.salt = crypto.randomBytes(16).toString('hex');
  this.hash = crypto
    .pbkdf2Sync(password, this.salt, 10000, 512, 'sha512')
    .toString('hex');
};

//Check password
UsersSchema.methods.validatePassword = function(password) {
  const hash = crypto
    .pbkdf2Sync(password, this.salt, 10000, 512, 'sha512')
    .toString('hex');
  return this.hash === hash;
};

//Get the webtoken
UsersSchema.methods.generateJWT = function() {
  const today = new Date();
  const expirationDate = new Date(today);
  expirationDate.setDate(today.getDate() + 60);

  return jwt.sign(
    {
      email: this.email,
      id: this._id,
      exp: parseInt(expirationDate.getTime() / 1000, 10),
    },
    'secret',
  );
};

//To JSON
UsersSchema.methods.toAuthJSON = function() {
  return {
    _id: this._id,
    email: this.email,
    token: this.generateJWT(),
    message: this.message,
  };
};

//Compile model
Users = mongoose.model('Users', UsersSchema);

//Export it
module.exports;
