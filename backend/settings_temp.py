TEMPLATES = [ 
    { 
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [os.path.join(BASE_DIR, 'frontend/templates')], 
        'APP_DIRS': True, 
        'OPTIONS': { 
            'context_processors': [ 
                'django.template.context_processors.debug', 
                'django.template.context_processors.request', 
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
            ], 
        }, 
    }, 
] 
ECHO is on.
STATIC_URL = 'static/' 
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend/static')] 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'core',  # Add this line 
] 
