import re

object_pattern = re.compile(r'L.*;')
simple_array_pattern = re.compile(r'\[B|\[D|\[I|\[J|\[S|\[Z|\[C')
object_array_pattern = re.compile(r'\[L.*;')

def class_name(str):
    return re.sub(r'[/$]', '.', re.search(r'(?<=L).*(?=;->)', str).group(0))


def field_name(str):
    return re.search(r'(?<=\>).*(?=\:)', str).group(0)


def funct_name(str):
    return re.search(r'(?<=\>).*(?=\()', str).group(0)


def param_list(str):
    param_strs = _param_strs(str)
    param_list = _object_array(param_strs)
    param_list += _simple_array(param_strs)
    param_strs = re.sub(object_array_pattern, '', param_strs)
    param_list += _object(param_strs)
    param_list += _simple(re.sub(r'\[B|\[D|\[I|\[J|\[S|\[Z|\[C|L.*;', '', param_strs))
    return param_list


def _param_strs(str):
    return re.search(r'(?<=\().*(?=\))', str).group(0)


def _simple_array(str):
    return re.findall(simple_array_pattern, str)


def _object_array(str):
    return re.findall(object_array_pattern, str)


def _object(str):
    return re.findall(object_pattern, str)


def _simple(str):
    return [s for s in str]


def is_field(str):
    return str.find(':') != -1
