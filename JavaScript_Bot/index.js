const config = require('./config.json');
const Telegraf = require('telegraf');
const { Markup } = Telegraf;
const data = require('./data');

const bot = new Telegraf(config.botToken);

var db = { user: {}, settings: data };

bot.start((ctx) => {

    db.user[ctx.from.id] = {
        name: ctx.from.first_name,
        age_group: 0,
        origin: 0,
        sex: 0,
        place_of_residence: 0,
        accounts: [],
        parent: null,
        stage: 0,
        weapon: null,
    };

    var msg = 'Hallo ' + ctx.from.first_name + ",\n\n";
    msg += "wir wollen gerne ein Spiel mit dir spielen. Es wird um deine Entscheidungen gehen. Also wähle weise.\n\n";
    msg += "Und weil es gefährlich da draußen sein kann, wähle zuerst eine Waffe.";

    ctx.replyWithMarkdown(
        msg,
        Markup.inlineKeyboard([
            Markup.callbackButton('Schwert', 'start_game'),
            Markup.callbackButton('Messer', 'start_game'),
            Markup.callbackButton('Bummerang', 'start_game'),
            Markup.callbackButton('Banane', 'start_game'),
        ]).extra());
});


bot.action('start_game', (ctx) => {
    var user = db.user[ctx.from.id];
    user.weapon = ctx.match[0];

    return ctx.reply('Gute Wahl. Viel Erfolg auf deiner Reise. Wir sehen uns schon bald wieder.\n\n liebe Grüße,\ngandalf',
        Markup.inlineKeyboard([
            Markup.callbackButton('Los gehts', 'event_startmedia'),
        ]).extra()
    );
});


bot.action(/event_.*/, (ctx) => {
    var user = db.user[ctx.from.id];

    var setting = db.settings[ctx.match.toString().substring(6)];
    if (!setting)
        return;

    console.log(setting);
    console.log(ctx.from.id);
    console.log(ctx.match);

    var markup = [];
    setting.next.forEach(n => {
        if (n.lenght < 3 || n[5] == 'read') {
            markup.push(Markup.callbackButton(n[1], 'event_' + n[0]));
        }
    });

    return ctx.reply(setting.text,
        Markup.inlineKeyboard(markup).extra()
    );
});


bot.startPolling()