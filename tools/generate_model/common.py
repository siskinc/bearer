def table_name_to_class_name(table):
    return ''.join(word.title() for word in table[2:].split('_'))
