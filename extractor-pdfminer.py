#!/usr/bin/env python

import logging
import os

from pdfminer.high_level import extract_text
from pyclowder.extractors import Extractor
import pyclowder.files

# create log object with current module name
log = logging.getLogger(__name__)


class ExtractorPdfminer(Extractor):
    def __init__(self):
        Extractor.__init__(self)

        # add any additional arguments to parser
        # self.parser.add_argument('--max', '-m', type=int, nargs='?', default=-1,
        #                          help='maximum number (default=-1)')

        # parse command line and load default logging configuration
        self.setup()

        # setup logging for the extractor
        logging.getLogger('pyclowder').setLevel(logging.DEBUG)
        logging.getLogger('__main__').setLevel(logging.DEBUG)

    def process_message(self, connector, host, secret_key, resource, parameters):
        # Process the file and upload the results
        # uncomment to see the resource
        # log.info(resource)
        # {'type': 'file', 'id': '6435b226e4b02b1506038ec5', 'intermediate_id': '6435b226e4b02b1506038ec5', 'name': 'N18-3011.pdf', 'file_ext': '.pdf', 'parent': {'type': 'dataset', 'id': '64344255e4b0a99d8062e6e0'}, 'local_paths': ['/tmp/tmp2hw6l5ra.pdf']}

        input_file = resource["local_paths"][0]
        input_file_id = resource['id']
        dataset_id = resource['parent'].get('id')
        # get input filename without extension
        input_filename = os.path.splitext(os.path.basename(resource["name"]))[0]

        # output filename
        output_txt_file = f'{input_filename}_pdfminer.txt'

        text = extract_text(input_file)
        with open(output_txt_file, 'w') as f:
            f.write(text)

        log.info("Output text files generated : %s", output_txt_file)
        connector.message_process(resource, "Pdf to text conversion finished.")

        # clean existing duplicate
        files_in_dataset = pyclowder.datasets.get_file_list(connector, host, secret_key, dataset_id)
        for file in files_in_dataset:
            if file["filename"] == output_txt_file:
                url = '%sapi/files/%s?key=%s' % (host, file["id"], secret_key)
                connector.delete(url, verify=connector.ssl_verify if connector else True)
        connector.message_process(resource, "Check for duplicate files...")

        # upload to clowder
        pyclowder.files.upload_to_dataset(connector, host, secret_key, dataset_id, output_txt_file)
        connector.message_process(resource, "Uploading output text file to Clowder...")


if __name__ == "__main__":
    # uncomment for testing
    #text = extract_text("tests/pdf/N18-3011.pdf")
    #print(text)

    extractor = ExtractorPdfminer()
    extractor.start()
