#!/usr/bin/env python
import yaml
import sys
import os


def mkdir_by_path(path_list):
    try:
        os.mkdir(os.path.join(".","/".join(path_list)))
    except OSError as exc:
        pass

def create_recursive_directories(directory_description, parent_tree:list):
    if isinstance(directory_description, dict):
        for path_part in directory_description:
            inside_directory = directory_description[path_part]
        
            if isinstance(inside_directory, list):
                
                for sub_path_part in inside_directory:
                    
                    parent_tree_copy = list(parent_tree)
                    
                    parent_tree_copy.append(path_part)

                    mkdir_by_path(parent_tree_copy)

                    create_recursive_directories(sub_path_part, parent_tree_copy)
            else:
                    parent_tree_copy = list(parent_tree)
                    
                    parent_tree_copy.append(path_part)

                    mkdir_by_path(parent_tree_copy)
    else:
        parent_tree_copy = list(parent_tree)
        
        parent_tree_copy.append(str(directory_description))

        mkdir_by_path(parent_tree_copy)

with open(sys.argv[1], 'r') as config_file_stream:
    try:
        config_file_dictionary = yaml.load(config_file_stream)
        
        create_recursive_directories(config_file_dictionary, [])

        print("Successfully created directories")
    except yaml.YAMLError as exc:
        print(exc)