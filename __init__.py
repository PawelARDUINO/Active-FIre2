# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ActivefireV2
                                 A QGIS plugin
 This is the second release of the Active FIre plugin
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-11-01
        copyright            : (C) 2020 by The Map Workshop
        email                : pawel.jan.dzierzynski@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ActivefireV2 class from file ActivefireV2.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .active_fire2 import ActivefireV2
    return ActivefireV2(iface)
