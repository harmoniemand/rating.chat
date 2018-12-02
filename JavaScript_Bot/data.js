module.exports = {
    //STAGE1 - Unterhaltung - Tag 0

    startmedia: {
        text: 'Du hast Feierabend und bist zu Hause. Da es etwas ruhig ist, möchtest du Musik hören. Wie machst du das?',
        next: [['video', 'Ich mache das Radio an'], ['restmusic', 'Ich öffne Spotify'], ['restmusic', 'Ich gehe zu youtube'], ['restmusic', 'Hey, Alexa...']]
    },

    video: {
        text: 'Nach der ganzen Musik möchtest du was gucken. Was tust du?',
        next: [['startdate', 'Ich schaue mir meine DVDs im Regal an.'], ['startdate', 'Netflix und Chill!'], ['startdate', 'Ab zu youtube'], ['startdate', 'Mal den Fernseher anschmeißen']]
    },
    restmusic: {
        text: 'Du entdeckst ein super cooles Lied...',
        next: [['video', 'Morgen auf der Arbeit zeige ich es Manfred'], ['video', 'Per Whatsapp mit Manni teilen'], ['video', 'Ab auf facebook damit']]
    },

    //STAGE1 - Unterhaltung - Tag 1
    startdate: {
        text: 'Da es so unterhaltsam ist schläfst du einfach ein...und schon klingelt der Wecker.\nGuten Morgen! Dein Handy erinnert dich: In zwei Tagen ist Datenight und du bist mit planen dran.',
        next: [['starttransport', 'Ganz klassisch ins Kino'], ['starttransport', 'Netflix und Chill!'], ['starttransport', 'Ein kleines Barkonzert steht an']]
    },


    starttransport: {
        text: 'Nachdem das geregelt ist, gehts ab zur Arbeit.',
        next: [['startpresent', 'Bloß nicht zu spät für die SBahn'], ['startpresent', 'Wo stand mein Auto noch gleich?'], ['startpresent', 'Fahrradhelm auf und los gehts']]
    },

    startpresent: {
        text: 'Auf der Arbeit ist es langweilig und du denkst über ein Geschenk für deinen Partner nach.',
        next: [['mannipresent', 'Frag ich mal Manni'], ['internetpresent', 'Das Internet weiß Rat'], ['amazonpresent', 'Direkt zu Amazon']]
    },

    mannipresent: {
        text: 'Manni hat keinen Bock auf dich und sagt du sollst weiter arbeiten. Hmmm, was jetzt?',
        next: [['internetpresent', 'Doch das Internet. Da sind sie wenigstens nett zu mir'], ['amazonpresent', 'Ich hab Amazon Prime!']]
    },

    internetpresent: {
        text: 'Du öffnest schnell deinen Browser...',
        next: [['engine', 'Chrome'], ['engine', 'Firefox'], ['engine', 'Internet Explorer'], ['engine', 'Safari']]
    },

    engine: {
        text: 'Und gehst zu...',
        next: [['research', 'Google'], ['research', 'bing'], ['research', 'Duckduckgo'], ['amazonpresent', 'Amazon :D']]
    },

    research: {
        text: 'Geschenkinspiration...',
        next: [
            ['adblock', 'Folgende Pinterests könnten dir gefallen', 'accounts.adblock.enabled', false, "read"],
            ['adblocker', 'Folgende Pinterests könnten dir gefallen', 'accounts.adblock.enabled', true, "read"],
            ['adblock', 'Spiegel Online: Die beliebtesten Geschenke der Deutschen', 'accounts.adblock.enabled', true, "read"],
            ['adblocker', 'Spiegel Online: Die beliebtesten Geschenke der Deutschen', 'accounts.adblock.enabled', true, "read"],
            ['adblock', 'Gutefrage.net hat gute Antworten'],
        ]
    },

    adblocker: {
        text: 'Ups, um das hier lesen zu können musst du deinen Adblocker deaktivieren...',
        next: [
            ['inspiration', 'Ja ok, weg damit', 'accounts.adblock.enabled', false, 'write'],
            ['alternative', 'Nee, da muss es Alternativen geben', 'accounts.adblock.enabled', true, 'write']
        ]
    },

    alternative: {
        text: 'Zurück auf Los, wo finde ich Geschenkideen?',
        next: [['internetretry', 'Doch nochmal das Internet'], ['endpresent', 'Ach nee komm, ich lasse es']]
    },

    internetretry: {
        text: 'Haha, auch hier Adblock.',
        next: [
            ['inspiration', 'Ok, jetzt kommts weg', 'accounts.adblock.enabled', false, 'write'],
            ['endpresent', 'Na dann gibts halt kein Geschenk', 'accounts.adblock.enabled', true, 'write']
        ]
    },

    inspiration: {
        text: 'Du findest großartige Inspiration und willst es gleich bestellen.',
        next: [['endpresent', 'Ab ins Geschäft nachher'], ['amazonpresent', 'Amazon']]
    },

    amazonpresent: {
        text: 'Das Geschenk ist im Warenkorb und nun zum checkout.',
        next: [['endpresent', 'Kreditkarte'], ['endpresent', 'paypal'], ['endpresent', 'Sofort Überweisung']]
    },

    endpresent: {
        text: 'Du gehst nochmal aufs Klo und machst dann Feierabend nach diesem anstrengenden Arbeitstag.',
        next: [['startschufa', 'Next']]
    }
};

/*
//Sonne runter und rauf bitte :)

//STAGE2 - Erste Auswirkungen - Tag 2

//Ab jetzt (STAGE2) kann, wenn der entsprechende Parameter groß genug ist, jederzeit der random_spam oder random_ads eingreifen. 
//Bei 'negative' sollte es dann zurück ins vorherige Event gehen.

random_spam
'I'm a Nigerian prince and need your help to save 9 mill $.If you can give me your bank account I will give you 30 %.Please contact me so we can start our business.'
[['posiive', 'Wow, das klingt gut!'], ['negative', 'Weg damit']]

random_ads
'5 heiße Singles in deiner Nähe, von denen deine Ärzte nicht wissen wollen, dass du sie kennst!'
        [['positive', 'Mmmmh mal kennen lernen'], ['negative', 'Jaja weg damit...']]

random_positive
'Warum fällst du auf diesen Spam herein??? Danke für deine Daten, hier ist die Waschmaschine.'
        ['nicetry', 'Noch eine Runde?']


//Über die GEZ Gebühren, die man gar nicht zahlen kann, kommt man zur Not in Stage 3 immer ins Schufa Szenario
schufa_startschufa
'Du hast einen Brief bekommen.'
        [['daytwo', 'Oh nee, Rundfunkgebühren Gebühren! Zahle ich...später.'], ['daytwo', 'G...E....ach weg damit']]

work_daytwo
'Du gehst wieder zur Arbeit und schaust in deine Mails.'
        [['random.spam', 'Oh, ein nigerianischer Prinz'], ['phishing', 'Hmm, was ist das denn?']]

work_phishing
'Das würde doch sehr gut zum Geschenk gestern passen! Woher wissen die das...'
        [['work_audio/work_shopping', 'Passt ja super, direkt mitgekauft'], ['work_audio/work_shopping', 'Nee, das reicht erstmal']]
//wenn media_startmedia Spotify oder youtube ist zu work_audio. Bei Alexa zu work_shopping.

work_audio
'Da die Kollegen zu laut Kuchen essen, brauchst du Musik zur Konzentration. Zurück in der Playlist von gestern siehst du noch ein paar weitere passende Musikvorschläge. Jetzt bist du endgültig abgelenkt und schreibst mit deinem Partner. Mmmh, du hast hier so schöne Bilder von dir...'
        [['fired', 'Sharing is caring'], ['sick', 'Doch nicht während der Arbeitszeit']]

//wenn media_startmedia Alexa war zu work_shopping. Bei Spotify oder youtube zu work_audio.
work_shopping
'Da die Kollegen zu laut Kuchen essen, kannst du dich nicht konzentrieren und du schaust mal bei Amazon vorbei. Oh, hier ist ja das Album von der Band gestern.'
        [['enddaytwo', 'Gleich bestellen'], ['enddaytwo', 'Brauche ich eigentlich nicht wirklich...']]

work_enddaytwo
'Auch der heutige Tag war relativ unspektakulär (mhh Spekulatius) und du freust dich aufs Date morgen.'
        [['startconcert/sick', 'Yay!],['startconcert / sick','Neudeutsch: Juhu!']]
//wenn date_startdate das Kino oder das Barkonzert ist concert_startconcert. Wenn date_startdate Netflix&Chill ist schufa_sick.

//STAGE3 - Fuck you :)

//wenn date_startdate das Kino oder das Barkonzert ist
concert_startconcert
'Bei eurem Date siehst du eine Gruppe, die ein Selfie macht.'
            [['sick', 'Haha, Deppen'], ['drugs', 'Yeaaaah Photobomb!!!']]

concert_drugs
'Stellt sich heraus, dass auf dem Event nicht nur du dabei warst, sondern auch ein unter Beobachtung stehender Drogendealer. Das SEK durchsucht jetzt deine Wohnung.'
            ['nicetry', 'Noch eine Runde?']


//wenn date_startdate Netflix&Chill ist oder keins der anderen Killerszenarien greift
schufa_sick
'Weil du spontan starke Zahnschmerzen bekommen hast, gehst du zum Arzt. Dieser stellt fest, dass du auf Grund deiner mangelnden Zahnhygiene eine aufwändige Zahnbehandlung brauchst, die die Kasse nicht übernimmmt.'
            [['positive', 'Gabs da nicht so nigerianische Prinzen...?'], ['nocredit', 'Schnell ein Kredit?']]

schufa_nocredit
'Tja, wer seine Rechnungen nicht zahlt hat natürlich auch eine geringe Kreditwürdigkeit. Kein Geld für dich!'
            ['nicetry', 'Noch eine Runde?']


work_fired
'Wer hätte geahnt, dass dein Partner alle Bilder in die Cloud synct. Mit den Nacktbildern nimmt dich jetzt erstmal keiner auf der Arbeit ernst, sorry ^^'
            ['nicetry', 'Noch eine Runde?']


fail_nicetry
'Im echten Leben gibt es auch keine zweite Chance für deine Daten.'
            ['startmedia', 'Ok ok verstanden...']
}

    */