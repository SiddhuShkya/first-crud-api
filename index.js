
const { createApp } = require("./src/app.js");

const app = createApp();
const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log(`Server running at ${port}`)
})