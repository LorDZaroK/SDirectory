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
from index import version, fechaselect

def index(req,):

	pag = """
	
		<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
				<title>SDirectory - Control de tickets SD</title>
				<link rel="stylesheet" type="text/css" href="estilo.css" media="screen"/>
				<link rel="shortcut icon" href="favicon.ico">
		</head>
		<body>
			<h1>SDirectory</h1>
			<ul style="list-style-type:none;">
				<li class="opcion"><a class="opcion" href="index.py">Volver</a></li>
			</ul>
			<h2 class="bar">
				<span class="version" style="text-align:right">%s</span>
			</h2>
			<h2>Estadísticas</h2>

			<p><table>
				<col width="200">
				<col width="100">
			<thead>
				<tr>	
					<th>Tipo</th>
					<th>Total</th>
				</tr>
				<tbody>
					<tr>
						<td class="par">Todos los Tickets</td>
						<td class="par">%s</td>
					</tr>
					<tr>
						<td class="impar">Tickets Activos</td>
						<td class="impar">%s</td>
					</tr>				
					<tr>
						<td class="par">Incidencias</td>
						<td class="par">%s</td>
					</tr>
					<tr>
						<td class="impar">Peticiones</td>
						<td class="impar">%s</td>
					</tr>
					<tr>
						<td class="par">Notas</td>
						<td class="par">%s</td>
					</tr>				
					<tr>
						<td class="impar">Resueltos</td>
						<td class="impar">%s</td>
					</tr>
					<tr>
						<td class="par">Devueltos al CAU</td>
						<td class="par">%s</td>
					</tr>
					<tr>
						<td class="impar">Escalados</td>
						<td class="impar">%s</td>
					</tr>
					<tr>
						<td class="par">Pendientes de Autorización</td>
						<td class="par">%s</td>
					</tr>
					<tr>
						<td class="impar">A la espera de caducar</td>
						<td class="impar">%s</td>
					</tr>
					<tr>
						<td class="par">Datos</td>
						<td class="par">%s</td>
					</tr>
					<tr>
						<td class="impar">VoIP</td>
						<td class="impar">%s</td>
					</tr>
					<tr>
						<td class="par">WiFI</td>
						<td class="par">%s</td>
					</tr>
					<tr>
						<td class="impar">Seguridad</td>
						<td class="impar">%s</td>
					</tr>
					<tr>
						<td class="par">Misc</td>
						<td class="par">%s</td>
					</tr>
				</tbody>				
			</table>
			
		</body>
		</html>
	"""		
	
	
	contodos = 0
	todos = executa_sql("SELECT id FROM ticket  ORDER BY entra, id")
	
	for todo in todos:
		contodos = contodos+1
		
	conactivos = 0
	activos = executa_sql("SELECT id FROM ticket WHERE estado = 1")
	
	for activo in activos:
		conactivos = conactivos+1
		
	conincident = 0
	incidents = executa_sql("SELECT id FROM ticket WHERE clase = 1")
	
	for incident in incidents:
		conincident = conincident+1
		
	conpeticion = 0
	peticiones = executa_sql("SELECT id FROM ticket WHERE clase = 2")
	
	for peticion in peticiones:
		conpeticion = conpeticion+1
		
	connota = 0
	notas = executa_sql("SELECT id FROM ticket WHERE clase = 3")
	
	for nota in notas:
		connota = connota+1
		
	concgp = 0
	cgps = executa_sql("SELECT id FROM ticket WHERE estado = 3")
	
	for cgp in cgps:
		concgp = concgp+1
		
	concau = 0
	caus = executa_sql("SELECT id FROM ticket WHERE estado = 2")
	
	for cau in caus:
		concau = concau+1
		
	consoc = 0
	socs = executa_sql("SELECT id FROM ticket WHERE estado = 4")
	
	for soc in socs:
		consoc = consoc+1
		
	conauth = 0
	auths = executa_sql("SELECT id FROM ticket WHERE estado = 5")
	
	for auth in auths:
		conauth = conauth+1
		
	concad = 0
	cads = executa_sql("SELECT id FROM ticket WHERE estado = 6")
	
	for cad in cads:
		concad = concad+1
		
	condatos = 0
	datos = executa_sql("SELECT id FROM ticket WHERE tipo = 2")
	
	for dato in datos:
		condatos = condatos+1
		
	convoip = 0
	voips = executa_sql("SELECT id FROM ticket WHERE tipo = 3")
	
	for voip in voips:
		convoip = convoip+1
		
	conwifi = 0
	wifis = executa_sql("SELECT id FROM ticket WHERE tipo = 4")
	
	for wifi in wifis:
		conwifi = conwifi+1
		
	consec = 0
	secs = executa_sql("SELECT id FROM ticket WHERE tipo = 5")
	
	for sec in secs:
		consec = consec+1
		
	conmisc = 0
	miscs = executa_sql("SELECT id FROM ticket  WHERE tipo = 1")
	
	for misc in miscs:
		conmisc = conmisc+1

	return pag % (version, contodos, conactivos, conincident, conpeticion, connota, concgp, concau, consoc, conauth, concad, condatos, convoip, conwifi, consec, conmisc)