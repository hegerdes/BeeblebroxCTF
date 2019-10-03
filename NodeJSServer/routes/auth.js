const jwt = require('express-jwt');
const jwtDecode = require('jwt-decode');

const getTokenFromHeadersGen = req => {
  console.log('Looking for Token in Header ...');
  var token = req.cookies.Auth;
  if (token) {
    console.log('Token: ' + token);
    return token;
  }
  console.log('Did not found Token');
  return null;
};

const getTokenFromHeadersSpecTask = req => {
  console.log('Looking for Token in Header ...');
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    var mytoken = String(userinfo.email);
    var myurl = String(req.url);
    myurl = myurl.substring(1, myurl.length);
    mytoken = mytoken.substring(3, mytoken.length);
    myurl = myurl.substring(3, myurl.length);
    var needt = parseInt(mytoken);
    var reqt = parseInt(myurl);

    if (needt >= reqt) {
      return token;
    } else return 'Wrong Token';
  }
  console.log('Did not found Token');
  return null;
};

const getTokenFromHeadersSpecSol = req => {
  console.log('Looking for Token in Header ...');
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    var mytoken = String(userinfo.email);
    var myurl = String(req.url);
    myurl = myurl.substring(1, myurl.length);
    mytoken = mytoken.substring(3, mytoken.length);
    myurl = myurl.substring(3, myurl.length);
    var needt = parseInt(mytoken);
    var reqt = parseInt(myurl);

    if (needt > reqt) {
      return token;
    } else return 'Wrong Token';
  }
  console.log('Did not found Token');
  return null;
};

const auth = {
  required: jwt({
    secret: 'secret',
    userProperty: 'payload',
    getToken: getTokenFromHeadersGen,
    failureRedirect: '/fail',
    failureFlash: false,
  }),
  specific_required: jwt({
    secret: 'secret',
    userProperty: 'payload',
    getToken: getTokenFromHeadersSpecTask,
    failureRedirect: '/fail',
    failureFlash: false,
  }),
  specific_requiredSol: jwt({
    secret: 'secret',
    userProperty: 'payload',
    getToken: getTokenFromHeadersSpecSol,
    failureRedirect: '/fail',
    failureFlash: false,
  }),
  optional: jwt({
    secret: 'secret',
    userProperty: 'payload',
    getToken: getTokenFromHeadersGen,
    credentialsRequired: false,
  }),
};

module.exports = auth;
