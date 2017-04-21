# -*- coding: UTF-8 -*-
# Copyright 2007-2008 One Laptop Per Child
# Copyright 2007 Gerard J. Cerchio <www.circlesoft.com>
# Copyright 2008 Andrés Ambrois <andresambrois@gmail.com>
# Copyright 2010 Marcos Orfila <www.marcosorfila.com>
#
# Copyright 2012 I. De Marchi <tangram.peces@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging
import sugar.logger
import gtk
import pygtk
from gettext import gettext as _
from sugar.activity.activity import Activity, ActivityToolbox
import pango
import os
import commands
import sys


logger = logging.getLogger('JPeces')


class JPeces_Start(Activity):

    def __init__(self, handle):
        # Initialize the parent
        Activity.__init__(self, handle)
        logger.debug('Initiating JPeces')
     
        self.java_path = self.get_java_path()
	if self.java_path != "":  		
	   self.create_script(os.getenv("JPECES_SCRIPT"))
           sys.exit(0)

	
    def write_file(self, file_path):
	raise NotImplementedError
	
    def read_file(self, file_path):
	raise NotImplementedError


    def create_script(self, script_path):
       """Create the script to run the program"""

       # In the future, some options to be included in the tuxmath script (like "--nosound")
       # could be selected by the user.
       script_text = self.java_path + " -jar $SUGAR_BUNDLE_PATH/jpeces/JPeces.jar"

       f = open(script_path, 'w')
       f.write(script_text)
       f.close()
       os.chmod(script_path, 0755)


    def get_java_path(self):
       """
       Check whether java exists and return the path to the "java" command.
       Returns an empty string in case java is not found.
       """

       # If "java -version" command fails, then java is not in the PATH
       status, output = commands.getstatusoutput('java -version')
       if status == 0:
          # Java was found
          return commands.getoutput('which java')
       else:
          return ''



