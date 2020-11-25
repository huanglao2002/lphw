try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    config ={
        'description': 'My_Project',
        'auth': 'Jim huang',
        'url': 'url to get it at.',
        'download_url': 'where to download it',
        'author_email': 'My email',
        'verion': '0.1',
        'install_requests' : ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
    }