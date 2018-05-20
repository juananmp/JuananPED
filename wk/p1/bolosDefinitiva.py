class RondaNoValida(Exception):
	pass

def puntuacion(partida):


	resultado=0
	index=0
	for rondaIndice in range(len(partida)):
		ronda = partida[index]
		tirada1,tirada2 = ronda
		if tirada1<0 or tirada1>10 or tirada2<0 or tirada2>10 or sum(ronda)>10:
			raise RondaNoValida
		if tirada1==10:
			rondaSig=partida[index+1]
			tirada1Sig,tirada2Sig=rondaSig
			if tirada1Sig == 10:
				rondaSigSig = partida[index+2]
				tirada1SigSig, tirada2SigSig = rondaSigSig
				resultado = resultado + 10 + tirada1Sig + tirada1SigSig
				index = index+1
			else:		
				resultado = resultado + 10 + tirada1Sig + tirada2Sig
				index = index+1
		elif tirada1 + tirada2 ==10:
			rondaSig=partida[index+1]
			tirada1Sig,tirada2Sig=rondaSig
			resultado = resultado + 10 + tirada1Sig
			index = index+1
		else:
			resultado = resultado + tirada1 + tirada2
			index = index+1
	return resultado	


