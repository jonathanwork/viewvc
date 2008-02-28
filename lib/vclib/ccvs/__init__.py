# -*-python-*-
#
# Copyright (C) 1999-2008 The ViewCVS Group. All Rights Reserved.
#
# By using this file, you agree to the terms and conditions set forth in
# the LICENSE.html file which can be found at the top level of the ViewVC
# distribution or at http://viewvc.org/license-1.html.
#
# For more information, visit http://viewvc.org/
#
# -----------------------------------------------------------------------

def CVSRepository(name, rootpath, authorizer, utilities, use_rcsparse):
  if use_rcsparse:
    import ccvs
    return ccvs.CCVSRepository(name, rootpath, authorizer, utilities)
  else:
    import bincvs
    return bincvs.BinCVSRepository(name, rootpath, authorizer, utilities)
