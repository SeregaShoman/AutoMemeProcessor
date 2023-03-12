class Standarts:
    GREETINGS = "GREETINGS"
    ENDING = "ENDING"
    ANOTHER = "ANOTHER"
    DOTA = "DOTA"
    TARKOW = "TARKOW"
    BADWORDS = "BADWORDS"

train_x = [
    "привет", "приветос", "здарова", "хей",
    "ку", "здравствуйте", "приветик", "привямба",
    "приветствую", "утро", "день", "вечер",
    "хеллоу", "приветики", "здравствуй",
    
    "пока", "покедова", "досвидос", "свидания",
    "прощай", "спокойной", "ночи", "пака",
    "до",

    "компендиум", "пудж", "турбо", "ммр",
    "дота", "дока", "плюс", "+", "рейтинг",
    "катка", "каточку", "скатаем", "мажор",
    "интернешнал",

    "буянов", "стрелять", "завод",

    "блять", "пиздец", "выблядок", "выблядки",
    "уебки", "твари", "пидорасы", "гондоны",
    "суки", "говно", "пизда", "хуй", "хуила",
    "хуек", "хуево", "секс"

    "сахар", "вода", "кушать", "покушать",
    "еда", "да", "нет", "вот", "бы",
    "машина", "купить", "ну", "я",
    "сыграл", "думаю", "мы", "ты",
    "тож", "яб", "голос", "подай",
    "принеси", "спрайт", "кола",
    "ну","как","норм","о",
    "иногда","одним","на",
]

train_y = [
    Standarts.GREETINGS,Standarts.GREETINGS,Standarts.GREETINGS,Standarts.GREETINGS,
    Standarts.GREETINGS,Standarts.GREETINGS,Standarts.GREETINGS,Standarts.GREETINGS,
    Standarts.GREETINGS,Standarts.GREETINGS,Standarts.GREETINGS,Standarts.GREETINGS,
    Standarts.GREETINGS,Standarts.GREETINGS,Standarts.GREETINGS,

    Standarts.ENDING,Standarts.ENDING,Standarts.ENDING,Standarts.ENDING,
    Standarts.ENDING,Standarts.ENDING,Standarts.ENDING,Standarts.ENDING,
    Standarts.ENDING,

    Standarts.DOTA, Standarts.DOTA,Standarts.DOTA,Standarts.DOTA,
    Standarts.DOTA,Standarts.DOTA,Standarts.DOTA,Standarts.DOTA,Standarts.DOTA,
    Standarts.DOTA,Standarts.DOTA,Standarts.DOTA,Standarts.DOTA,
    Standarts.DOTA,

    Standarts.TARKOW,Standarts.TARKOW,Standarts.TARKOW,

    Standarts.BADWORDS,Standarts.BADWORDS,Standarts.BADWORDS,Standarts.BADWORDS,
    Standarts.BADWORDS,Standarts.BADWORDS,Standarts.BADWORDS,Standarts.BADWORDS,
    Standarts.BADWORDS,Standarts.BADWORDS,Standarts.BADWORDS,Standarts.BADWORDS,Standarts.BADWORDS,
    Standarts.BADWORDS,Standarts.BADWORDS,Standarts.BADWORDS,

    Standarts.ANOTHER, Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,
    Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,
    Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,
    Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,
    Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,
    Standarts.ANOTHER,Standarts.ANOTHER,
    Standarts.ANOTHER, Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,
    Standarts.ANOTHER,Standarts.ANOTHER,Standarts.ANOTHER,

]