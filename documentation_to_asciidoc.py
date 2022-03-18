#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import settings
import os
from document_type import DocumentType

def main():
	
	if not os.path.exists(settings.OUTPUT_DIR):
		os.mkdir(settings.OUTPUT_DIR)

	for document in DocumentType:
		write_asciidoc(document)


def write_asciidoc(document):
	# ファイルパス設定
	doc_info = document.value
	input_file = os.path.join(settings.DOCUMENTATION_BASE_DIR, doc_info['name'] + '.log')
	output_file = os.path.join(settings.OUTPUT_DIR, document.name + '.adoc')

	# ファイル出力開始
	with open(output_file, 'w', encoding='utf-8') as wf:
		# タイトル行
		wf.writelines(settings.TEMPLATE_TITLE.format(name=document.name))
		# テーブルヘッダー
		wf.writelines(
			settings.TEMPLATE_HEADER.format(num=doc_info['num']
			, name=document.name
			, headers=doc_info['headers']))
		# テーブルデータ
		convert_asciidoc(document, input_file, wf)
		# テーブルフッター
		wf.writelines(settings.TEMPLATE_FOOTER)


def convert_asciidoc(document, input_file, wf):
	# データ部は、ドキュメント毎にフォーマットが異なるため、処理を分ける
	if document in(DocumentType.Effects, DocumentType.Triggers):
		convert_effects(input_file, wf)
	elif document == DocumentType.Scopes:
		convert_scopes(input_file, wf)
	elif document == DocumentType.Modifiers:
		convert_modifiers(input_file, wf)


def convert_effects(input_file, wf):
	with open(input_file) as rf:
		for line in rf:
			# 「 - 」を含む行になるまでは無視
			if ' - ' not in line:
				continue

			# Name, Descの取得
			name, desc = line.split(' - ', 1)

			# Exsample, Supported Scopesの取得
			example = ''
			scopes = ''
			while True:
				line = next(rf)
				if 'Supported Scopes' in line:
					# Scopes
					scopes = line.split(':')[1]
					break
				else:
					# Example
					example += line

			# 取得した各データの出力
			wf.writelines(settings.TEMPLATE_DATA.format(data=name.strip()))
			wf.writelines(settings.TEMPLATE_DATA.format(data=desc.strip()))
			wf.writelines(settings.TEMPLATE_EXAMPLE.format(data=example.strip()))
			wf.writelines(settings.TEMPLATE_DATA.format(data=scopes.strip()))
			wf.writelines('\n')


def convert_scopes(input_file, wf):
	with open(input_file) as rf:
		for line in rf:
			# 「 - 」を含む行になるまでは無視
			if ' - ' not in line:
				continue

			# Name, Descの取得
			name, desc = line.split(' - ', 1)

			# 取得した各データの出力
			wf.writelines(settings.TEMPLATE_DATA.format(data=name.strip()))
			wf.writelines(settings.TEMPLATE_DATA.format(data=desc.strip()))


def convert_modifiers(input_file, wf):
	with open(input_file) as rf:
		for line in rf:
			# 「 - 」を含む行になるまでは無視
			if not line.startswith('- '):
				continue

			# Name, Descの取得
			tmp = line.split(',', 1)
			name = tmp[0][2:]
			desc = tmp[1].split(':', 1)[1]

			# 取得した各データの出力
			wf.writelines(settings.TEMPLATE_DATA.format(data=name.strip()))
			wf.writelines(settings.TEMPLATE_DATA.format(data=desc.strip()))


if __name__ == "__main__":
	main()