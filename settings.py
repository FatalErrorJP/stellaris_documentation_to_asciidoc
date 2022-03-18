#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# 共通設定
# DOCUMENTATION_BASE_DIR: 読み込み元のログファイルディレクトリパス
# OUTPUT_DIR: AsciiDocファイルの出力先ディレクトリ
###############################################################################
import os
DOCUMENTATION_BASE_DIR = os.environ['USERPROFILE'] + '\Documents\Paradox Interactive\Stellaris\logs\script_documentation'
OUTPUT_DIR = '.\output'

###############################################################################
# AsciiDocのテンプレート設定
###############################################################################
TEMPLATE_TITLE = '''= {name} List
:table-caption: 表

'''
TEMPLATE_HEADER = '''[cols="{num}*a", separator=：, options="autowidth,header"]
.{name}
|===
{headers}
'''
TEMPLATE_DATA = '： {data}\n'
TEMPLATE_EXAMPLE = '''： ----
{data}\n
----
'''
TEMPLATE_FOOTER = '|===\n'
