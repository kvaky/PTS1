import cmd
import getpass

# slovnik hracov, kde key je meno a value je objekt hraca

mena_hraci = {}

def getpassword(command):
    '''Dekorator prikazov na ktore je potrebne heslo: vypyta si heslo, ak je 
    spravne, vykona prikaz, ak nie, vypise chybovu hlasku a skonci.
    
    Args:
      command: prikaz, ktory ma byt na heslo.
    '''

    def wrapper(self, args):
        if getpass.getpass() == password:
            return command(self, args)
        else:
            print ('Zadal si zle heslo')

    return wrapper


# Trieda reprezentujuca hraca dana atributmi name, points a junior

class Hrac:

    def __init__(self, name, points):
        self.name = name
        self.junior = False
        self.points = float(points)


# Trieda implementujuca komunikaciu s pouzivatelom

class ParseCommands(cmd.Cmd):

    intro = '\nNapis help pre dokumentaciu'
    prompt = '\ncakam prikaz: '

    # funkcie zacinajuce 'help' su dokumentujuce prikazy

    def help_points(self):
        print ('points <name> <number>\nPrida hracovi <name> <number> bodov '
            'a vypise o tom hlasku.\nCislo moze by aj zaporne.\nAk hrac <name> este'
            ' nie je evidovany, prida ho do zoznamu s <number> bodmi a vypise o tom'
            ' hlasku.')

    def help_junior(self):
        print ('junior <name>\nOznaci, ze hrac <name> je junior')

    def help_quit(self):
        print ('Vypne aplikaciu')

    def help_ranking(self):
        print ('ranking (Optional: <\'junior\'>)\nVypise cele poradie v tvare:'
            ' poradove cislo, meno, pocet bodov.\nHracov zoradime podla poctu'
            ' bodov.\nAk je zadany ako argument retazec \'junior\', vypise' 
            ' poradie medzi juniormi.')

    def help_reduce(self):
        print ('reduce <number>\nZnizi pocet bodov kazdeho hraca o'
            ' <number> %\nVysledok sa zaokrhli na cele cisla nadol.')

    @getpassword
    def do_points(self, args):
        '''Ak hrac nie je este evidovany v slovniku, tak ho evidujeme pod menom 
        name s points bodmi a oznamime to pouzivatelovi inak hracovi name 
        pridame points bodov a oznamime to pouzivatelovi
    
        Args:
          name: Meno hraca.
          points: Pocet bodov, ktore mu chceme pridat.
        '''
        (name, points) = args.split()
        if name not in mena_hraci:
            mena_hraci[name] = Hrac(name, points)
            print ('pridal som cloveka', name, 's', points, 'bodmi')
        else:
            print ('pridavam', points, 'pre', name)
            mena_hraci[name].points += float(points)
            print (name, 'ma', mena_hraci[name].points, 'bodov')


    @getpassword
    def do_reduce(self, percent):
        '''Prejde cez kazdeho hraca v slovniku a znizi jeho body o percent 
        percent a zaokruhli nadol
    
        Args:
          percent: O kolko percent znizit kazdemu hracovi body.
        '''
        percent = float(percent) / 100
        for hrac in mena_hraci.values():
            hrac.points = int(hrac.points * (1 - percent))

        # oznaci hraca name ako juniora

    @getpassword
    def do_junior(self, name):
        '''Oznaci hraca ako juniora
        
        Args:
          name: Meno hraca ktoreho chceme oznacit ako juniora
        '''
        mena_hraci[name].junior = True


    def do_ranking(self, args):
        '''Ak uzivatel zada ako argument junior, vypise poradove cislo, meno, 
        body hracov oznacenych ako junior inak vypise to iste pre vsetkych 
        hracov
        
        Args: 
          (Optional) 'junior': Ak je zadany argument konstanta 'junior', spravi
              ranking len pre hracov oznacenych junior.
        '''

        zoznam = sorted(mena_hraci.values(), key=lambda hrac: \
                        hrac.points, reverse=True)
        vypis = []
        if args == 'junior':
            for hrac in zoznam:
                if hrac.junior:
                    vypis.append(hrac)
        else:
            vypis = zoznam
        for i in range(0, len(vypis)):
            print (i + 1, vypis[i].name, vypis[i].points, 'bodov')

        # ukonci aplikaciu

    @getpassword
    def do_quit(self, args):
        '''Ukonci program
        '''
        return True


# vypyta si od uzivatela heslo ktore bude pouzivat bez toho aby ho zobrazovalo

password =getpass.getpass(prompt='\nVloz heslo, ktore budes pouzivat (je neviditelne) ')

# spusti komunikaciu s uzivatelom

ParseCommands().cmdloop()

