const puppeteer = require("puppeteer");
const fs = require("fs");

const readline = require("readline");

const cron = require("node-cron");
const { log, error } = require("console");

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// db
const { Client } = require("pg");
const { request } = require("http");

const connectionParams = {
    user: "postgres",
    host: "localhost",
    database: "postgres",
    password: "Qwertyu123451!",
    port: 5432
};

const client = new Client(connectionParams);


async function insertToDataBase(cryptoName, title, content, articleLink) {
    try {
        
        console.log("Вход в БД!");
        const checkQuery = "SELECT COUNT(*) FROM news WHERE URL = $1";
        const checkResult = await client.query(checkQuery, [articleLink]);
        
        if (checkResult.rows[0].count > 0) {
            console.log("Статья уже есть в БД");
        }
        else {
            const query = "INSERT INTO news (crypto_name, title, content, URL) VALUES ($1, $2, $3, $4)";
            const values = [cryptoName, title, content, articleLink];
            await client.query(query, values);           
            console.log("Данные успешно добавлены в БД!")
        }
        

    } catch (error) {
        console.log("Ошибка при загрузке данных в бд: ", error);
    }
}



async function parseAndInsertToDataBase(articleLink, cryptoName) {
    try {

        console.log("#");

        const browser = await puppeteer.launch({
            headless: "new"
        });
        const page = await browser.newPage();
        await page.goto(articleLink);

        console.log("Название криптовалюты: ", cryptoName);

        const title = await page.$eval("h1.sc-151230bb-0.cmIZAV", (element) => element.textContent);
        
        console.log("\n");
        console.log("Заголовок: ", title);

        const contentElements = await page.$$eval('p', (elements) => elements.map((element) => element.textContent));
        const content = contentElements.join("\n");

        console.log("Содержание: ", content);
        console.log("\n");
        
        await insertToDataBase(cryptoName, title, content, articleLink);
        
        await browser.close();
        

    } catch (ex) {
        console.error(`Не удалось получить доступ к статье: ${articleLink}`);
        console.error(`Ошибка: ${ex}`);
    }
}


// async function parseAndWriteToCsv(articleLink, csvWriter) {
//     console.log(articleLink);
//     try {
//         const browser = await puppeteer.launch({
//             headless: "new"
//         });
//         const page = await browser.newPage();
//         await page.goto(articleLink);

//         const title = await page.$eval("h1.huQzNi", (element) => element.textContent);

//         console.log("\n");
//         console.log("Заголовок: ", title);

//         const contentElements = await page.$$eval('p', (elements) => elements.map((element) => element.textContent));
//         const content = contentElements.join("\n");

//         console.log("Содержание: ", content);
//         console.log("\n");

//         csvWriter.write([title, content]);

//         await browser.close();

//     } catch (ex) {
//         console.error(`Не удалось получить доступ к статье: ${articleLink}`);
//         console.error(`Ошибка: ${ex}`);
//     }
// }

async function main() {
    try {
        const browser = await puppeteer.launch({
            headless: false
        });

        let page;
        // const page = await browser.newPage();

        r1.question("Введите название криптовалюты (без ошибок, на английском):\n", async (cryptoNameInput) => {
            cryptoNameInput = cryptoNameInput.charAt(0).toLowerCase() + cryptoNameInput.slice(1);
            
            page = await browser.newPage();
            await page.goto(`https://cryptorank.io/news/${cryptoNameInput}`);
            
            const articleLinks = new Set();
            const cryptoName = await page.$eval("span.sc-151230bb-0.sc-444b21a2-6.cmIZAV.iVSSqq", (element) => element.textContent);
            

            await client.connect();

            while (true) {
    
                const articleElements = await page.$$('div.sc-2cd471ac-3');
    
                for (const article of articleElements) {
                    const links = await article.$$eval('a', (elements) => elements.map((element) => element.href));
    
                    for (const link of links) {
                        if (link.startsWith("https://cryptorank.io/news/feed/")) {
                            if (!articleLinks.has(link)) {
                                articleLinks.add(link);
                                console.log(`Спарсено (кол-во) ссылок - ${articleLinks.size}`);
                                console.log(`Ссылка: ${link}`);
                            }
                        }
                    }
                }
    
                try {
                    const showMoreButton = await page.waitForSelector('button.sc-4ebbd3ae-1.YYMJ.sc-7947ae-3.dxRVKk', { timeout: 3000 });
                    await showMoreButton.click();
    
                } catch (error) {
                    console.error('Кнопка "Show more news" не найдена или не кликнута.');
                    console.error(`Ошибка: ${error}`);
                }
    
    
    
    
                await new Promise(page => setTimeout(page, 5000));
    
                const articleLinksSize = articleLinks.size;
    
                if (articleLinksSize >= 10) {
                    break;
                }
            }
    
    
    
            // await new Promise(page => setTimeout(page, 5000));
    
            // await page.evaluate(() => {
            //     window.scrollBy(0, document.body.scrollHeight - 1500);
            //     // window.scrollBy(0, window.innerHeight - 1500);
            // });
    
            // const currentArticleCount = articleLinks.size;
            // if (currentArticleCount === previousArticleCount || currentArticleCount >= 100) {
            //     break;
            // }


            // const csvFilePath = "C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\cryptonews_app\\parser\\crypto_news.csv";
            // const csvWriter = fs.createWriteStream(csvFilePath, { flags: 'w' });
            // csvWriter.write("Title;Content\n");
            
            for (const articleLink of articleLinks) {
                // await parseAndWriteToCsv(articleLink, csvWriter);
                // await page.waitForTimeout(Math.floor(Math.random() * 2000) + 3000);
                console.log("##");
                await parseAndInsertToDataBase(articleLink, cryptoName);
                await new Promise(page => setTimeout(page, Math.floor(Math.random() * 2000) + 3000));
            }
    
            await client.end();
            await browser.close();

        
            r1.close();
        });
        
        

    } catch (ex) {
        console.error('Не удалось получить доступ к главной странице новостей.');
        console.error(`Ошибка: ${ex}`);
    }
}

cron.schedule("15 * * * *", async () => {
    console.log("Запуск скрипта (1 круг)...")
    await new Promise(page => setTimeout(page, 5000));

    try {
        await main();
    } catch (error) {
        console.error("Ошибка выполнения скрипта: ", error);
    }
})

cron.schedule("30 * * * *", async () => {
    console.log("Запуск скрипта (2 круг)...")
    await new Promise(page => setTimeout(page, 5000));

    try {
        await main();
    } catch (error) {
        console.error("Ошибка выполнения скрипта: ", error);
    }
})