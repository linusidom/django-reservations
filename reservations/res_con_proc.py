from django.conf import settings # import the settings file

def language_settings(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'LANGUAGE_CODE': settings.LANGUAGE_CODE}