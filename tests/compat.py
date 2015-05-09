try:
    from django.template import engines

    def get_old_options():
        return engines.templates['djinga']['OPTIONS'].copy()

    def set_environment(**options):
        try:
            del engines._engines['djinga']
        except KeyError:
            pass
        engines.templates['djinga']['OPTIONS'] = options
        engines['djinga']  # this reinitializes the djinga backend

except ImportError:
    # django < 1.8
    from djinga import engines

    last_options = {}

    def get_old_options():
        return last_options

    def set_environment(**options):
        engines._env = None
        engines._init_env(**options)
        last_options = options.copy()
