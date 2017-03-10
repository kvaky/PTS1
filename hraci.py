import cmd

zoznam=[]	

class Hrac:
	
	junior=False
	
	def __init__(self,name,points):
		self.name=name
		self.points=int(points)

class ParseCommands(cmd.Cmd):
	
	def do_points(self,args):
		name,points=args.split()
		found=False
		for hrac in zoznam:
			if hrac.name==name:
				hrac.points+=int(points)
				found=True
				print(hrac.name,hrac.points)
		if not found:
			zoznam.append(Hrac(name,points))
		
		
	
	def do_reduce(self,percent):
		percent=int(percent)/100
		for hrac in zoznam:
			hrac.points=int(hrac.points*(1-percent))


				 
	
	

password=input('Put your new password: ')

ParseCommands().cmdloop()

