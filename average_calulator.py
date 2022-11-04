import csv
import os
from collections import OrderedDict
# For the average
from statistics import mean 
def fillcsv():
	Students=OrderedDict()
	studentcounter=1
	studentcount=int(input('tedad danesh amoz ra vared konid? :'))
	if(studentcount>=1):
		while(studentcounter<=studentcount):
			studentAverage=(input('name va nomarat ra vared konid(ex:nima 10 12 14 16....):')).strip().split()
			if(len(studentAverage)>2):
				Students[studentAverage[0]]=studentAverage[1:]
				studentcounter+=1
			else:
				print('dade eshtebash ')			
			
		with open('input1.csv','w',newline='') as fill:
			writer=csv.writer(fill)	
			writer.writerows(Students.items())
def Readcsv():
	Average=OrderedDict()
	with open('input.csv') as Fin:
		RowReader=csv.reader(Fin)
		for row in RowReader:
			#hazf fazai khali('') az csv
			row=list(filter(None,row))
			#
			person=row[0]
			row=row[1:]
			for everynum in range(len(row)):
				row[everynum]=float(row[everynum])
			Average[person]=mean(row)
	return Average		
def calculate_averages():
	#temp dict to hold csv 
	tempdict=Readcsv().copy()
	showResault(tempdict)
	#newline='' remove space between every list when entered		
	with open('output.csv','w',newline='') as Out:
		writer=csv.writer(Out)
		writer.writerows(tempdict.items())
	checkquit()	
def calculate_sorted_averages():
	tempdict=Readcsv().copy()
	tempdict=sorted(tempdict.items(),key=lambda x: x[1])
	showResault(tempdict)
	with open('output.csv','w',newline='') as out:
			writer=csv.writer(out)
			writer.writerows(tempdict)
	checkquit()			
def calculate_three_best():
	tempdict=Readcsv().copy()
			#if reverse=True >> descending(nozoli)
	tempdict=sorted(tempdict.items(),key=lambda x: x[1],reverse=True)
	tempdict=tempdict[:3]
	showResault(tempdict)
	with open('output.csv','w',newline='') as out:
		writer=csv.writer(out)
		writer.writerows(tempdict)
	checkquit()	
def calculate_three_worst():
	tempdict=Readcsv().copy()
	tempdict=sorted(tempdict.items(),key=lambda x: x[1],reverse=False)			
	#split three worst first of list
	tempdict=tempdict[:3]
	tempdict=OrderedDict(tempdict)
	showResault(tempdict)
	with open('output.csv','w',newline='') as out:
	 	writer=csv.writer(out)
	 	writer.writerows(map(lambda x: [x],tempdict.values()))
	checkquit()	
def calculate_average_of_averages():
	tempdict=Readcsv().copy()
	tempdict['Average']=mean(tempdict.values())
	print('average_of_averages :%s'% tempdict['Average'])	
	with open('output.csv','w',newline='') as out:
		writer=csv.writer(out)
		writer.writerow(tempdict.values())
	checkquit()	
def entery():
	print('/***** SIMPLE Average Calculator *****/')
	#fillcsv()	
	entery=int(input('\t1:calculate_averages\n\t2:calculate_three_best\n\t3:calculate_three_worst\n\t4:calculate_sorted_averages\n\t5:calculate_average_of_averages\n:'))
	print('----------------')
	if entery==1:
		calculate_averages()
	elif entery==2:
		calculate_three_best()
	elif entery==3:
		calculate_three_worst()
	elif entery==4:
		calculate_sorted_averages()
	elif entery==5:
		calculate_average_of_averages()
def showResault(Dictionary):
	if (type(Dictionary) is dict or type(Dictionary) is OrderedDict):
		for everyitem in Dictionary.items():
			print(' %s :%s' %(everyitem[0],everyitem[1]))	
	else:
		for everyitem in Dictionary:
			print(' %s :%s' %(everyitem[0],everyitem[1]))		
def checkquit():
	useranswer=(input('-------------------------\nDo you really want to exit ([y]/n)?').strip())
	print('----------------')
	if(useranswer=='y'):
		print('see u soon dude')
	elif useranswer=='n':
		clear=lambda: os.system('cls')
		clear()
		entery()	
entery()	
			