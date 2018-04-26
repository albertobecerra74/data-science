#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:05:54 2018

@author: alberto
"""
import PyPDF2

try: 
    pdfFileObj = open('/home/alberto/Documentos/books/Spark_in_Action.pdf', 'rb')

except FileNotFoundError:
    print('El fichero introducido no existe')


else:
    print(pdfFileObj)
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    numpag = pdfReader.numPages
    
    print(numpag)
    
    for i in range(numpag):
        pageObj = pdfReader.getPage(i)

        print(pageObj.extractText())
    
        respuestavalida = False
        continua = ''
        
        while respuestavalida == False:
            continua = input("Desea seguir? (S/N)?")    
       
            if continua == 'S':
                respuestavalida = True
                break
            elif continua == 'N':
                respuestavalida = True
                break

            elif continua == '':
                respuestavalida = True
                break
       
            else:
                continue
            
            
        if continua not in  ('S',''):
            break
        
        
        
                        
    



