const fs = require('fs');
const nReadlines = require('n-readlines');

async function processLineByLine() {
    const broadBandLines = new nReadlines('UBCSWSActivities_TS.html');
    
    var line;

    while (line = broadBandLines.next()) {
        line = line.toString('ascii');
        if (line.includes("<p>") && !line.includes("Sat") && !line.includes("Sun")) {
            console.log(line.substring(26,29));

            line = broadBandLines.next().toString('ascii');

            while (!line.includes("<tr>")) {
                line = broadBandLines.next();
            }
            for (var i = 0; i < 5; i++) {
                line = broadBandLines.next();
            }
            console.log(broadBandLines.next().toString('ascii'));
            for (i = 0; i < 3; i++) {
                line = broadBandLines.next();
            }

            line = broadBandLines.next().toString('ascii');
            if (!line.includes("</tr>")) {
                console.log(line);
                console.log(broadBandLines.next().toString('ascii'));
            }
            
        }
        
    }
}

processLineByLine();