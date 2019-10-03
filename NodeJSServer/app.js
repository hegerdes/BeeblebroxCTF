const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const session = require('express-session');
const cors = require('cors');
const mongoose = require('mongoose');
const jwtDecode = require('jwt-decode');
const errorHandler = require('errorhandler');
const createError = require('http-errors');
const cookieParser = require('cookie-parser');
const morgan = require('morgan');
const passport = require('passport');
const useragent = require('express-useragent');
const mariadb = require('mariadb')
// const winston = require('./config/winston');
const port = process.env.port || 8000;

//Configure Mongoose
mongoose.promise = global.Promise;
mongoose.set('debug', true);
mongoose.set('useCreateIndex', true);
mongoose
  .connect('mongodb://ctf:ConSecurMongoDB@localhost:27017/ctf', {
    useNewUrlParser: true,
    useUnifiedTopology: true
  })
  .catch(err => {
    console.error('No DB connection:', err.stack);
    process.exit(1);
  });

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log('MongoDB: we are connected!');
  mongoose.connection.on('error', err => {
    logError(err);
  });
});


var myconn = mariadb.createConnection({
  host: 'localhost',
  user: 'ctf10',
  connectionLimit: 500,
  password: 'ConSecurMariaDB',
  database: 'ctf10',
});


global.myconn = myconn;


const mypool = mariadb.createPool({
    host: 'localhost',
    user: 'ctf11',
    connectionLimit: 800,
    password: 'ConSecurMariaDB',
    database: 'ctf11',
  });
  
  mypool.getConnection()
    .then(conn =>{
      console.log('SQL Connected')
    })
    .catch(err =>{
      console.log(err)
      process.exit(1);
    })
//Share th global connection
global.mypool = mypool;

//Initiate our app
const app = express();

//Setup views
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

//Configure our app
app.use(morgan('dev'));
// app.use(morgan('combined', { stream: winston.stream }));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(useragent.express());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(
  session({
    secret: 'passport-tutorial',
    cookie: { maxAge: 60000 },
    resave: true,
    saveUninitialized: false,
  }),
);
app.use(passport.initialize());
app.use(passport.session());
app.use(cors());
app.use(require('morgan')('dev'));
app.use(express.static(path.join(__dirname, 'public')));

//Models
require('./models/Users');
require('./config/passport');

//Routes
const routes = require('./routes');
app.use(routes);

// catch 404 and forward to error handler
app.use((req, res, next) => {
  next(createError(404));
});

var user = 'non';
// error handler
app.use((err, req, res, next) => {
  var token = req.cookies.Auth;
  if (token) {
    var userinfo = jwtDecode(token);
    user = userinfo.email;
  }
  var permission = 'Permission dinied!';
  var advice =
    'This user has no permission to visit this site. Please log in with an account that has permission.';
  //auth error
  if (err.name === 'UnauthorizedError') {
    //No token
    if (err.message === 'No authorization token was found') {
      return res.render('err/unauthorized', {
        title: err.name,
        status: permission,
        message: err.message,
        users: user,
      });
    }
    //Wrong Token
    if (err.message === 'jwt malformed') {
      return res.render('err/unauthorized', {
        title: err.name,
        status: permission,
        message: advice,
        users: user,
      });
    } else
    return res.status(401).json({ error: err.name + ': ' + err.message });
  } else {
    // general err
    res.locals.message = err.message;
    res.locals.error =
      req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    return res.render('error', { title: err.name });
  }
});

//In Production use forever start app.js
// and remap port with: sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000
app.listen(port, () =>
  console.log('Server running on http://localhost:' + port),
);
