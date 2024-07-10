import urllib.request
import os

def report(blocknr, blocksize, size):
    current = blocknr * blocksize
    percent = 100.0 * current / size
    sys.stdout.write("\rDownloading... {0:.2f}%".format(percent))
    sys.stdout.flush()

def downloadFile(url):
    try:
        fname = url.split('/')[-1]
        urllib.request.urlretrieve(url, fname, reporthook=report)
        print("\nDownload complete!")
    except Exception as e:
        print("\nDownload failed: ", e)

if __name__ == "__main__":
    tld = "http://www.tutorialspoint.com/"
    print("Name of Tutorial? ")
    query = input().strip()  # Use input() for Python 3.x, strip() to remove any extra whitespace

    url = tld + query + '/' + query + '_tutorial.pdf'
    print("Downloading PDF for " + query + "...")
    downloadFile(url)

    print("\nComplete PDF for " + query + " has been downloaded.")
