import os
import yaml
import shutil

CURRENT_DIR = os.path.dirname(__file__)

def translate_source(lang='en_us'):

    source_file = '{lang}.yml'.format(lang=lang)
    with open(source_file, 'r') as stream:
        translation_data = yaml.load(stream)
        for project in translation_data:
            print('> Project: {project}'.format(project=project))
            project_src_path = os.path.join(CURRENT_DIR, '..', project)
            project_dst_path = os.path.join(project_src_path, 'out', lang)
            shutil.copytree(project_src_path, project_dst_path, ignore=shutil.ignore_patterns('out'))

            for file_path in translation_data[project]:
                file_to_translate = os.path.join(project_dst_path, file_path)
                print('  > Path: {file_to_translate}'.format(file_to_translate=file_to_translate))
                content = ''
                with open(file_to_translate, 'r') as target_file:
                    content = target_file.read()
                with open(file_to_translate, 'w') as target_file:
                    print('    > File: {file_to_translate}'.format(file_to_translate=translation_data[project]))
                    for pairs in translation_data[project].values():
                        for pair in pairs:
                            for k, v in pair.items():
                                print('      > {k} -> {v}'.format(k=k, v=v))
                                key = '<!--L10N:{k}-->'.format(k=k)
                                content = content.replace(key, v)
                    target_file.write(content)

def list_langs():
    
    lang_to_translate = []
    for file_name in os.listdir(CURRENT_DIR):
        if file_name.endswith('.yml'):
            lang_to_translate.append(file_name[:-4])

    return lang_to_translate

def main():

    for lang in list_langs():
        translate_source(lang)

if __name__ == '__main__':
    main()