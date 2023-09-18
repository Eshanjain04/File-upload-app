# -*- coding: utf-8 -*-
class DocumentationBuilder:
    def __init__(self):
        self.project_name = 'Finverv UI Admin'
        self.description = 'Api documentation for UI Admin'
        self.email = 'sangeet@finverv.com'
        self.servers = [
            'http://127.0.0.1:12521/v2',
            'https://sandbox-ui-admin.finverv.in/v2'
        ]

    def project_servers(self):
        servers = []
        for item in self.servers:
            servers.append({
                'url': item
            })
        return servers

    def project_description(self):
        base_structure = {
            'openapi': '3.0.1',
            'info': {
                'title': self.project_name,
                'description': self.description,
                'contact': {
                    'email': self.email
                },
                'version': '1.0'
            },
            'servers': self.project_servers(),
            'security': [
                {
                    'Bearer': []
                }
            ],
            'components': {
                'securitySchemes': {
                    'Bearer': {
                        'type': 'apiKey',
                        'description': 'Enter the token e.g. Bearer '
                                       'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
                                       'eyJ1c2VyX2lkIjoiNjMwZjIyZGRmNzEyNjU0MjFhM'
                                       'mIzMTFjIiwiZXhwIjoxNzA2MTc3MjA1fQ.F5yFJcF'
                                       '6NQtfeAtRKPSPeY5-0UyBM-oyPTSsayNL1g4',
                        'name': 'Authorization',
                        'in': 'header'
                    }
                }
            },
        }

        return base_structure
