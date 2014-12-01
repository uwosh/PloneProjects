# -*- coding: utf-8 -*-
#
# File: wfsubscribers.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


##code-section module-header #fill in your manual code here
##/code-section module-header


def preAcceptProject(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition or \
       event.transition.id != 'accept_project':
        return
    ##code-section preAcceptProject #fill in your manual code here
    ##/code-section preAcceptProject


def postRejectProject(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition or \
       event.transition.id != 'reject_project':
        return
    ##code-section postRejectProject #fill in your manual code here
    ##/code-section postRejectProject


def postSubmitProject(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition or \
       event.transition.id != 'submit_project':
        return
    ##code-section postSubmitProject #fill in your manual code here
    ##/code-section postSubmitProject


def postAcceptProject(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition or \
       event.transition.id != 'accept_project':
        return
    ##code-section postAcceptProject #fill in your manual code here
    ##/code-section postAcceptProject


def preRejectProject(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition or \
       event.transition.id != 'reject_project':
        return
    ##code-section preRejectProject #fill in your manual code here
    ##/code-section preRejectProject


def preSubmitProject(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition or \
       event.transition.id != 'submit_project':
        return
    ##code-section preSubmitProject #fill in your manual code here
    ##/code-section preSubmitProject


def postResubmitProject(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition or \
       event.transition.id != 'resubmit_project':
        return
    ##code-section postResubmitProject #fill in your manual code here
    ##/code-section postResubmitProject


def preResubmitProject(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition or \
       event.transition.id != 'resubmit_project':
        return
    ##code-section preResubmitProject #fill in your manual code here
    ##/code-section preResubmitProject



##code-section module-footer #fill in your manual code here
##/code-section module-footer

