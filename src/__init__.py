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
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Sammy'
__date__ = '2024-02-27'
__copyright__ = '(C) 2024 by Sammy'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load plugin class from file.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .base_plugin import base_plugin_Class
    return base_plugin_Class()
