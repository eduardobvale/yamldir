# yamldir
Python tool to create a directory based on a yaml

# Usage

Create a yaml file with your folder structure like this:

```
%YAML 1.2
---
Projects:
  - Open Source:
    - yamldir
    - another_proj
```

and run the python script like this:

````
python yamldir.py [file.yaml]
````
