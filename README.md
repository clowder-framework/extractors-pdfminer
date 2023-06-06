# extractors-pdfminer
Clowder extractor for pdf files.
This extractor uses the [pdfminer.six](https://github.com/pdfminer/pdfminer.six) library to extract textual information from pdf files. 

## Build extractor image

- Run `docker build . -t hub.ncsa.illinois.edu/clowder/extractor-pdfminer:<version>` to build docker image
- If you ran into error `[Errno 28] No space left on device:`, try below:
    - Free more spaces by running `docker system prune --all` 
    - Increase the Disk image size. You can find the configuration in Docker Desktop

## Publish Image to Private NCSA repo
- Login first: `docker login hub.ncsa.illinois.edu`
- Run `docker image push hub.ncsa.illinois.edu/clowder/extractor-pdfminer:<version>`

## Deployment
- Please refer to Clowder instructions

