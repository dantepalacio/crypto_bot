const TelegramBot = require("node-telegram-bot-api");
require("dotenv").config();
const token_bot = process.env.TELEGRAM_BOT_TOKEN;

console.log(token_bot)

const web_url = "https://yandex.kz";
const bot = new TelegramBot(token_bot, {polling: true});



bot.on("message", async (msg) => {
    const chatID = msg.chat.id;
    const text = msg.text;

    if (text === "/start") {
        await bot.sendMessage(chatID, "Ниже появится кнопка, для заполнения формы", {
            reply_markup: {
                // keyboard: [
                //     [{text: "Заполни форму"}]
                // ]
                inline_keyboard: [
                    [{text: "Сделать заказ", web_app: {url: web_url}}]
                ]
            }
        })
    }

    bot.sendMessage(chatID, "Received your message");
})