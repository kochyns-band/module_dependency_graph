# -*- coding: utf-8 -*-
{
    'name': "Graph Module Dependency",
    'summary': """Graph Module Dependency""",
    'author': "Kochyn's Band",
    'website': "https://github.com/kochyns-band/module_dependency_graph",
    'category': 'Tools',
    'version': '11.0.1.0.1',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/assets.xml',
        'views/ir_module.xml',
    ],
    'qweb': [
        'static/src/xml/module_graph.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    "application": False,
}