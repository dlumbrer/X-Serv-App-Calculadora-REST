#!/usr/bin/python

import webapp
import random


class calculadoraApp(webapp.webApp):

    def parse(self, request):
        op = request.split()[0]
        rec = request.split()[1].split("/")[1]
        cuerpo = request.split("\r\n\r\n")[1]        
        return (op,rec,cuerpo)


    def process(self, parsedRequest):
        if parsedRequest[0] == "GET":
            try:
                if len(self.operacion.split("+")) == 2:
                    suma = float(self.operacion.split("+")[0]) + float(self.operacion.split("+")[1])
                    return ("200 OK", "<html><body><p>Suma: " + str(suma) + "</p></body></html>")
                if len(self.operacion.split("-")) == 2:
                    resta = float(self.operacion.split("-")[0]) - float(self.operacion.split("-")[1])
                    return ("200 OK", "<html><body><p>Resta: " + str(resta) + "</p></body></html>")
                if len(self.operacion.split("*")) == 2:
                    suma = float(self.operacion.split("*")[0]) * float(self.operacion.split("*")[1])
                    return ("200 OK", "<html><body><p>Multiplicacion: " + str(suma) + "</p></body></html>")	
                if len(self.operacion.split("/")) == 2:
                    division = float(self.operacion.split("/")[0]) / float(self.operacion.split("/")[1])
                    return ("200 OK", "<html><body><p>Division: " + str(division) + "</p></body></html>")
            except AttributeError:
                #Todavia no se ha iniciado self.operacion
                return ("404 Not Found", "<html><body><p>NO HAY OPERACION AUN</p></body></html>")
            except ValueError:
                #Operacion con algun fallo
                return ("404 Not Found", "<html><body><p>La operacion no es correcta.</p></body></html>")

        elif parsedRequest[0] == "PUT":
            self.operacion = parsedRequest[2]
            print self.operacion
            return ("200 OK", "<html><body><p>Actualizado operando</p></body></html>")	

if __name__ == "__main__":
    servaleat = calculadoraApp("localhost", 1234)
