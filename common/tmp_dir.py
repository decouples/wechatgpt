# encoding:utf-8
import os
import pathlib


class TmpDir(object):
    """A temporary directory that is deleted when the object is destroyed."""

    tmpFilePath = pathlib.Path("./tmp/")

    def __init__(self):
        pathExists = os.path.exists(self.tmpFilePath)
        if not pathExists:
            os.makedirs(self.tmpFilePath)

    def path(self):
        return str(self.tmpFilePath) + "/"
