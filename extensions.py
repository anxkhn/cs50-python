
def main():
    extn = str(input("Input file name ").strip().lower())
    find(extn)


def find(extn):
    if "." in extn:
        ext = extn.split(".", 1)
        if ext[1] == ("jpg"):
            print("image/jpeg")
        elif ext[1] == ("png"):
            print("image/png")
        elif ext[1] == "gif":
            print("image/gif")
        elif ext[1] == "pdf":
            print("application/pdf")
        elif ext[1] == "zip":
            print("application/zip")
        elif ext[1] == "txt":
            print("text/plain")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")

main()