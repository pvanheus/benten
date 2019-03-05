import pathlib
import os
import shutil

from benten.editing.cwlprocess import CwlProcess
from benten.models.tool import Tool

current_path = pathlib.Path(__file__).parent
test_dir = "tool-model-test-temp-cwl-dir"


def setup():
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)


def teardown():
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)


def test_parsing_empty_tool():

    path = pathlib.Path(test_dir, "nothing.cwl")

    with open(path, "w") as f:
        f.write("")

    cwl_doc = CwlProcess.create_from_file(path)
    cwl_doc.compute_cwl_dict()
    t = Tool(cwl_doc=cwl_doc)

    assert t.cwl_doc == cwl_doc
