# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) Monoyer Fabian (info@olabs.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Website Sale Tracker",
    'author': "O'Labs",
    'website': "http://www.olabs.be",
    'description': """


    """,
    'category': 'website',
    'version': '1.1',
    'depends': ['website','website_sale'],
   'data': [
         'security/ir.model.access.csv',
         'views/backend.xml'
       ],
    'images':['static/description/banner.jpg',],
    'installable': True,
}

