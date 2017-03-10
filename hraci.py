import cmd

zoznam={'fero': 4}	

class Hrac:
	
	junior=False
	
	def __init__(self,name,points):
		self.name=name
		self.points=points

class ParseCommands(cmd.Cmd):
	
	def do_points(self,args):
		name,points=args.split()
		zoznam[name]+=int(points)
		print(name,zoznam[name])
 
	
	

password=input('Put your new password: ')

ParseCommands().cmdloop()

