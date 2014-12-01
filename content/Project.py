# -*- coding: utf-8 -*-
#
# File: Project.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.uwosh_ploneprojects.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseFolderSchema['title'].copy()
copied_fields['title'].searchable = 1
copied_fields['title'].widget.label = "Project Name"
schema = Schema((

    copied_fields['title'],

    TextField(
        name='briefDescription',
        widget=TextAreaWidget(
            rows=3,
            label="Brief Description",
            label_msgid='uwosh_ploneprojects_label_briefDescription',
            i18n_domain='uwosh_ploneprojects',
        ),
        searchable=1,
    ),
    TextField(
        name='fullDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            rows=3,
            label="Full Description",
            label_msgid='uwosh_ploneprojects_label_fullDescription',
            i18n_domain='uwosh_ploneprojects',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    StringField(
        name='requestorName',
        widget=StringField._properties['widget'](
            label="Requestor Name",
            label_msgid='uwosh_ploneprojects_label_requestorName',
            i18n_domain='uwosh_ploneprojects',
        ),
        required=1,
    ),
    StringField(
        name='requestorEmail',
        widget=StringField._properties['widget'](
            label="Requestor Email",
            label_msgid='uwosh_ploneprojects_label_requestorEmail',
            i18n_domain='uwosh_ploneprojects',
        ),
        required=1,
    ),
    StringField(
        name='requestorOrg',
        widget=StringField._properties['widget'](
            label="Requestor Organization",
            label_msgid='uwosh_ploneprojects_label_requestorOrg',
            i18n_domain='uwosh_ploneprojects',
        ),
        required=1,
    ),
    DateTimeField(
        name='projectDueDate',
        widget=DateTimeField._properties['widget'](
            label="Project Due Date",
            label_msgid='uwosh_ploneprojects_label_projectDueDate',
            i18n_domain='uwosh_ploneprojects',
        ),
        write_permission="UWOshPloneProjects: Modify Advanced Content",
    ),
    StringField(
        name='priority',
        widget=SelectionWidget(
            label="Priority",
            label_msgid='uwosh_ploneprojects_label_priority',
            i18n_domain='uwosh_ploneprojects',
        ),
        write_permission="UWOshPloneProjects: Modify Advanced Content",
        vocabulary=('Low', 'Medium', "High"),
    ),
    StringField(
        name='url',
        widget=StringField._properties['widget'](
            label='Url',
            label_msgid='uwosh_ploneprojects_label_url',
            i18n_domain='uwosh_ploneprojects',
        ),
        write_permission="UWOshPloneProjects: Modify Advanced Content",
    ),
    TextField(
        name='notes',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            rows=3,
            label='Notes',
            label_msgid='uwosh_ploneprojects_label_notes',
            i18n_domain='uwosh_ploneprojects',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='requirements',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            rows=3,
            label='Requirements',
            label_msgid='uwosh_ploneprojects_label_requirements',
            i18n_domain='uwosh_ploneprojects',
        ),
        read_permission="UWOshPloneProjects: View Advanced Content",
        searchable=1,
        default_output_type='text/html',
        write_permission="UWOshPloneProjects: Modify Advanced Content",
    ),
    TextField(
        name='useCases',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            rows=3,
            label="Use Cases",
            label_msgid='uwosh_ploneprojects_label_useCases',
            i18n_domain='uwosh_ploneprojects',
        ),
        read_permission="UWOshPloneProjects: View Advanced Content",
        searchable=1,
        default_output_type='text/html',
        write_permission="UWOshPloneProjects: Modify Advanced Content",
    ),
    TextField(
        name='features',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            rows=3,
            label='Features',
            label_msgid='uwosh_ploneprojects_label_features',
            i18n_domain='uwosh_ploneprojects',
        ),
        read_permission="UWOshPloneProjects: View Advanced Content",
        searchable=1,
        default_output_type='text/html',
        write_permission="UWOshPloneProjects: Modify Advanced Content",
    ),
    StringField(
        name='svnUrl',
        widget=StringField._properties['widget'](
            label='Svnurl',
            label_msgid='uwosh_ploneprojects_label_svnUrl',
            i18n_domain='uwosh_ploneprojects',
        ),
        write_permission="UWOshPloneProjects: Modify Advanced Content",
        read_permission="UWOshPloneProjects: View Advanced Content",
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Project_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Project(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IProject)

    meta_type = 'Project'
    _at_rename_after_creation = True

    schema = Project_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('acceptProject')
    def acceptProject(self):
        """
        """
        pass


registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
##/code-section module-footer



