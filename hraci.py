import cmd
import getpass

mena_hraci={}

def najdiHraca(name):
	for hrac in zoznam:
		if hrac.name==name:
			return hrac
	return False

class Hrac:
	
	junior=False
	
	def __init__(self,name,points):
		self.name=name
		self.points=int(points)

class ParseCommands(cmd.Cmd):
	
	def do_points(self,args):
		name,points=args.split()
		if name not in mena_hraci:
			mena_hraci[name]=Hrac(name,points)
			print('pridal som cloveka',name,'s',points,'bodmi')
		else:
			print('pridavam',points,'pre',name)
			mena_hraci[name].points+=int(points)
			print(name,'ma',mena_hraci[name].points,'bodov')
	
	def do_reduce(self,percent):
		percent=int(percent)/100
		for hrac in zoznam:
			hrac.points=int(hrac.points*(1-percent))
	
	def do_junior(self,name):
		mena_hraci[name].junior=True

	def do_ranking(self,args):
		zoznam=sorted(mena_hraci.values(),key=lambda hrac:hrac.points,reverse=True)
		for hrac in zoznam:
			if args=='junior': 
				if hrac.junior:
					print(hrac.name)
			else:print(hrac.name)	

	def do_quit(self,args):return True	

password=getpass.getpass(prompt='Vloz heslo, ktore budes pouzivat ')

ParseCommands().cmdloop()
