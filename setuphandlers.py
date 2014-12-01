# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('uwosh_ploneprojects: setuphandlers')
from Products.uwosh_ploneprojects.config import PROJECTNAME
from Products.uwosh_ploneprojects.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
##/code-section HEAD

def isNotuwosh_ploneprojectsProfile(context):
    return context.readDataFile("uwosh_ploneprojects_marker.txt") is None



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotuwosh_ploneprojectsProfile(context): return 
    shortContext = context._profile_path.split(os.path.sep)[-3]
    if shortContext != 'uwosh_ploneprojects': # avoid infinite recursions
        return
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()

def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotuwosh_ploneprojectsProfile(context): return
    shortContext = context._profile_path.split(os.path.sep)[-3]
    if shortContext != 'uwosh_ploneprojects': # avoid infinite recursions
        return
    site = context.getSite()



##code-section FOOT
##/code-section FOOT
