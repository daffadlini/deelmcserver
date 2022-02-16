const fs = require('fs');

const connectionString = process.env.DATABASE_URL;

const { Client } = require('pg');

const client = new Client({
  connectionString: connectionString,
  ssl: { rejectUnauthorized: false }
});

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }

var myData;

const retreiveQuery = `
select convert_from(file, 'UTF-8') as file from files where filename='world.zip'`;

client.connect();

client.query(retreiveQuery, (err, res, fields) => {
    if (err) {
        console.error(err);
        return;
	}
    
  console.log('fetched')

    let row = res.rows[0];
    myData = row.file
        main();

  client.end();
});

function main() {

  fs.writeFile('./world.zip', myData, 'hex', err => {
      if (err) {
          console.log('Error writing file', err)
      } else {
      console.log('saved')
      }            
  })

  sleep(2000);

  console.log('**script**: fetched world folder')

}


