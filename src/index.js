const express = require("express");
const app = express();
const cors = require("cors");
const pool = require('./db.js');

app.use(cors());
app.use(express.json());

//Fetch all rooms that are free in the current time interval
app.post("/", async (req, res) => {
    try {
        // console.log(req.body);
        const { room } = req.body;
        
    } catch (err) {
        console.error(err.message);
    }
})

app.listen(5000, () => {
    console.log("Server started on port 5000");
})