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

def index (req, sd="0"):

	busca = int(sd)

	tickets = executa_sql("""SELECT id, DATE_FORMAT(entra, %s), clase, procedencia, estado, tipo, descripcion, accion, DATE_FORMAT(sale, %s) FROM ticket WHERE id = %s""" % (fechaselect, fechaselect, busca,))


	pag="""
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
					<li class="opcion"><a class="opcion" href="/sdirectory/index.py">Volver</a></li>
				</ul>
				<h2 class="bar">
					<span class="version" style="text-align:right">%s</span>
				</h2>
			
				<p><table>
					<col width="100">
					<col width="100">
					<col width="90">
					<col width="100">
					<col width="90">
					<col width="90">
					<col width="400">
					<col width="400">
					<col width="100">
					<thead>
						<tr>
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
					</thead>
						<tbody>
							%s
						</tbody>
				</table>
			
				%s
			
			</body>
		</html>
	"""


	filas = ""
	contador = 0

	for ticket in tickets:
		filas += """
			<tr>
				<td class="par">SD%s</td>
				<td class="par">%s</td>
		""" % (ticket[0], ticket[1])
		
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



	formulario = """
		<form action=/sdirectory/modificar.py/modconfirm>
			<input type="hidden" name ="sd" value="%s">
				Estado del ticket:
				<select name="clase">

	""" % (ticket[0],)
	
	if ticket[2] == 1:
		formulario += """
			<option selected value="1">Incidencia</option>
			<option value="2">Petición</option>
			<option value="3">Nota</option>
		"""

	if ticket[2] == 2:
		formulario += """
			<option value="1">Incidencia</option>
			<option selected value="2">Petición</option>
			<option value="3">Nota</option>
		"""

	if ticket[2] == 3:
		formulario += """
			<option value="1">Incidencia</option>
			<option value="2">Petición</option>
			<option selected value="3">Nota</option>
		"""

	elif ticket[2] == 0:
		formulario += """
			<option value="1">Incidencia</option>
			<option value="2">Petición</option>
			<option value="3">Nota</option>
		"""
	
	formulario += """
		</select>

			Tipo:
		<select name="estado">
	"""

	if ticket[4] == 1:
		formulario += """
			<option selected value="1">En Proceso</option>
			<option value="2">Devuelto</option>
			<option value="3">Resuelto</option>
			<option value="4">Escalado</option>
			<option value="5">Pendiente Autorización</option>
			<option value="6">Caducidad</option>
		"""

	if ticket[4] == 2:
		formulario += """
			<option value="1">En Proceso</option>
			<option selected value="2">Devuelto</option>
			<option value="3">Resuelto</option>
			<option value="4">Escalado</option>
			<option value="5">Pendiente Autorización</option>
			<option value="6">Caducidad</option>
		"""

	if ticket[4] == 3:
		formulario += """
			<option value="1">En Proceso</option>
			<option value="2">Devuelto</option>
			<option selected value="3">Resuelto</option>
			<option value="4">Escalado</option>
			<option value="5">Pendiente Autorización</option>
			<option value="6">Caducidad</option>
		"""

	if ticket[4] == 4:
		formulario += """
			<option value="1">En Proceso</option>
			<option value="2">Devuelto</option>
			<option value="3">Resuelto</option>
			<option selected value="4">Escalado</option>
			<option value="5">Pendiente Autorización</option>
			<option value="6">Caducidad</option>
		"""
				
	if ticket[4] == 5:
		formulario += """
			<option value="1">En Proceso</option>
			<option value="2">Devuelto</option>
			<option value="3">Resuelto</option>
			<option value="4">Escalado</option>
			<option selected value="5">Pendiente Autorización</option>
			<option value="6">Caducidad</option>
		"""
				
	if ticket[4] == 6:
		formulario += """
			<option value="1">En Proceso</option>
			<option value="2">Devuelto</option>
			<option value="3">Resuelto</option>
			<option value="4">Escalado</option>
			<option value="5">Pendiente Autorización</option>
			<option selected value="6">Caducidad</option>
		"""

	elif ticket[4] == 0:
		formulario += """
			<option value="1">En Proceso</option>
			<option value="2">Devuelto</option>
			<option value="3">Resuelto</option>
			<option value="4">Escalado</option>
			<option value="5">Pendiente Autorización</option>
			<option value="6">Caducidad</option>
		"""



	formulario += """
		</select>

			Tipo:
		<select name="tipo">
	"""



	if ticket[5] == 1:
		formulario += """
			<option selected value="1">Misc.</option>
			<option value="2">Datos</option>
			<option value="3">VoIP</option>
			<option value="4">WiFI</option>
			<option value="5">Seguridad</option>
		"""

	if ticket[5] == 2:
		formulario += """
			<option value="1">Misc.</option>
			<option selected value="2">Datos</option>
			<option value="3">VoIP</option>
			<option value="4">WiFI</option>
			<option value="5">Seguridad</option>
		"""

	if ticket[5] == 3:
		formulario += """
			<option value="1">Misc.</option>
			<option value="2">Datos</option>
			<option selected value="3">VoIP</option>
			<option value="4">WiFI</option>
			<option value="5">Seguridad</option>
		"""

	if ticket[5] == 4:
		formulario += """
			<option value="1">Misc.</option>
			<option value="2">Datos</option>
			<option value="3">VoIP</option>
			<option selected value="4">WiFI</option>
			<option value="5">Seguridad</option>
		"""

	if ticket[5] == 5:
		formulario += """
			<option value="1">Misc.</option>
			<option value="2">Datos</option>
			<option value="3">VoIP</option>
			<option value="4">WiFI</option>
			<option selected value="5">Seguridad</option>
		"""

	elif ticket[5] == 0:
		formulario += """
			<option value="1">Misc.</option>
			<option value="2">Datos</option>
			<option value="3">VoIP</option>
			<option value="4">WiFI</option>
			<option value="5">Seguridad</option>
		"""




	formulario += """
			</select>
			<br>
			Descripción:<br><textarea name="descripcion" cols="65" rows="10" textmode="multiLine">%s</textarea><br>
			Notas o Solución aportada:<br><textarea name="accion" cols="65" rows="10" textmode="multiLine">%s</textarea><br>            
			Fecha de solución: <input type="text" size="10" name="sale" value="%s"/><br>
			<input type="submit" value="Modificar"/>
		</form> 
	""" % (ticket[6], ticket[7], ticket[8])




	return pag % (version, filas, formulario)


def modconfirm (req, sd="", clase="", estado="", tipo="", descripcion="", accion="", sale=""):


	busca = int(sd)

	executa_sql("""UPDATE ticket SET clase='%s', estado='%s', tipo='%s', descripcion='%s', accion='%s', sale=(STR_TO_DATE(REPLACE('%s','/','.'), GET_FORMAT(date, 'EUR'))) WHERE id = %s""" % (clase, estado, tipo, descripcion, accion, sale, busca))

	pag = """

	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
			<link rel="stylesheet" href="/sdirectory/estilo.css">
			<meta http-equiv="refresh" content="2;/sdirectory/index.py">
			<title>SDirectory - Control de tickets SD</title>
		</head>
        <body>
			<h1>SDirectory</h1>
			<p>Se ha modificado el ticket SD%s, volviendo a la ventana principal... Si no funciona pulsar</p>
			<a href="/sdirectory/index.py">Aquí</a>

		</body>
	</html>
	"""

	return pag % sd