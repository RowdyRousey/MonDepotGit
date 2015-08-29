#! /usr/bin/python
# -*- coding: utf-8 -*-

###############################
# Cartouche de présentation
###############################

import os
import sys
import re
import pygtk
pygtk.require('2.0')
import gtk

ERROR = 0

LONG_BUFFER = 1024
LONG_HEAD_BUFFER = 20
LONG_HEAD_BLOC = 6 

REGEX_FIN_BUFFER="^ZZZZ"
ExprFinMessage = re.compile( REGEX_FIN_BUFFER, re.MULTILINE)

REGEX_MODULE = {'MESG': "^\x10.\x01", 'OLDI': "^\x08.\x01"}
ExprModuleOldi = re.compile(REGEX_MODULE["OLDI"],re.DOTALL)
ExprModuleMesg = re.compile(REGEX_MODULE["MESG"],re.DOTALL)

REGEX_SPACE = " {2,}"
ExprSpace = re.compile( REGEX_SPACE, re.MULTILINE )

REGEX_DATE = "^\d{2}/\d{2}/\d{4} \d{2}H\d{2}'\d{2}\" "
ExprDate = re.compile( REGEX_DATE, re.DOTALL )

REGEX_MSG_OLDI = "\([A-Z]{3}.*|-TITLE.*"
ExprMess = re.compile(REGEX_MSG_OLDI,re.MULTILINE)

PATH_LOG='./Log/'






