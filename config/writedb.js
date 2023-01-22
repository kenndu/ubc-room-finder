const fs = require('fs');
const readline = require('readline');
const { Client } = require('pg');
const { CLIENT_LONG_PASSWORD } = require('mysql/lib/protocol/constants/client');

const client = new Client({
    user: "postgres",
    password: "root",
    host: "localhost",
    port: 5432,
    database: "postgres"
});

client.connect();

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function processLineByLine() {
    const fileStream = fs.createReadStream('result.txt');
  
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });
    // Note: we use the crlfDelay option to recognize all instances of CR LF
    // ('\r\n') in input.txt as a single line break.
  
    for await (const line of rl) {
        // Each line in input.txt will be successively available here as `line`.
        // console.log(`${line}`);
        var arr = line.split(".");
        arr[1] = arr[1].toLowerCase();
        arr[2] = arr[2].replace("[", "{").replace("]", "}");
        console.log(arr);
        
        let query = 'SELECT COUNT(*) FROM schedule WHERE room = $1';
        let room = [arr[0]];

        // eslint-disable-next-line no-loop-func
        client.query(query, room, (err, res) => {
            if (!err) {
                if (res.rows[0]['count'] == 0) {
                    console.log(res.rows[0]['count']);
                    
                    let insertQuery = 'INSERT INTO schedule (room, ' + arr[1] + ') VALUES ($1, $2)';
                    let insertParams = [arr[0], arr[2]];
                    console.log(insertQuery);

                    client.query(insertQuery, insertParams, (err, res) => {
                        if (!err) {
                            console.log(res.rows);
                        } else {
                            console.error(err.message);
                        }
                    })

                } else {
                    let updateQuery = 'UPDATE schedule SET ' + arr[1] + ' = $1 WHERE room = $2';
                    let updateParams = [arr[2], arr[0]];

                    console.log("updateQuery: " + updateQuery);
                    client.query(updateQuery, updateParams, (err, res) => {
                        if (!err) {
                            console.log(res.rows);
                        } else {
                            console.error(err.message);
                        }
                    })
                }
            } else {
                console.log(err.message);
            }
        })

        await sleep(200)
    }

}

processLineByLine();
