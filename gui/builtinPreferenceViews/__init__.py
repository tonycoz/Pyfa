__all__ = ["pyfaGeneralPreferences","pyfaHTMLExportPreferences","pyfaUpdatePreferences","pyfaNetworkPreferences"]

import wx

if not 'wxMac' in wx.PlatformInfo or ('wxMac' in wx.PlatformInfo and wx.VERSION >= (3,0)):
    __all__.append("pyfaCrestPreferences")
