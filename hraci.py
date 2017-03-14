import cmd
import getpass

#slovnik hracov, kde key je meno a value je objekt hraca
mena_hraci={}

#dekorator commandov na ktore je potrebne heslo: vypyta si heslo, ak je spravne, vykona
#prikaz, ak nie, vypise chybovu hlasku a skonci
def getpassword(command):
	def wrapper(self,args):
		if getpass.getpass()==password:
			return command(self,args)
		else:
			print('Zadal si zle heslo')
	return wrapper

#Trieda reprezentujuca hraca dana atributmi name, points a junior
class Hrac:
	
	junior=False
	
	def __init__(self,name,points):
		self.name=name
		self.points=int(points)

#Trieda implementujuca komunikaciu s pouzivatelom
class ParseCommands(cmd.Cmd):
	intro= '\nNapis help pre dokumentaciu'
	prompt= '\ncakam prikaz: '
	
	#funkcie zacinajuce 'help' su dokumentujuce prikazy	
	def help_points(self):
		print( '''points <name> <number>
  Prida hracovi <name> <number> bodov a vypise o tom hlasku. Cislo moze by aj zaporne.
  Ak hrac <name> este nie je evidovany, prida ho do zoznamu s <number> bodmi a vypise o tom
  hlasku.''')

	def help_junior(self):
		print('''\njunior <name>
  Oznaci, ze hrac <name> je junior''')

	def help_quit(self):
		print('\nvypne aplikaciu')

	def help_ranking(self):
		print('''\nranking (optional: <'junior'>)
  Vypise cele poradie v tvare: poradove cislo, meno, pocet bodov. Hracov zoradime podla poctu bodov.
  Ak date ako argument retazec 'junior', vypise poradie medzi juniormi''')

	def help_reduce(self):
		print('''\nreduce <number>
  Znizi pocet bodov kazdeho hraca o <number>%. Vysledok sa zaokrhli na cele cisla nadol.''')

	#ak hrac nie je este evidovany v slovniku, tak ho evidujeme pod menom name s points 
	#bodmi a oznamime to pouzivatelovi
	#inak hracovi name pridame points bodov a oznamime to pouzivatelovi	
	@getpassword
	def do_points(self,args):
		name,points=args.split()
		if name not in mena_hraci:
			mena_hraci[name]=Hrac(name,points)
			print('\npridal som cloveka',name,'s',points,'bodmi')
		else:
			print('\npridavam',points,'pre',name)
			mena_hraci[name].points+=int(points)
			print(name,'ma',mena_hraci[name].points,'bodov')

	#prejde cez kazdeho hraca v slovniku a znizi jeho body o percent percent a zaokruhli 
	#nadol	
	@getpassword
	def do_reduce(self,percent):
		percent=int(percent)/100
		for hrac in mena_hraci.values():
			hrac.points=int(hrac.points*(1-percent))
	
	#oznaci hraca name ako juniora
	@getpassword
	def do_junior(self,name):
		mena_hraci[name].junior=True

	#ak uzivatel zada ako argument junior, vypise poradove cislo, meno, body hracov
	#oznacenych ako junior
	#inak vypise to iste pre vsetkych hracov
	def do_ranking(self,args):
		zoznam=sorted(mena_hraci.values(),key=lambda hrac:hrac.points,reverse=True)
		vypis=[]
		if args=='junior':
			for hrac in zoznam:
				if hrac.junior:
					vypis.append(hrac)
		else:
			vypis=zoznam
		for i in range(0,len(vypis)):
			print('\n',i+1,vypis[i].name,vypis[i].points,'bodov')			
			
	#ukonci aplikaciu		
	@getpassword
	def do_quit(self,args):return True

#vypyta si od uzivatela heslo ktore bude pouzivat bez toho aby ho zobrazovalo
password=getpass.getpass(prompt='\nVloz heslo, ktore budes pouzivat (je neviditelne) ')

#spusti komunikaciu s uzivatelom
ParseCommands().cmdloop()
