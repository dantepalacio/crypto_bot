const puppeteer = require("puppeteer");
const fs = require("fs");
const { log, error } = require("console");

// db
const { Client } = require("pg");

const connectionParams = {
    user: "postgres",
    host: "localhost",
    database: "postgres",
    password: "Qwertyu123451!",
    port: 5432
};


// client.connect()
//     .then(() => {
//         console.log("DB Connected!");
// })
//     .catch(error => {
//         console.log(`Error: ${error}`);
// })
//     .finally(() => {
//         client.end();
// });


const client = new Client(connectionParams);


async function insertToDataBase(title, content) {
    try {
        console.log("Вход в базу данных...");

        // await client.connect();
        const query = "INSERT INTO news (title, content) VALUES ($1, $2)";
        const values = [title, content];
        await client.query(query, values);

    } catch (error) {
        console.log("Ошибка при загрузке данных в бд: ", error);
    }
}



async function parseAndInsertToDataBase(articleLink) {
    try {
        const browser = await puppeteer.launch({
            headless: "new"
        });
        const page = await browser.newPage();
        await page.goto(articleLink);

        const title = await page.$eval("h1.huQzNi", (element) => element.textContent);

        console.log("\n");
        console.log("Заголовок: ", title);

        const contentElements = await page.$$eval('p', (elements) => elements.map((element) => element.textContent));
        const content = contentElements.join("\n");

        console.log("Содержание: ", content);
        console.log("\n");
        
        await insertToDataBase(title, content);
        
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
            headless: "new"
        });
        const page = await browser.newPage();
        await page.goto('https://cryptorank.io/news/bitcoin');

        const articleLinks = new Set();

        await client.connect();
        // while (true) {
        //     // const newLinksFound = false;
        //     const articleElements = await page.$$('div.sc-2cd471ac-3');

        //     for (const article of articleElements) {
        //         const links = await article.$$eval('a', (elements) => elements.map((element) => element.href));

        //         for (const link of links) {
        //             if (link.startsWith("https://cryptorank.io/news/feed/")) {
        //                 if (!articleLinks.has(link)) {
        //                     articleLinks.add(link);
        //                     console.log(`Спарсено (кол-во) ссылок - ${articleLinks.size}`);
        //                     console.log(`Ссылка: ${link}`);
        //                 }
        //             }
        //         }
        //     }





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
            // if (currentArticleCount >= 30) {
            //     // console.log("Статьи закончились!");
            //     break;
            // }
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
        const csvFilePath = "C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\cryptonews_app\\parser\\crypto_news.csv";
        const csvWriter = fs.createWriteStream(csvFilePath, { flags: 'w' });
        csvWriter.write("Title;Content\n");

        for (const articleLink of articleLinks) {
            // await parseAndWriteToCsv(articleLink, csvWriter);
            // await page.waitForTimeout(Math.floor(Math.random() * 2000) + 3000);

            await parseAndInsertToDataBase(articleLink);
            await new Promise(page => setTimeout(page, Math.floor(Math.random() * 2000) + 3000));
        }

        await client.end();
        await browser.close();



    } catch (ex) {
        console.error('Не удалось получить доступ к главной странице новостей.');
        console.error(`Ошибка: ${ex}`);
    }
}

main()