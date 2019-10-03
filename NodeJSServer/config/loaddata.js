const jsonfile = require('jsonfile');

exports.loadData = function() {
  const file = 'data/LevelInfo.json';
  jsonfile.readFile(file, (err, levelinfo) => {
    if (err) console.error(err);
    //console.dir(levelinfo.levels[0])
    //TODO pass to Router
    return levelinfo;
  });
};
