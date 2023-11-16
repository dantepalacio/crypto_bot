const { log, error } = require("console");
const { Client } = require("pg");

const connectionParams = {
    user: "postgres",
    host: "localhost",
    database: "postgres",
    password: "Qwertyu123451!",
    port: 5432
};

const client = new Client(connectionParams);

async function createTable() {
    try {
        await client.connect();

        const createTableQuery = `
            CREATE TABLE IF NOT EXISTS news (
                id serial PRIMARY KEY,
                crypto_name TEXT,
                title TEXT,
                content TEXT,
                url TEXT,
                time TEXT
            );
        `;

        await client.query(createTableQuery);
    } catch (error) {
        console.error("Ошибка при создании таблицы: ", error);
    } finally {
        await client.end();
    }
}

createTable();
