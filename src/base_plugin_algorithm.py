# -*- coding: utf-8 -*-

"""
/***************************************************************************
BASE_PLUGIN
 
 Aquí va la descripció del plugin, que fa, ....

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Sammy'
__date__ = '2024-02-27'
__copyright__ = '(C) 2024 by Sammy'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from os import path

from qgis.PyQt.QtGui import QIcon

from qgis.PyQt.QtCore import QCoreApplication

from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterVectorLayer)

class base_plugin_Algorithm_Class(QgsProcessingAlgorithm):
    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    INPUT = 'capa_de_entrada'
    feedback_ctl = None

    def initAlgorithm(self, config):
        """
        Paràmetres d'entrada i sortida del algorithme, nomès es un exemple, i es poden possar els que
        es necessitin per realitzar el procés
        """
        in_layer_param = self.INPUT
        in_layer_text = 'Seleccionar capa entrada'
        self.addParameter(QgsProcessingParameterVectorLayer(in_layer_param, in_layer_text, types=[QgsProcessing.TypeVectorLine], defaultValue=None))

    def processAlgorithm(self, parameters, context, feedback):
        """
        Aquí es on es fa tota la feina.
        """
        self.feedback_ctl = feedback # Guardem el feedback per si cal utilitzar-ho en una altre part del algorisme

        self.feedback_ctl.pushInfo('Iniciant el algorisme...')

        out_layer = parameters[self.INPUT]  # Recollim el paràmetre de entrada

        # Fem una crida a una funció interna del algorisme
        self.feedback_ctl.pushInfo(self.__hola_mon())

        """
        Cosetes que fa
        Més cosetes
        Altres cosetes
        .
        .
        .
        """

        self.feedback_ctl.pushInfo('Acabant el algorisme...')

        """
          Sortida de l'algorisme, per convenció un JSON amb la clau "OUTPUT" i el valor de sortida,
          però pot ser qualsevol altre cosa.
        """
        return {self.OUTPUT: out_layer}

    def icon(self):
        """
        La icona que defineix el algorisme
        """
        icon_file = '{0}/icons/{1}.svg'.format(path.dirname(__file__) ,self.name())
        return QIcon(icon_file)

    def name(self):
        """
        Nom del algorisme.
        Es l'identificador intern de l'algorisme per QGIS.
        Ha de ser el més curt possible, amb caràcters alfanumèrics i sense
        espais, comes, o caràcters similars.
        """
        return 'base_plugin_algorithm'

    def displayName(self):
        """
        Nom de l'algorisme que es mostrarà a la caixa de eines de QGIS.
        """
        return 'Base Plugin Algorithm [v1.0]'

    def shortHelpString(self):
        """
        Text de ajuda que mostrarà QGIS al executar el algorisme.
        Pot contenir format HTML.
        """
        text_ajut = []
        text_ajut.append('<b>Base Plugin Algorithm</b>')
        text_ajut.append('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor')
        text_ajut.append('incididunt ut labore et dolore magna aliqua. Risus nullam eget felis eget nunc')
        text_ajut.append('lobortis mattis aliquam. Dictum non consectetur a erat.')
        return '<br/>'.join(text_ajut)

    def helpUrl(self):
        """
        Arxiu o web d'ajuda del algorisme/plugin
        Pot ser una URL o directament un arxiu amb l'ajuda.
        Per defecte, aquest plugin busca al directori "/help" (que penja del plugin), un arxiu PDF amb el mateix nom que l'algorisme
        """
        link_ajuda = 'file:///{0}/help/{1}.pdf'.format(path.dirname(__file__) ,self.name())
        print(link_ajuda)
        return link_ajuda

    def group(self):
        """
        Grup al que pertany l'algorisme
        """
        return self.groupId()

    def groupId(self):
        """
        Identificar únic del grup al que pertany l'algorisme.
        COMPTE!!: Aquest "id" ha de ser únic per cada proveidor i nomès pot tenir
        caràcters alfanumèrics i en minúscula, sense espais ni cap altra caràcter de
        formateig.
        """
        return ''

    def createInstance(self):
        return base_plugin_Algorithm_Class()

    # Funcions privades del algorisme
    # -------------------------------
    """
    Aquí podriem possar les funcions internes que fa servir
    l'algorisme
    """
    def __hola_mon(self):
        return 'HOLA MON!!!'
