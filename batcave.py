class Places:
    def __init__(self, description):
        self.description = description
        self.heroes = []
        self.direction = {"sever": None,
                          "východ": None,
                          "jih": None,
                          "západ": None}

    def umisti(self, sever, vychod, jih, zapad):
        self.direction["sever"] = sever
        self.direction["východ"] = vychod
        self.direction["jih"] = jih
        self.direction["západ"] = zapad

    def pridej_hrdinu(self, hrdina):
        self.heroes.append(hrdina)

    def odeber_hrdinu(self, hrdina):
        self.heroes.remove(hrdina)

    def konverzace(self, hrdina):
        if len(self.heroes) > 1:
            print(f"{hrdina.name} se snaží konverzovat s ostatními hrdiny:")
            for p_hero in self.heroes:
                if p_hero.id != hrdina.id:
                    print(f"{hrdina.name}: Ahoj, {p_hero.name}! Jak se máš?")
                    print(f"{p_hero.name}: Jsem v pořádku, {hrdina.name}. Co ty?")

class Hero:
    pocet_bytosti = 0

    def __init__(self, name, race, place, job, health, questions):
        self.name = name
        self.race = race
        self.job = job
        self.health = health
        Hero.pocet_bytosti += 1
        self.id = Hero.pocet_bytosti
        self.place = place
        place.pridej_hrdinu(self)
        self.questions = questions

    def kde_jsi(self):
        print(self.place.description)
        if len(self.place.heroes) > 1:
            print("vidím tyto postavy: ", end="")
            for p_hero in self.place.heroes:
                if p_hero.id != self.id:
                    print(f"({p_hero.id}) {p_hero.race} - {p_hero.job}")
        print("*****************************")

    def jdi_na(self, smer):
        if self.place.direction[smer] is not None:
            self.place.odeber_hrdinu(self)
            self.place = self.place.direction[smer]
            self.place.pridej_hrdinu(self)

    def vyber_otazku(self):
        print(f"{self.name}, vyberte si otázku, kterou chcete položit:")
        for index, question in enumerate(self.questions.keys(), start=1):
            print(f"{index}. {question}")
        
        choice = int(input("Zadejte číslo otázky: ")) - 1
        question = list(self.questions.keys())[choice]
        answer = self.questions[question]
        print(f"{self.name}: {question}")
        print(f"{self.name}: {answer}")

# Místa
wayne_tower = Places("Wayne Tower, největší budova Gothamu - sídlo firmy Wayne Enterprises.")
batcave = Places("Batcave, tajná základna Batmana (utajená).")
gotham_streets = Places("Ulice Gothamu, temné a nebezpečné.")
arkham_asylum = Places("Arkham Asylum, blázinec pro superzločince.")
gotham_park = Places("Park v Gothamu, místo klidu a odpočinku, může být i zrádný.")

# Setting directions
wayne_tower.umisti(None, gotham_streets, None, None)
batcave.umisti(None, gotham_streets, None, None)
gotham_streets.umisti(batcave, gotham_park, None, wayne_tower)
arkham_asylum.umisti(None, None, None, gotham_streets)
gotham_park.umisti(gotham_streets, None, None, None)

# Creating heroes with their own question dictionaries
batman_questions = {
    "Jaký je tvůj plán na dnešek?": "Budu chránit Gotham.",
    "Máš nějaké nové gadgety?": "Ano, mám několik nových překvapení pro zločince."
}

robin_questions = {
    "Jak se máš, Robine?": "Mám se dobře, Batmane!",
    "Co plánuješ dneska?": "Chci se podívat po městě s tebou."
}

alfred_questions = {
    "Jak se máš, Alfrede?": "Jsem v pořádku, pane Bruce.",
    "Můžete mi připravit nějaké jídlo?": "Samozřejmě, pane."
}

gordon_questions = {
    "Jak to jde, komisaři?": "Mám plné ruce práce s vyšetřováním.",
    "Můžete mi poskytnout nějaké informace?": "Určitě, co potřebujete vědět?"
}

bruce_wayne_questions = {
    "Jak se ti daří, Bruce?": "Daří se mi skvěle, díky.",
    "Máš nějaké nové podnikatelské plány?": "Ano, plánujeme expanze na nové trhy."
}


batman = Hero("Batman", "Člověk", batcave, "tajemná osoba", 300, batman_questions)
robin = Hero("Robin", "Člověk", gotham_streets, "pobočník", 200, robin_questions)
alfred = Hero("Alfred Pennyworth", "Člověk", wayne_tower, "komorník", 225, alfred_questions)
gordon = Hero("komisař Gordon", "Člověk", gotham_streets, "detektiv", 250, gordon_questions)
bruce_wayne = Hero("Bruce Wayne", "Člověk", wayne_tower, "podnikatel", 175, bruce_wayne_questions)


batman.kde_jsi()
batman.jdi_na("východ")
batman.kde_jsi()
batman.place.konverzace(batman)

# Bruce Wayne se nemůže potkat s Batmanem
bruce_wayne.kde_jsi()


hero_choice = input("Vyberte hrdinu pro konverzaci (Batman, Robin, Alfred, Gordon, Bruce): ")
if hero_choice.lower() == "batman":
    batman.vyber_otazku()
elif hero_choice.lower() == "robin":
    robin.vyber_otazku()
elif hero_choice.lower() == "alfred":
    alfred.vyber_otazku()
elif hero_choice.lower() == "gordon":
    gordon.vyber_otazku()
elif hero_choice.lower() == "bruce":
    bruce_wayne.vyber_otazku()
else:
    print("Neplatná volba.")