from __future__ import absolute_import
def classFactory(iface):

    from .WntOS import WntOS
    return WntOS(iface)
