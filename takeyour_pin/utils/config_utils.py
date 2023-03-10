from yaml import load, FullLoader

from os import path, curdir


def config(config_file: str | None = None) -> dict:

  path_yaml = path.abspath(curdir)

  file_yaml = "config.yaml" if config_file is None else config_file

  with open(f'{path_yaml}/{file_yaml}', "r") as file:

    config_list = load(file, Loader=FullLoader)

  return config_list
