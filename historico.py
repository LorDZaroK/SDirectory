# -*- coding: iso-8859-1 -*-

#################################################################################
#	 Copyright 2012-2014 Albert Casas Granados									#
#																				#
# 	 This file is part of SDirectory.											#
#	 Written by Albert Casas Granados											#
#	 albert.casasgranados@gmail.com												#
#																				#
#    SDirectory is free software: you can redistribute it and/or modify			#
#    it under the terms of the GNU General Public License as published by		#
#    the Free Software Foundation, either version 3 of the License, or			#
#    (at your option) any later version.										#
#																				#
#    SDirectory is distributed in the hope that it will be useful,				#
#    but WITHOUT ANY WARRANTY; without even the implied warranty of				#
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the				#
#    GNU General Public License for more details.								#
#																				#
#    You should have received a copy of the GNU General Public License			#
#    along with SDirectory.  If not, see <http://www.gnu.org/licenses/>.		#
#																				#
#################################################################################

from __future__ import division
from mod_python import Session, util
import MySQLdb
from bbdd import executa_sql
from index import version

def index (req, select):

	if select == "0":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket  ORDER BY entra, id")
		subtitle = "Todos los Tickets"
	if select == "1":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE clase = 1 ORDER BY entra, id")
		subtitle = "Incidencias"
	if select == "2":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE clase = 2 ORDER BY entra, id")
		subtitle = "Peticiones"
	if select == "3":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE clase = 3 ORDER BY entra, id")
		subtitle = "Notas"
	if select == "4":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE estado = 1 ORDER BY entra, id")
		subtitle = "Tickets Pendientes"
	if select == "5":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE estado = 3 ORDER BY entra, id")
		subtitle = "Resueltos"
	if select == "6":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE estado = 4 ORDER BY entra, id")
		subtitle = "Escalados a otros grupos"
	if select == "7":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE estado = 2 ORDER BY entra, id")
		subtitle = "Devueltos al CAU"
	if select == "8":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket  WHERE estado = 5 ORDER BY entra, id")
		subtitle = "Pendientes de Autorización"
	if select == "9":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE estado = 6 ORDER BY entra, id")
		subtitle = "Pendientes de caducar"
	if select == "10":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket  WHERE tipo = 1 ORDER BY entra, id")
		subtitle = "Tickets Misceláneos"
	if select == "11":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE tipo = 2 ORDER BY entra, id")
		subtitle = "Tickets de Datos"
	if select == "12":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE tipo = 3 ORDER BY entra, id")
		subtitle = "Tickets de VoIP"
	if select == "13":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE tipo = 4 ORDER BY entra, id")
		subtitle = "Tickets de WiFI"
	if select == "14":
		tickets = executa_sql("SELECT id, DATE_FORMAT(entra,'%d/%m/%Y'), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale,'%d/%m/%Y') FROM ticket WHERE tipo = 5 ORDER BY entra, id")
		subtitle = "Tickets de Seguridad"

	


	pag = """
		<html>
			<head>
                <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
                <title>SDirectory - Control de tickets SD</title>
                <link rel="stylesheet" type="text/css" href="/sdirectory/estilo.css" media="screen"/>
                <link rel="shortcut icon" href="favicon.ico">
			</head>
			<body>
                <h1>SDirectory</h1>
                
				<ul style="list-style-type:none;">
					<li class="opcion"><a class="opcion" href="index?select=0">Todos los Tickets</a></li>
					<li class="opcion"><a class="opcion" href="index?select=1">Incidencias</a></li>
					<li class="opcion"><a class="opcion" href="index?select=2">Peticiones</a></li>
					<li class="opcion"><a class="opcion" href="index?select=3">Notas</a></li>
					<li class="opcion"><a class="opcion" href="index?select=4">Tickets Pendientes</a></li>
					<li class="opcion"><a class="opcion" href="index?select=5">Resueltos</a></li>
					<li class="opcion"><a class="opcion" href="index?select=6">Escalados</a></li>
					<li class="opcion"><a class="opcion" href="index?select=7">Devueltos al CAU</a></li>
					<li class="opcion"><a class="opcion" href="index?select=8">Pendientes de Autorización</a></li>
					<li class="opcion"><a class="opcion" href="index?select=9">Pendiente de caducar</a></li>
					<li class="opcion"><a class="opcion" href="index?select=10">Misc.</a></li>
					<li class="opcion"><a class="opcion" href="index?select=11">Datos</a></li>
					<li class="opcion"><a class="opcion" href="index?select=12">VoIP</a></li>
					<li class="opcion"><a class="opcion" href="index?select=13">WiFI</a></li>
					<li class="opcion"><a class="opcion" href="index?select=14">Seguridad</a></li>
					<li class="opcion"><a class="opcion" href="/sdirectory/index.py">Volver</a></li>
                </ul>
                <h2 class="bar">
					<span class="version" style="text-align:right">%s</span>
                </h2>
				
				<h2>Tickets Pendientes</h2>
		
				<h2>%s</h2>
                <p><table>
					<col width="75">
					<col width="100">
					<col width="100">
					<col width="90">
					<col width="100">
					<col width="90">
					<col width="90">
					<col width="375">
					<col width="375">
					<col width="100">
					<thead>
						<tr>
							<th>Acción</th>
							<th># Ticket</th>
							<th>Recibido</th>
							<th>Clase</th>
							<th>Procedencia</th>
							<th>Estado</th>
							<th>Tipo</th>
							<th>Descripción</th>
							<th>Acción</th>
							<th>Fecha Acción</th>
						</tr>
						<tbody>
							%s
						</tbody>
				</table>
				<ul style="list-style-type:none;">
					<li class="opcion"><a class="opcion" href="#top">Subir</a></li>
					<li class="opcion"><a class="opcion" href="/sdirectory/index.py">Volver</a></li>
				</ul>
				<h2 class="bar"> 
					<span class="version" style="text-align:right">.</span>
				<h2>
			</body>
        </html>

	"""
	filas = ""
	contador = 0

	for ticket in tickets:
		contador = contador+1

		if contador % 2:
			filas += """
				<tr>
					<td class="par"><a href="/sdirectory/modificar.py/index?sd=%s">Modificar</a><br><a href="/sdirectory/borrar.py/index?sd=%s">Borrar</a></td>
					<td class="par">SD%s</td>
					<td class="par">%s</td>
			""" % (ticket[0], ticket[0], ticket[0], ticket[1])

			if ticket[2] == 0:
				filas += """<td class="par"> - </td>"""			
			if ticket[2] == 1:
				filas += """<td class="par">Incidencia</td>"""
			if ticket[2] == 2:
				filas += """<td class="par">Petición</td>"""
			if ticket[2] == 3:
				filas += """<td class="par">Nota</td>"""
			
			if ticket[3] == 0:
				filas += """<td class="par"> - </td>"""			
			if ticket[3] == 1:
				filas += """<td class="par">CAU</td>"""
			if ticket[3] == 2:
				filas += """<td class="par">Cliente</td>"""
			if ticket[3] == 3:
				filas += """<td class="par">CGP</td>"""
								
			if ticket[4] == 0:
				filas += """<td class="par"> - </td>"""
			if ticket[4] == 1:
				filas += """<td class="par">En Proceso</td>"""
			if ticket[4] == 2:
				filas += """<td class="par">Devuelta</td>"""
			if ticket[4] == 3:
				filas += """<td class="par">Resuelto</td>"""
			if ticket[4] == 4:
				filas += """<td class="par">Escalado</td>"""
			if ticket[4] == 5:
				filas += """<td class="par">Pendiente Autorización</td>"""
			if ticket[4] == 6:
				filas += """<td class="par">Caducidad</td>"""
			
			if ticket[5] == 0:
				filas += """<td class="par"> - </td>"""
			if ticket[5] == 1:
				filas += """<td class="par">Misc.</td>"""
			if ticket[5] == 2:
				filas += """<td class="par">Datos</td>"""
			if ticket[5] == 3:
				filas += """<td class="par">VoIP</td>"""
			if ticket[5] == 4:
				filas += """<td class="par">WiFI</td>"""
			if ticket[5] == 5:
				filas += """<td class="par">Seguridad</td>"""



			filas += """
					<td class="par">%s</td>
					<td class="par">%s</td>
					<td class="par">%s</td>
				</tr>
			""" % (ticket[6], ticket[7], ticket[8])

		else:
			filas += """
			<tr>
				<td class="impar"><a href="/sdirectory/modificar.py/index?sd=%s">Modificar</a><br><a href="/sdirectory/borrar.py/index?sd=%s">Borrar</a></td>
				<td class="impar">SD%s</td>
				<td class="impar">%s</td>
			""" % (ticket[0], ticket[0], ticket[0], ticket[1])

			if ticket[2] == 0:
				filas += """<td class="impar"> - </td>"""			
			if ticket[2] == 1:
				filas += """<td class="impar">Incidencia</td>"""
			if ticket[2] == 2:
				filas += """<td class="impar">Petición</td>"""
			if ticket[2] == 3:
				filas += """<td class="impar">Nota</td>"""
						
			if ticket[3] == 0:
				filas += """<td class="impar"> - </td>"""
			if ticket[3] == 1:
				filas += """<td class="impar">CAU</td>"""
			if ticket[3] == 2:
				filas += """<td class="impar">Cliente</td>"""
			if ticket[3] == 3:
				filas += """<td class="impar">CGP</td>"""
			
			if ticket[4] == 0:
				filas += """<td class="impar"> - </td>"""
			if ticket[4] == 1:
				filas += """<td class="impar">En Proceso</td>"""
			if ticket[4] == 2:
				filas += """<td class="impar">Devuelta</td>"""
			if ticket[4] == 3:
				filas += """<td class="impar">Resuelto</td>"""
			if ticket[4] == 4:
				filas += """<td class="impar">Escalado</td>"""
			if ticket[4] == 5:
				filas += """<td class="impar">Pendiente Autorización</td>"""
			if ticket[4] == 6:
				filas += """<td class="impar">Caducidad</td>"""
								
			if ticket[5] == 0:
				filas += """<td class="impar"> - </td>"""
			if ticket[5] == 1:
				filas += """<td class="impar">Misc.</td>"""
			if ticket[5] == 2:
				filas += """<td class="impar">Datos</td>"""
			if ticket[5] == 3:
				filas += """<td class="impar">VoIP</td>"""
			if ticket[5] == 4:
				filas += """<td class="impar">WiFI</td>"""
			if ticket[5] == 5:
				filas += """<td class="impar">Seguridad</td>"""
			
			
			filas += """    
					<td class="impar">%s</td>
					<td class="impar">%s</td>
					<td class="impar">%s</td>
				</tr>
			""" % (ticket[6], ticket[7], ticket[8])

	return pag % (version, subtitle, filas)