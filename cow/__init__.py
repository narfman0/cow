plugin_type_choices = []
plugin_map = {}


def register(plugin_class, name):
    plugin_type_choices.append((name, name))
    plugin_map[name] = plugin_class
