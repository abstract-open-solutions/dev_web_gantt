# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Abstract srl (<http://www.abstract.it>)
#    All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Web Gant from odoo dev',
    'description': """
Odoo Web Gantt chart view.
==========================

Override to get features from dev version.

See https://github.com/odoo-dev/odoo/commit/9f07606cf9b26d14ae38c0d1093204a3f9fb2008.
""", # noqa
    'version': '2.0',
    'depends': [
        'web_gantt',
        'project',
    ],
    'author': 'Abstract',
    'license': 'AGPL-3',
    'category': 'Web',
    'website': 'http://www.abstract.it',
    'data': [
        'views/web_gantt.xml',
        'views/project_view.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'auto_install': False,
}
