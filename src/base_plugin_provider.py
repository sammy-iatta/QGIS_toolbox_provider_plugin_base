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

from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon

from os import path

from .base_plugin_algorithm import base_plugin_Algorithm_Class

class base_plugin_Provider_Class(QgsProcessingProvider):

    def __init__(self):
        """
        Default constructor.
        """
        QgsProcessingProvider.__init__(self)

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        self.addAlgorithm(base_plugin_Algorithm_Class())
        # add additional algorithms here
        # self.addAlgorithm(MyOtherAlgorithm())

    def id(self):
        """
        Retorna un identificador unic per definir el proveidor. Poden ser
        les sigles de la empresa, codi de projecte, ... però ha de ser curt i només
        amb caracters (p.e. MY_UTILS, VEC_TOOLS, ...)
        """
        return 'BASE_PLUGIN_PROVIDER'

    def name(self):
        """
        Retorna el nom del proveidor, que s'utilitza a la caixa de eines de QGIS
        per agrupar totes les funcions d'aquest proveidor.
        hauria de ser un string el més curt possible
        """
        return 'BASE PLUGIN PROVIDER- v1.0 -'

    def icon(self):
        """
        La icona que s'utilitzarà pel proveidor a la caixa de eines de QGIS
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        icon_file = '{0}/icons/{1}.svg'.format(path.dirname(__file__) ,self.id())
        return QIcon(icon_file)

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return 'BASE PLUGIN PROVIDER by Sammy'
