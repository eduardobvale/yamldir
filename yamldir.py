#!/usr/bin/env python
import yaml
import sys
import os


def mkdir_by_path(parent_tree, path_part):
    parent_tree_copy = list(parent_tree)
                    
    parent_tree_copy.append(str(path_part))

    try:
        os.mkdir(os.path.join(".","/".join(parent_tree_copy)))
    except OSError as exc:
        pass

def create_recursive_directories(directory_description, parent_tree:list):
    if isinstance(directory_description, dict):
        for path_part in directory_description:
            inside_directory = directory_description[path_part]
        
            if isinstance(inside_directory, list):
                
                for sub_path_part in inside_directory:
                    mkdir_by_path(parent_tree, path_part)

                    new_sub_path = list(parent_tree)

                    new_sub_path.append(path_part)
                    
                    create_recursive_directories(sub_path_part, new_sub_path)
            else:
                mkdir_by_path(parent_tree, path_part)
    else:
        mkdir_by_path(parent_tree, directory_description)

with open(sys.argv[1], 'r') as config_file_stream:
    try:
        config_file_dictionary = yaml.load(config_file_stream)
        
        create_recursive_directories(config_file_dictionary, [])

        print("Successfully created directories")
    except yaml.YAMLError as exc:
        print(exc)