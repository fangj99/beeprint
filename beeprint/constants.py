# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division

# >> 优先策略
# 正确性优先，尽量正确显示出所有字段，有无法解析的字段立即报错并退出
_PS_CORRECTNESS_FIRST = 1
# 内容优先，尽量保证输出全文，对于无法解析的字段以预置内容代替
# 比如：<CAN NOT PARSE OBJECT>
_PS_CONTENT_FIRST = 2

# an element will occupy a single block 
# it has its own leading spaces
_AS_ELEMENT_ = 1
# compares to _AS_ELEMENT_, a value is a component of an element
# it has not leading spaces except a span between a key
# it belongs to a key
_AS_VALUE_ = 2
# when display, these elements need comma between each others
# it must has a parent block
# eg: [1, 2], {'key1': 'val1', 'key2': 'val2'}, (1, 2)
_AS_LIST_ELEMENT_ = \
    _AS_TUPLE_ELEMENT_ = 4

_AS_DICT_ELEMENT_ = 8
_AS_CLASS_ELEMENT_ = 16

# string type
_ST_LITERAL_ = 1 # string literal depends on script's coding
_ST_UNICODE_ = 2
_ST_BYTES_ = 4
_ST_UNDEFINED_ = 0

# debug level
_DL_MODULE_ = 1
_DL_FUNC_ = 2
_DL_STATEMENT = 3

# long string 
_LS_WRAP_BY_NONE = 0
_LS_WRAP_BY_TERMINAL = 1
_LS_WRAP_BY_80_COLUMN = 2
